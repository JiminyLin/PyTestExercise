#!/usr/bin/python3
# coding=utf-8
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

