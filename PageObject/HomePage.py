from Common.base_page import BasePage
from selenium import webdriver


class HomePage(BasePage):
    # 个人信息头像定位
    user_img = ("xpath", '/html/body/div[1]/div/div[3]/ul/li[3]')

    # 个人信息名称定位
    user_name = ("xpath", '/html/body/div[1]/div/div[3]/ul/li[3]/div/a[1]')

    # 个人资料设置定位
    user_set = ("xpath", '/html/body/div[1]/div/div[3]/ul/li[3]/div/a[3]')

    def login_name_ass(self):
        """获取登录名"""
        self.click_element(self.user_img)
        my_name = self.get_text(self.user_name)
        return my_name

    def user_set_jump(self):
        """跳转个人设置页面"""
        self.click_element(self.user_img)
        self.click_element(self.user_set)
        return self
