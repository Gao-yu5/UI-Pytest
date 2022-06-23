# -*- coding:utf-8 -*-
"""
封装各种公共的业务功能方法
"""

from utils.driver_base import DriverBase
from utils.tools import *
from pages.login_page import *

class Drivers(DriverBase):

    def __init__(self, driver='Chrome', enable_headless=False, enable_no_picture=False, enable_maximize_window=False):
        super(Drivers, self).__init__(driver, enable_headless, enable_no_picture, enable_maximize_window)

    def login_interface(self, url, login_button, login_position=None, username={}, password={}):
        """
        进入登陆界面，模拟登陆
        :param url: Login URL
        :param login_button: 登陆按钮locator
        :param login_position: 进行登陆的页面位置（如果需要切换的话）
        :param username: 用户名，字典格式：{'locator': '//', 'value': 'abc'}
        :param password: 密码，字典格式：{'locator': '//', 'value': '456'}
        :return:
        """
        self.open_windows(url=url)

        if login_position:  # 有些页面要切换到指定地方，才能进行登陆
            self.click_button(locator=login_position)

        self.send_keys(locator=username['locator'], value=username['value'])
        self.send_keys(locator=password['locator'], value=password['value'])
        self.click_button(login_button)
    def chaxun_interdace(self,chacun_button,chacun_button1,chacun_button2,
                         # chacun_button3,
                         guke={}):
        # 先登录
        # a=LoginPage()
        # self.open_windows(url= 'http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT),value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT),value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 点击信息查询
        self.click_button(chacun_button)
        # 查询顾客信息
        # 查询
        self.click_button(chacun_button1)
        # 输入顾客编号
        self.send_keys(locator=guke["locator"],value=guke["value"])
        # 点击查询
        self.click_button(chacun_button2)
        # assert "1001239" in browser.get_current_page_source()
        # self.click_button(chacun_button3)
        self.refresh()

    def chaxun_interdace_pope(self,chacun_button,chacun_button1,chacun_button2,chacun_button3,guke={}):
        # 先登录
        # a=LoginPage()
        # self.open_windows(url= 'http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT),value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT),value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 点击信息查询
        self.click_button(chacun_button)
        # 查询经办人信息
        self.click_button(chacun_button1)
        # 输入经办人编号
        self.send_keys(locator=guke["locator"],value=guke["value"])
        # 点击查询
        self.click_button(chacun_button2)

        self.click_button(chacun_button3)
        self.refresh()
    def chaxun_interdace_yaop(self,chacun_button,chacun_button1,chacun_button2,guke={}):
        # 先登录
        # a=LoginPage()
        # self.open_windows(url= 'http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT),value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT),value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 点击信息查询
        self.click_button(chacun_button)
        # 查询药品人信息
        self.click_button(chacun_button1)
        # 输入药品编号
        self.send_keys(locator=guke["locator"],value=guke["value"])
        # 点击查询
        self.click_button(chacun_button2)
        self.refresh()
    def luru_guke_interdace(self,chacun_button778,chacun_button1,
                        chacun_button2,ida={},name={},age={},tele={},poper={},
                       time={},med={},address={},dale={},bei={}
                            ):
        # 先登录
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 点击信息录入
        self.click_button(chacun_button778)
        # 点击录入顾客信息
        self.click_button(chacun_button1)
        # 输入编号
        self.send_keys(locator=ida["locator"], value=ida["value"])
        # 输入name
        self.send_keys(locator=name["locator"], value=name["value"])
        # 输入age
        self.send_keys(locator=age["locator"], value=age["value"])
        # 输入电话
        self.send_keys(locator=tele["locator"], value=tele["value"])
        # 输入经办人
        self.send_keys(locator=poper["locator"], value=poper["value"])
        # 日期
        self.send_keys(locator=time["locator"], value=time["value"])
        # 药品
        self.send_keys(locator=med["locator"], value=med["value"])
        # 住址
        self.send_keys(locator=address["locator"], value=address["value"])
        # 症状
        self.send_keys(locator=dale["locator"], value=dale["value"])
        # 备注
        self.send_keys(locator=bei["locator"], value=bei["value"])
        # 点击录入
        self.click_button(chacun_button2)
        self.refresh()
    def luru_pope(self,can,can1,can2,can3,ida={},name={},tele={},bz={}):
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 点击信息录入
        self.click_button(can)
         # 点击录入经办人
        self.click_button(can1)
         # 编号
        self.send_keys(locator=ida["locator"], value=ida["value"])
         # 姓名
        self.send_keys(locator=name["locator"], value=name["value"])
         # 电话
        self.send_keys(locator=tele["locator"], value=tele["value"])
         # 备注
        self.send_keys(locator=bz["locator"], value=bz["value"])
        self.click_button(can2)
        self.click_button(can3)
        self.refresh()
    def luru_yaop(self,can,can1,can2,can3,ida={},name={},bz={}):
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 点击信息录入
        self.click_button(can)
        # 点击录入药品
        self.click_button(can1)
        # 编号
        self.send_keys(locator=ida["locator"], value=ida["value"])
        # 名称
        self.send_keys(locator=name["locator"], value=name["value"])
            # 功效
        self.send_keys(locator=bz["locator"], value=bz["value"])
        # 点击录入
        self.click_button(can2)
        # 点击确定
        self.click_button(can3)
        self.refresh()

    def shanchu_interdace(self,can1,can2,can3,can4,can5):
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 信息删除
        self.click_button(can1)
        # 顾客删除
        self.click_button(can2)
        # 选择guke
        self.click_button(can3)
        # 点击产删除
        self.click_button(can4)
        # 点击确定
        self.click_button(can5)
        self.refresh()
    def shanchu_yaop_pope(self,can,can1,can2,can3,can4):
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # self.click_button(can)
        # 删除r和药品
        self.click_button(can1)
        # 选择删除人
        self.click_button(can2)
        # 点击产删除
        self.click_button(can3)
        # 点击确定
        self.click_button(can4)
        self.refresh()

    def xiugai_interdace(self,can1,can2,can3,can4,can5,ida={},tele={}):
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        # 信息修改
        self.click_button(can1)
        # 顾客修改
        self.click_button(can2)
        # 输入编号
        self.send_keys(locator=ida["locator"], value=ida["value"])
        # 点击查询
        self.click_button(can3)
        # 修改内容
        self.send_keys(locator=tele["locator"], value=tele["value"])
        # 点击修改
        self.click_button(can4)
        # 点击确定
        self.click_button(can5)
        self.refresh()
    def xiugai_pope_yaop(self,can1,cnn2,can3,can4,ida={},te={}):
        # 人修改
        self.click_button(can1)
        # 输入编号
        self.send_keys(locator=ida["locator"], value=ida["value"])
        # 点击查询
        self.click_button(can2)
        # 修改内容
        self.send_keys(locator=tele["locator"], value=tele["value"])
        # 点击修改
        self.click_button(can3)
        # 点击确定
        self.click_button(can4)
        self.refresh()

    def liulan_gk(self,can1,can2,can3,can4,can5):
        # a = LoginPage()
        # self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        # self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        # self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        # self.click_button(a.LOGIN_BUTTON)
        '''
        点击信息浏览
        点击浏览顾客
        选择顾客
        点击查看
        关闭窗口
        '''
        self.click_button(can1)
        self.click_button(can2)
        self.click_button(can3)
        self.click_button(can4)
        self.click_button(can5)
        self.refresh()
    def liulan_pope_yaop(self,can1):
        '''
        点击人和药品查看
        '''
        self.click_button(can1)
    def daying(self,can1,can2,can3,can4):
        '''
        点击数据报表
        点击顾客
        选择内容
        点击打印
        '''
        self.click_button(can1)
        self.click_button(can2)
        self.click_button(can3)
        self.click_button(can4)
    def dayin_pope_yaop(self,can1,can2,can3):
        '''
        点击顾客
        选择内容
        点击打印

        '''
        self.click_button(can1)
        self.click_button(can2)
        self.click_button(can3)
    def yonghu1_add(self,can1,can2,can3,user={},password={}):
        a = LoginPage()
        self.open_windows(url='http://47.111.8.42:8080/mms/mms/index.html')
        self.send_keys(locator=(a.USERNAME_INPUT), value="admir")
        self.send_keys(locator=(a.PASSWORD_INPUT), value="1234")
        self.click_button(a.LOGIN_BUTTON)
        '''
        用户管理
        用户管理
        添加
        输入用户
        输入密码
        点击save
        '''
        self.click_button(can1)
        self.click_button(can2)
        self.click_button(can3)
        self.send_keys(locator=user["locator"], value=user["value"])
        self.send_keys(locator=password["locator"], value=password["value"])
        self.click_button(can4)
    def yonghu_xiu(self,can1,can2,can3,can4,user={}):
        '''
        用户管理
        选择内容
        点击编辑
        修改用户
        点击save
        '''
        self.click_button(can1)
        self.click_button(can2)
        self.click_button(can3)
        self.send_keys(locator=user["locator"], value=user["value"])
        self.click_button(can4)
    def yoyhu_del(self,can1,can2,can3):
        '''
        选择内容
        点击删除
        点击确定

        '''
        self.click_button(can1)
        self.click_button(can2)
        self.click_button(can3)