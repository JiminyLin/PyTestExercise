#!/usr/bin/python3
# coding=utf-8
import os
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

curDir = os.getcwd()
class TestTestWorkWechat:
    def setup_class(self, method):

        options = Options()
        options.debugger_address = "127.0.0.1:9222"

        #实例webdriver.Chrome，且设置为复用浏览器
        self.driver = webdriver.Chrome(options=options)


    def teardown_(self, method):
        self.driver.quit()

    @pytest.fixture()
    def login(self):
        #登录状态打开企业微信，并把cookies存储到shelve
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies")
        cookie = self.driver.get_cookies()
        db['cookie'] = cookie
        # print(cookie)
        db.close()


    def test_uploadContacs(self,login):
        #打开企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #获取cookies
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        #添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.implicitly_wait(3)

        #查找 导入通讯录按钮
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()

        #上传通讯录
        self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_uploadInputMask').send_keys(curDir+'/datas/通讯录批量导入模板.xlsx')

        #校验上传的文件的文件名
        filename = self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_fileNames').text
        assert filename == '通讯录批量导入模板.xlsx'
        sleep(3)
