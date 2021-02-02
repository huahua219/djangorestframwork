#coding:utf-8
#__author:huahua 
#data:2020-09-14 11:03 AM
"""
背景：供应商通过EDI推送物料发货单信息，我方需要根据供应商推送信息来实现佳友自动核对物料信息
本脚本作用：爬取EDI信息并解析，保存到数据库（EDI库），这些数据用来核对佳友发货单 以及 查找供应商是否少推送了（遗漏）
"""
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiayou.settings")
django.setup()

from django.core.management import BaseCommand
import datetime
import traceback
import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from purchases.management.commands.parsing_po_methods import Logger
from purchases.models import Edi_excute_info, Edi_Po, Edi_Po_line

logger = Logger().logger


class Command(BaseCommand):
    def handle(self, *args, **options):
        SaveEdiData().save_data()


class EdiSpider(object):
    """
    封装EDI爬虫方法，爬取发货单数据
    """
    __username = 'icgooedi'
    __password = 'shimao2018'
    __login_url = "http://edi.icgoo.net:5080/pyas2/login?next=/pyas2/"
    __x_path = '/html/body/div[4]/div[1]/div/form/input/@value'

    def __init__(self):
        self.session = requests.session()

    @property
    def __get_token(self):
        html = self.session.get(self.__login_url)
        html_content = html.text
        result = Selector(text=html_content).xpath(self.__x_path).extract()
        token = str(result[0])
        return token

    @property
    def __login(self):
        payload = {
            'username': self.__username,
            'password': self.__password,
            'csrfmiddlewaretoken': self.__get_token,
            'next': '/pyas2/'
        }
        return self.session.post(self.__login_url, data=payload)

    def __get_html(self, url):
        '''解析页面内容'''
        html = self.session.get(url=url).content
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        return soup

    def __get_page_info(self, url):
        '''获取页面链接及其时间'''
        soup = self.__get_html(url)
        try:
            tags = soup.tbody.find_all("a", class_="pyas2link")  # 获取链接
            element = soup.tbody.find_all('a', text='View MDN')  # 获取时间
            return soup, tags, element
        except:
            logger.error(traceback.format_exc())
            return False

    @property
    def __get_messageUrl(self):
        '''
        1，数据是从最新的一条开始往后爬
        2，以时间点为依据，如果此条url数据小与或等于上次爬取开始的时间（数据上次已经获取），则停止爬取
        采集最新数据信息解析页面获取messageUrl集合
        :return:
        '''
        last_time = Edi_excute_info.objects.using('edi').first().edi_time       #数据库库获取上一次执行时间
        # last_time = datetime.datetime.strptime('2019-04-03 21:06:17', '%Y-%m-%d %H:%M:%S')
        # end_time = datetime.datetime.strptime('2019-04-03 22:08:31', '%Y-%m-%d %H:%M:%S')
        logger.info('last query Time:={}'.format(last_time))
        login = self.__login
        result = []
        pre = "http://edi.icgoo.net:5080/pyas2/payload/"
        last = "/?action=this"
        url = 'http://edi.icgoo.net:5080/pyas2/message/?direction=IN'
        soup, tags, element = self.__get_page_info(url)  #无需判断False，第一次都有值

        pages = int((soup.span.span.get_text()).replace(" ", "").split('of')[1])   # 获取翻页总数
        t_flag = 0                          # 控制记录的时间的标志
        for page in range(pages - 1):
            tmp = 0                         # tmp=1跳出循环的标志
            for j in range(len(tags)):
                EDI_time = (element[j]['href'].split('mdn')[1]).split('.')[0][1:]  # 获取页面时间
                get_time = EDI_time[:4] + '-' + EDI_time[4:6] + '-' + EDI_time[6:8] + ' ' + \
                           EDI_time[8:10] + ':' + EDI_time[10:12] + ':' + EDI_time[12:14]
                get_time = datetime.datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S')

                if page == 0 and t_flag == 0:  # 本次执行时间点写入库，下次接着这个时间点地方爬数据
                    Edi_excute_info.objects.using('edi').create(
                        excute_time=datetime.datetime.now(),
                        edi_time=get_time  # get_time 即是EDI页面Timestamp列时间
                    )
                    t_flag = 1
                # if get_time >= end_time:
                #     continue
                if get_time < last_time:
                    tmp = 1
                    break
                message_id = tags[j].string

                if 'arrow' not in message_id:  # 判断渠道，获取是arrow,digikey来的，过滤出其他的渠道
                    continue
                result.append(pre + tags[j].string + last)
            if tmp == 1:
                break
            # 翻页
            url = "http://edi.icgoo.net:5080/pyas2/message/?direction=IN&page=" + str(page + 2)
            get_info_data = self.__get_page_info(url)
            if get_info_data:
                soup, tags, element = get_info_data

        return result

    @property
    def __get_data(self):
        """
        获取采购单号IDE详细数据
        :return:{url:values} 返回一个字典，key为url,values为对应url页面内容
        """
        data = dict()
        result = self.__get_messageUrl
        logger.info('search_length:{}'.format(len(result)))
        for url in result:
            try:
                soup = self.__get_html(url)
                data[url] = soup.pre.string
            except:
                logger.error(traceback.format_exc())
        return data

    def __call__(self):
        return self.__get_data


class SaveEdiData(object):
    """
    处理爬出来的有效数据写入数据库
    """
    def save_data(self):
        edi_data = EdiSpider()()
        for key, value in edi_data.iteritems():
            try:
                BIG = ((value.split('\nBIG|')[1]).split('\nREF|')[0])
                invoice_number = BIG.split('|')[1]
                try:
                    tracking_number = (value.split('REF|IA|')[1]).split('|')[0]
                    po_number = (BIG.split('|')[-1])
                except:
                    tracking_number = ''
                    po_number = ((value.split('\nBIG|')[1]).split('\n')[0]).split('|')[-1]
                #***start**手动执行代码查寻，根据发票号/采购单号*****
                # if invoice_number in ['WI00099900', 'WI00101314', 'WSI0766408-30', 'WSI0766411-30']:
                # if po_number != 'PO109924':
                #     print(invoice_number, key)
                # else:
                #     continue
                # ***end*******

                obj,is_exist  = Edi_Po.objects.using('edi').get_or_create(
                    purchase_num=po_number, invoice_num=invoice_number, tracking_number=tracking_number, message_url=key,
                )
                if not is_exist:
                    continue

                IT1 = value.split('\nIT1|')[1:]
                IT1[-1] = IT1[-1].split('TDS|', 1)[0]
                for elem in IT1:
                    check_price = elem.split('|')[3]
                    check_qty = elem.split('|')[1]
                    if check_qty == '0':   #check_qty=0则忽略掉
                        continue
                    # MF = elem.split('|')[8]     #厂商
                    name = elem.split('|')[10]
                    try:
                        origin_place = (elem.split('|')[14]).split('\n')[0]  # 产地可以忽略为空
                    except:
                        origin_place = ''
                    Edi_Po_line.objects.using('edi').create(
                        name=name, check_price=check_price, check_qty=check_qty, origin_place=origin_place, po=obj
                    )
            except:
                logger.error(u'exception_key={}\n{}'.format(key, traceback.format_exc()))



if __name__ == '__main__':
    ret = EdiSpider()()
    # res = SaveEdiData().save_data()
    print(len(ret))