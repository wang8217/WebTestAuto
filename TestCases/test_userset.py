import time

import pytest
from PageObject.HomePage import HomePage
from PageObject.SetPage import SetPage
from TestDatas.UserSet_data import userset_data


class Test_user_set():
    @pytest.mark.parametrize("user", userset_data.user_one)
    def test_user_set_success(self, login, user):
        driver = login
        home_set = HomePage(driver)
        home_set.user_set_jump()
        user_set = SetPage(driver)
        # 修改名称
        user_set.update_name(user["user_name"])
        # 修改头像
        user_set.update_img(user["user_img"])
        user_set.update_btn()
        assert user_set.update_text() == '更新成功'



if __name__ == '__main__':
    pytest.main(["test_userset.py"])