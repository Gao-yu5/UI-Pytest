# -*- coding:utf-8 -*-
import os
import time
import allure
import pytest

from utils.tools import *
from utils.decorators import error_screenshot
from pages.login_page import ChaXun,Chacun_pope,ChaXun_yaop
from settings import MODULE_DIR


@allure.feature('信息查询')
class TestchaxunPage(ChaXun,Chacun_pope,ChaXun_yaop):
    # 获取测试数据
    test_data = get_yaml_test_chaxun(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    @allure.story('顾客查询界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('guke', test_data)
    def test_chaxun_guke(self,  guke, browser):
        browser.chaxun_interdace(chacun_button=self.xinxichaxun,
                                 chacun_button1=self.gukechaxun,
                                 guke={"locator":self.shuru,"value":guke},
                                 chacun_button2=self.chaxun_button,
                                 # chacun_button3=self.x_annaiu1
                                 )
        assert "小明" in browser.get_current_page_source()


    test_data1 = get_yaml_test_chaxun1(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))

    @allure.story('经办人查询界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('pope', test_data1)
    def test_chaxun_pope(self,pope,browser):
        browser.chaxun_interdace_pope(
            chacun_button=self.xinxi,
                                 chacun_button1=self.jinbanr,
                                 guke={"locator": self.jinbanr_id, "value": pope},
                                 chacun_button2=self.CHA,
                                chacun_button3=self.x_annaiu2
                                      )
        assert "1001239" in browser.get_current_page_source()
        # browser.quit_browser()

    test_data2 = get_yaml_test_chaxun2(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    @allure.story('药品查询界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('yaop', test_data2)
    def test_chaxun_yaop(self, yaop, browser):
        browser.chaxun_interdace_yaop(chacun_button=self.vv,
                                 chacun_button1=self.xx,
                                 guke={"locator": self.GG, "value": yaop},
                                 chacun_button2=self.HA,
                                      )
        assert "1000007667" in browser.get_current_page_source()
