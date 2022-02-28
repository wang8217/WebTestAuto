# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:wy
@File:base_page.py
 
"""
import logging
import time
from webbrowser import Chrome

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def find(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
        except Exception as err:
            logging.error(f"元素定位失败：{err}")
        else:
            return e

    def wait_element_visible(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素出现，显性等待"""
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            e = wait.until(expected_conditions.visibility_of_element_located(locator))
        except Exception as err:
            logging.error(f"元素未出现：{err}")
        else:
            return e

    def wait_element_clickable(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可点击，显性等待"""
        try:
            # timeout超时时间20秒，poll_frequency0.2秒获取一次
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            # 直到获取到locator元素
            e = wait.until(expected_conditions.element_to_be_clickable(locator))
        except Exception as err:
            logging.error(f"元素未出现,不可点击：{err}")
            logging.error(f"元素：{locator}")
        else:
            return e

    def send_input(self, locator, keys):
        """输入框输入"""
        e = self.wait_element_visible(locator)
        e.send_keys(keys)
        return self

    def click_element(self, locator):
        """点击元素"""
        e = self.wait_element_clickable(locator)
        e.click()
        return self

    def mouse_until(self, locator):
        """鼠标移至元素处"""
        ac = ActionChains(self.driver)
        ac.move_to_element(self.wait_element_visible(locator)).perform()
        return self

    def get_text(self, locator):
        """获取元素文本"""
        e = self.wait_element_visible(locator).text
        return e

    def input_file(self, locator, input_file):
        """上传文件"""
        e = self.wait_element_visible(locator)
        e.send_keys(input_file)
        return self