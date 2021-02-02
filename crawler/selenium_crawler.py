# -*-coding:utf-8-*-
"""
https://www.oneyac.com/
爬取品牌数据
"""
import time
import traceback
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from selenium import webdriver
# import MySQLdb
from selenium.webdriver.support.wait import WebDriverWait


class Command(BaseCommand):
    def handle(self, *args, **options):
        Crawler()()


class Crawler(object):
    def __init__(self):
        # self.db = MySQLdb.connect("192.168.2.14", "jydemo", "asdasd", "jiayou3_test_mini", charset='utf8')
        self.browser = webdriver.Firefox(executable_path='/home/hua/geckodriver')  # 火狐浏览器
        self.cursor = self.db.cursor()
        self.url = "https://www.oneyac.com/brand/886.html"          # 某个品牌url
        self.brand_url = "https://www.oneyac.com/brand/list.html"   # 品牌区url

    @property
    def get_browser_data(self):
        browser = self.browser
        browser.get(self.url)
        wait = WebDriverWait(browser, 4)
        pages = int(browser.find_element_by_id("list_totalPages").text)
        p = 1
        while p < pages:
            print(u'第%s页' % p)
            #  翻页方式
            element1 = browser.find_element_by_link_text(u'下一页')
            time.sleep(2)
            browser.execute_script("arguments[0].click();", element1)
            browser = self.get_html_content(browser)
            p += 1
        # start****************最后一页数据(上面无法拿到最后一页的数据，所以重新写个跳转拿最后一页的数据)**********
        print(u'第%s页' % pages)
        browser.find_element_by_xpath('//*[@id="list_pagination"]/span[2]/input').send_keys(pages)
        browser.find_elements('xpath', '/html/body/div[4]/div[2]/div[3]/div[2]/span[2]/button')
        element1 = browser.find_element_by_css_selector('#list_pagination > span.page-go > button')
        browser.execute_script("arguments[0].click();", element1)
        browser = self.get_html_content(browser)
        # end**************************
        browser.close()

    def get_html_content(self, browser):
        soup = BeautifulSoup(browser.page_source, "lxml")
        # 表头和表数据
        # data_head = soup.select("#list_thead")[0]         # 表头数据
        data_talbe = soup.select("#list_tbody_list")[0]     # 表数据
        name_list = data_talbe.findAll("a", attrs={'class': 'listPro_code preText'})    # 型号列表
        desc_list = data_talbe.findAll(attrs={'class': 'listPro_desc'})                 # 描述列表
        key_params_list = data_talbe.findAll("div", attrs={'class': 'c-attrs_con'})     # 关键参数列表
        price_list = data_talbe.findAll("tbody")                                        # 单价参数列表
        stock_list = data_talbe.findAll("span", attrs={'class': 'text-warning text-bold fs-14'})  # 库存参数列表
        # 遍历表格记录
        for i in range(len(name_list)):
            name = name_list[i].text
            desc = desc_list[i].text.replace('\n', '').replace(' ', '')[:64]
            key_params = key_params_list[i].text.replace('\n', '').replace(' ', '')
            price = price_list[i].text.replace('\n', '').replace(' ', '')
            try:
                stock = stock_list[i].text.replace('\n', '').replace(' ', '')
            except:
                stock = 0
            self.data_insert_db(name, desc, key_params, price, stock)
        return browser

    def data_insert_db(self, name, desc, key_params, price, stock):
        """插入数据库"""
        sql = """insert into jiayou3_test_mini.crawler_data (`name`, `desc`, key_params, price, stock) values ('%s', '%s', '%s', '%s', '%s')""" % (name, desc, key_params, price, stock)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print(traceback.print_exc())
            self.db.rollback()

    @property
    def get_all_brand_url(self):
        """获取所有品牌url"""
        url_list = list()
        self.browser.get(self.brand_url)
        wait = WebDriverWait(self.browser, 4)
        soup = BeautifulSoup(self.browser.page_source, "lxml")
        data = soup.select('#bandList')[0]
        brand_list = data.findAll("div", attrs={'class': 'BD-lstSec__ul'})  # 整个页面的brand div集合
        for brands in brand_list:
            div_url_list = brands.findAll("a")
            for one in div_url_list:
                url_list.append(one['href'])
        self.browser.close()
        return url_list

    def __call__(self, *args, **kwargs):
        self.get_browser_data
        self.db.close()


if __name__ == '__main__':
    # Crawler()()
    cls = Crawler()
    cls.get_all_brand_url

