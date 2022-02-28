from Common.base_page import BasePage


class SetPage(BasePage):

    # 姓名定位
    user_name_input = ("xpath", '//*[@id="user_name"]')

    # 头像定位
    user_img_btn = ("xpath", '//*[@id="user_avatar"]')

    # 保存按钮定位
    user_save_btn = ("xpath", '//*[@id="edit_user_67526"]/div[2]/button')

    # 更新成功文案定位
    alert_success = ("xpath", '//*[@id="main"]/div[1]')

    def update_name(self, user_name):
        """修改用户名"""
        self.send_input(self.user_name_input, user_name)
        return self

    def update_img(self, user_img):
        """修改头像"""
        self.input_file(self.user_img_btn, user_img)
        return self

    def update_btn(self):
        """点击更新按钮"""
        self.click_element(self.user_save_btn)
        return self

    def update_text(self):
        """更新成功信息"""
        T = self.get_text(self.alert_success)
        return T
