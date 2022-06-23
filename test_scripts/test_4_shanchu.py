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

@allure.feature('删除顾客信息')
class Test_shanchuPage(shanchu_gk,shanchu_jbr,shannchu_yaop):
    @allure.story('删除顾客界面测试')
    @error_screenshot()
    def test_shanchu_guke(self, browser):
        browser.shanchu_interdace(can1=self.shan_xinxi,
                                  can2=self.shan_guke,
                                  can3=self.shanchu_name,
                                  can4=self.shanchu_dianji,
                                  can5=self.shanchu_ok
                                    )

    @allure.story('删除经办人界面测试')
    @error_screenshot()

    def test_shanchu_pope(self, browser):

        browser.shanchu_yaop_pope(  can=self.shan_xinxi_1,
                                    can1=self.jbr_sxx,
                                    can2=self.jbr_name,
                                    can3=self.JBR_SC,
                                    can4=self.JBR_OK,
                          )




    @allure.story('删除药品界面测试')
    @error_screenshot()

    def test_shanchu_yaop(self, browser):
        browser.shanchu_yaop_pope(  can=self.shan_xinxi_2,
                                    can1=self.yao_xi,
                                    can2=self.yao_name,
                                    can3=self.yao_sc,
                                    can4=self.yao_ok,
                                    )
