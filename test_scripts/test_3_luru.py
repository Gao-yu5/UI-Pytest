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

@allure.feature('录入顾客信息')
class Test_luru_Page(Luru,luru_yap,luru_pope):
    test_data = get_yaml_test_luru(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    @allure.story('录入信息界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('ida,name,age,tele,poper,time,med,address,dale,bei', test_data)
    def test_luru_guke(self,ida,name,age,tele,poper,time,med,address,dale,bei, browser):
        browser.luru_guke_interdace(chacun_button778=self.luru_by,
                                    chacun_button1=self.luru_guke,
                                    ida={"locator": self.ID, "value": ida},
                                     name = {"locator": self.name, "value": name},
                                    age = {"locator": self.age, "value": age},
                                    tele = {"locator": self.tele, "value": tele},
                                    poper = {"locator": self.POPE, "value": poper},
                                     time = {"locator": self.TIME, "value": time},
                                    med = {"locator": self.YAOP, "value": med},
                                    address = {"locator": self.ZHUZHI, "value": address},
                                    dale = {"locator": self.ZHENGA, "value": dale},
                                    bei = {"locator": self.BZ, "value": bei},
                                    chacun_button2=self.LR
                                    )



    test_data1 = get_yaml_test_luru_pope(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    @allure.story('录入经办人界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('ida, name,  tele, bz', test_data1)
    def test_luru_pope(self, ida, name,  tele, bz, browser):
        browser.luru_pope(  can=self.luru_by1
                            ,can1=self.jinbanr
                          ,ida={"locator": self.bianhao, "value": ida}
                          ,name={"locator": self.jname, "value": name}
                          ,tele={"locator": self.dianhua, "value": tele}
                          ,bz={"locator": self.beizhu, "value": bz}
                        , can2=self.lurudf
                          ,can3= self.luru_ok
                          )



    test_data2 = get_yaml_test_luru_yaop(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    @allure.story('录入药品人界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('ida, name,  bz', test_data2)
    def test_luru_yaop(self, ida, name, bz, browser):
        browser.luru_yaop(  can=self.yao_ue
                            ,can1=self.yao_lur
                          , ida={"locator": self.yao_id, "value": ida}
                          , name={"locator": self.yao_name, "value": name}
                          , bz={"locator": self.yao_nen, "value": bz}
                            , can2=self.yao_dian
                          , can3=self.yao_ok
                          )

