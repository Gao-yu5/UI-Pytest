# -*- coding:utf-8 -*-
import os
import time
import allure
import pytest

from utils.tools import *
from utils.decorators import error_screenshot
from pages.login_page import *
from settings import MODULE_DIR


# 获取测试数据
test_data = get_yaml_test_login(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))


@allure.feature('登录')
class TestLoginPage(LoginPage):

    @allure.story('登陆界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('username,password', test_data)
    def test_login(self,username,password, browser):
        browser.login_interface(url=  self.URL,
                                login_button=self.LOGIN_BUTTON,
                                # login_position=self.LOGIN_POSITION,
                                username={'locator': self.USERNAME_INPUT, 'value': username},
                                password={'locator': self.PASSWORD_INPUT, 'value': password})
        assert browser.get_current_url()=="http://47.111.8.42:8080/mms/mms/index.html"



