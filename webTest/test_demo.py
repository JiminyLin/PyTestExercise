#!/usr/bin/python3
# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_weixin(self):
        self.driver.find_element(By.ID,'menu_contacts').click()
        sleep(3)

    def test_cookies(self):
        cookies =  self.driver.get_cookie()
        print(cookies)

    def test_testdemo(self):
        self.driver.get("https://ceshiren.com")
        