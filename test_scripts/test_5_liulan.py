# -*- coding:utf-8 -*-
import os
import time
import allure
import pytest

from utils.tools import *
from utils.decorators import error_screenshot
from pages.login_page import *
from settings import MODULE_DIR

@allure.feature('信息查询')
class TestliulanPage(look_guke):

    @allure.story('顾客浏览界面测试')
    @error_screenshot()

    def test_liulan_guke(self,  browser):
        browser.liulan_gk(can1=self.kook_1,
                          can2=self.kook_2,
                          can3=self.kook_3,
                            can4=self.kook_4,
                            can5=self.kook_5
                          )
        assert "编号:4396" in browser.get_current_page_source()

    # @allure.story('经办人浏览界面测试')
    # @error_screenshot()
    #
    # def test_liulan_pope(self,browser):
    #     browser.chaxun_interdace_pope(
    #
    #                              chacun_button1=self.jinbanr,
    #                              guke={"locator": self.jinbanr_id, "value": pope},
    #                              chacun_button2=self.CHA,
    #                             chacun_button3=self.x_annaiu2
    #                                   )
    #     assert "1001239" in browser.get_current_page_source()
    #
    #
    #
    # @allure.story('药品浏览界面测试')
    # @error_screenshot()
    # def test_liulan_yaop(self, yaop, browser):
    #     browser.chaxun_interdace_yaop(
    #                              chacun_button1=self.xx,
    #                              guke={"locator": self.GG, "value": yaop},
    #                              chacun_button2=self.HA,
    #                                   )
    #     assert "1000007667" in browser.get_current_page_source()
        # browser.quit_browser()
