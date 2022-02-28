# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:wy
@File:conftest.py
 
"""
import pytest
from selenium import webdriver

from PageObject.LoginPage import LoginPage
from TestDatas.Login_data import login_data


@pytest.fixture(scope="class")
def browser():
    """启动和关闭浏览器"""
    driver = webdriver.Chrome()
    # 浏览器最大化
    driver.maximize_window()
    yield driver
    driver.quit()

"""已登录前置"""
@pytest.fixture()
def login(browser):
    login_page = LoginPage(browser)
    success = login_data.login_success[0]
    login_page.get_home().login(success["mobile"], success["pwd"])
    yield browser
