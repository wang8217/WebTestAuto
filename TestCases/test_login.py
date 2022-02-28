# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:wy
@File:test_login.py
 
"""
import pytest

from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from TestDatas.Login_data import login_data


class TestLogin:

    @pytest.mark.parametrize("success", login_data.login_success)
    def test_login_success(self, browser, success):
        """登录成功"""
        login_page = LoginPage(browser)
        login_page.get_home().login(success["mobile"], success["pwd"])

        """跳转首页验证登录信息"""
        home_page = HomePage(browser)
        assert home_page.login_name_ass() == success["name"]


if __name__ == '__main__':
    pytest.main(["test_login.py"])


