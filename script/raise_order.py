# -*-coding:utf-8-*-
"""
需求，给大众点评刷单
selenium极致应用
"""


import time
import traceback
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from selenium import webdriver
from selenium.webdriver import ChromeOptions
# import MySQLdb
from selenium.webdriver.support.wait import WebDriverWait
import re
from mitmproxy import ctx

"""
博客：
https://onefine.blog.csdn.net/article/details/88200217?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-12.baidujs&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-12.baidujs

seleniumyou 有一些特征值(要突破限制就要破解特征值)， 例如下面：
    window.navigator.webdriver
    window.navigator.languages
    window.navigator.plugins.length
"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        Crawler()()


class Crawler(object):
    def __init__(self):
        # self.db = MySQLdb.connect("192.168.2.14", "jydemo", "asdasd", "jiayou3_test_mini", charset='utf8')
        # self.cursor = self.db.cursor()
        # self.driver = webdriver.Firefox(executable_path='/Users/hua/Public/pro/geckodriver')  # 火狐浏览器
        # self.driver = webdriver.Safari()

        self.option = ChromeOptions()  # 实例化一个ChromeOptions对象
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
        # 在调用浏览器驱动时传入option参数就能实现undefined(chrome 79以前版本)
        # self.driver = webdriver.Chrome(executable_path='/Users/hua/Public/pro/chromedriver', options=self.option)
        self.driver = webdriver.Chrome(executable_path='/Users/hua/Public/pro/chromedriver')
        # chrome 79以后版本
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

        self.username = '18025475521'
        self.passward = 'ahua1048459134'

    def open_pages(self):
        self.driver.get('https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F')
        iframe = self.driver.find_element_by_xpath('//*[@id="J_login_container"]/div/iframe')
        self.driver.switch_to.frame(iframe)   # 切换窗口iframe
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[5]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tab-account"]').click()

        username = self.driver.find_element_by_xpath('//*[@id="account-textbox"]')
        password = self.driver.find_element_by_xpath('//*[@id="password-textbox"]')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.passward)
        self.driver.find_element_by_xpath('//*[@id="login-button-account"]').click()
        # cookies = self.driver.get_cookies()



if __name__ == '__main__':
    # Crawler()()
    cls = Crawler()
    cls.open_pages()

