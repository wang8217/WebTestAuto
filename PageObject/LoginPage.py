# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:wy
@File:LoginPage.py
 
"""
import time

from Common.base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    url_home = "http://testerhome.com/account/sign_in"

    # 登录按钮定位
    login_btn = ("xpath", '/html/body/div[1]/div/div[3]/ul/li[2]/a')

    # 用户名定位
    mobile_locator = ("xpath", '//*[@id="user_login"]')

    # 密码定位
    password_locator = ("xpath", '//*[@id="user_password"]')

    # 登录定位
    login_btn2 = ("xpath", '//*[@id="new_user"]/div[4]/input')

    # 记住密码按钮定位
    user_remember = ("xpath",'//*[@id="user_remember_me"]')

    def get_home(self):
        """访问首页"""
        self.driver.get(self.url_home)
        return self

    def login(self, mobile, pwd):
        """用户名与密码"""
        mobile_ele = self.send_input(self.mobile_locator, mobile)
        pw_ele = self.send_input(self.password_locator, pwd)

        """点击登录"""
        login_ele2 = self.click_element(self.login_btn2)
        return self






