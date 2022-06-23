# -*- coding:utf-8 -*-
"""
mms页面的所有元素
"""

from selenium.webdriver.common.by import By

# 登录
class LoginPage(object):
    URL = 'http://47.111.8.42:8080/mms/login.html'
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[1]/div/input')

    # 查询顾客
class ChaXun(object):
    xinxichaxun=(By.XPATH,"//div[@id='accordion']/div/div/div")
    gukechaxun = (By.XPATH,"//div[@id='SC']/a/span/span")
    shuru=(By.XPATH,"//input[@type='text']")
    chaxun_button = (By.XPATH,"//div[@id='output']/div[2]/div/div/div/div/div[2]/div[2]/a/span/span")
    x_annaiu1=(By.XPATH,"")

class Chacun_pope(object):
    xinxi = (By.XPATH, "//div[@id='accordion']/div/div/div")
    jinbanr =(By.XPATH,"//div[@id='SC']/a[2]")
    # 输入
    jinbanr_id= (By.XPATH, "//input[@type='text']")
    # 点击查询
    CHA= ( By.XPATH,"//a[contains(@href, 'javascript:SAMIdclick()')]")
    # 点击关闭
    x_annaiu2 = (By.XPATH,"/html/body/div[5]/div[1]/div[3]/a")
class ChaXun_yaop(object):
    vv = (By.XPATH,"//div[@id='accordion']/div/div/div")
    # bb = (By.XPATH, "//a[3]/span/span")
    # 药品查询
    xx=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/a[3]/span/span[1]")
    # 输入
    GG=(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/span/input[1]")
# 点击查
    HA = (By.XPATH, "//*[@id='output']/div[2]/div/div/div/div/div[2]/div[2]/a")

# 录入顾客

class Luru(object ):
    luru_by=(By.XPATH,"//*[@id='accordion']/div[2]/div[1]/div[1]")
    luru_guke=(By.XPATH,"//*[@id='EC']/a[1]/span/span[1]")

    ID=(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/form/div/div[1]/span[1]/input[1]")
    name=(By.XPATH,"//*[@id='ECMform']/div/div[1]/span[2]/input[1]")
    age=(By.XPATH,"//*[@id='ECMform']/div/div[2]/span[1]/input[1]")
    tele=(By.XPATH,"//*[@id='ECMform']/div/div[2]/span[2]/input[1]")
    POPE=(By.XPATH,"//*[@id='ECMform']/div/div[2]/span[3]/input[1]")
    TIME=(By.XPATH,"//*[@id='ECMform']/div/div[3]/span[1]/input[1]")
    YAOP=(By.XPATH,"//*[@id='ECMform']/div/div[3]/span[2]/input[1]")
    ZHUZHI=(By.XPATH,"//*[@id='ECMform']/div/div[4]/span/input[1]")
    ZHENGA=(By.XPATH,"//*[@id='ECMform']/div/div[5]/span[1]/textarea")
    BZ=(By.XPATH,"//*[@id='ECMform']/div/div[5]/span[2]/textarea")
    LR=(By.XPATH,"//*[@id='output']/div[2]/div/div/div/div/a/span")


    # 录入经办人
class luru_pope(object):
    luru_by1 = (By.XPATH, "//*[@id='accordion']/div[2]/div[1]/div[1]")
    jinbanr=(By.XPATH,"//*[@id='EC']/a[2]/span/span[1]")

    bianhao=(By.XPATH, '//*[@id="EAMform"]/div[1]/span[1]/input[1]')
    jname=(By.XPATH, "(//input[@type='text'])[2]")
    dianhua=(By.XPATH, '//*[@id="EAMform"]/div[2]/span[2]/input[1]')
    beizhu=(By.XPATH, '//*[@id="EAMform"]/div[3]/span/textarea')

    lurudf=(By.XPATH, "//h1[contains(.,'录入')]")
    luru_ok=( By.XPATH,"//a[contains(.,'确定')]")
    # 录入药品
class luru_yap(object):
    yao_ue=(By.XPATH,"//*[@id='accordion']/div[2]/div[1]/div[1]")
    yao_lur=(By.LINK_TEXT,"录入药品信息")
    yao_id=(By.XPATH,"//form[@id='EMMform']/div/span/input")
    yao_name=(By.XPATH,"//div[2]/span/textarea")
    yao_nen=(By.XPATH,"//div[3]/span/textarea")
    yao_dian=(By.LINK_TEXT,"录入")
    yao_ok=(By.LINK_TEXT,"确定")



class shanchu_gk(object):
    # 信息删除
    shan_xinxi=(By.XPATH,"//div[3]/div/div")
    shan_guke=(By.LINK_TEXT,"删除顾客信息")
    shanchu_name=(By.NAME,"GenreId")
    shanchu_dianji=(By.LINK_TEXT,"删除信息")
    shanchu_ok=(By.LINK_TEXT,"确定")
class shanchu_jbr(object):
    shan_xinxi_1 = (By.XPATH, "//div[3]/div/div")
    jbr_sxx=(By.LINK_TEXT,"删除经办人信息")
    jbr_name=(By.XPATH,"//div[2]/table/tbody/tr/td[2]/div")
    JBR_SC=(By.LINK_TEXT,"删除经办人")
    JBR_OK=(By.LINK_TEXT,"确定")
class shannchu_yaop(object):
     shan_xinxi_2 = (By.XPATH, "//div[3]/div/div")
     yao_xi=(By.LINK_TEXT,"删除药品信息")
     yao_name=(By.XPATH,"//*[@id='datagrid-row-r1-1-4']/td/div")
     yao_sc=(By.LINK_TEXT,"删除药品")
     yao_ok=(By.LINK_TEXT,"确定")

# 修改
# class xiugai_guk(object):
#     guke_xiugai=(By.LINK_TEXT,"信息修改")
#     guke_gai=(By.LINK_TEXT,"修改顾客信息")
#     guke_shur=(By.XPATH,"//input[@type='text']")
#     guke_cah=(By.LINK_TEXT,"查询")
#     guke_name=(By.XPATH,"(//input[@type='text'])[7]")
#     guke_qr=(By.LINK_TEXT,"修改")
#     guke_qu=(By.LINK_TEXT,"确定")
# class pope(object):
#     pope_1 = (By.LINK_TEXT,"修改经办人信息")
#     pope_2 = (By.XPATH,"(//input[@type='text'])[3]")
#     pope_3 = (By.LINK_TEXT,"查询")
#     pope_4 = (By.XPATH,"(//input[@type='text'])[17]")
#     pope_5 = (By.LINK_TEXT,"修改")
#     pope_6 = (By.LINK_TEXT,"确定")
# class yaop(object):
#     yaop_1 = (By.LINK_TEXT,"修改药品信息")
#     yaop_2 = (By.XPATH,"(//input[@type='text'])[5]")
#     yaop_3 = (By.LINK_TEXT,"查询")


# 信息浏览
class look_guke(object):
    kook_1  = (By.XPATH,"//div[5]/div/div")
    kook_2 = (By.XPATH,"//div[5]/div[2]/a/span/span")
    kook_3 = (By.XPATH,"//div[2]/div/div[2]/div/table/tbody/tr/td/div")
    kook_4 = (By.LINK_TEXT,"查看详情")
    # xpath = // div[2] / div / div[2] / div / table / tbody / tr / td / div
    kook_5 = (By.XPATH,"//body/div[7]/div/div[3]/a")
class look_pope(object):
    kook_pope_1 = ()
class look_yaop(object):
    look_yaop_1 = ()

# 用户
# class yonghu_add(object):
#     yonghu_1= (By.LINK_TEXT,"用户管理")
#     yonghu_2 = (By.LINK_TEXT,"用户管理")
#     yonghu_3 = (By.LINK_TEXT,"添加")
#     yonghu_4 = (By.XPATH,"/html/body/div[6]/div[1]/form/div[2]/span/input[1]")
#     YOUHU_5 = (By.XPATH,"/html/body/div[6]/div[1]/form/div[3]/span/input[1]")
#     YOUHU_6= (By.LINK_TEXT,"Save")
# class yh_bianji(object):
#     bj1 = (By.LINK_TEXT, "用户管理")
#     bj2 = (By.LINK_TEXT,"1")
#     bj3= (By.LINK_TEXT,"编辑")
#     bj4 = (By.XPATH,"/html/body/div[6]/div[1]/form/div[2]/span/input[1]")
#     bj5 = (By.LINK_TEXT, "Save")
# class sh_chu(object):
#     sc1= (By.LINK_TEXT,"1")
#     sc12=(By.LINK_TEXT,"删除")
#     sc3=(By.LINK_TEXT,"确定")

