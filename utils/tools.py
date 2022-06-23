# -*- coding:utf-8 -*-
"""
工具模块
"""

import os
import yaml
import pandas as pd
from settings import MODULE_DIR
# 登录数据
def get_yaml_test_login(filepath):
    """
    获取Yaml文件的测试数据
    :param filepath: 文件路径
    :return:
    """
    result = []
    with open(filepath, encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['tests']
        for each in test:
            result.append(tuple(each.values()))
    return result



# 顾客信息查询数据
def get_yaml_test_chaxun(filepath):
    # 获取查询的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['chaxun']
        for each in test:
            result.append(tuple(each.values()))
    return result
# 经办人信息查询数据
def get_yaml_test_chaxun1(filepath):
    # 获取查询的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['chaxun1']
        for each in test:
            result.append(tuple(each.values()))
    return result
# 药品查询信息
def get_yaml_test_chaxun2(filepath):
    # 获取查询的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['chaxun2']
        for each in test:
            result.append(tuple(each.values()))
    return result







# 顾客录入信息数据
def get_yaml_test_luru(filepath):
    # 获取录入的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['luru']
        for each in test:
            result.append(tuple(each.values()))
    return result
# 经办人录入信息
def get_yaml_test_luru_pope(filepath):
    # 获取录入的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['luru_pope']
        for each in test:
            result.append(tuple(each.values()))
    return result
# 药品录入信息
def get_yaml_test_luru_yaop(filepath):
    # 获取录入的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['luru_yaop']
        for each in test:
            result.append(tuple(each.values()))
    return result





# 顾客信息修改
def get_yaml_test_xiugai_guke(filepath):
    # 获取录入的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['xiugai_guke']
        for each in test:
            result.append(tuple(each.values()))
    return result
# 经办人信息修改
def get_yaml_test_xiugai_pope(filepath):
    # 获取录入的数据
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['xiugai_pope']
        for each in test:
            result.append(tuple(each.values()))
    return result


def get_yaml_test_yonhu(filepath):
    #用户
    result = []
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['yonghu']
        for each in test:
            result.append(tuple(each.values()))
    return result

def get_excel_test_data(filepath, sheet_name):
    """
    获取Excel表格的测试数据
    :param filepath: 文件路径
    :param sheet_name: 工作表名
    :return: 包含所有行的列表
    """
    data = pd.read_excel(filepath, sheet_name=sheet_name)  # 读取表格
    data.fillna('', inplace=True)  # 替换所有的缺失值为空字符""
    new_list = data.values.tolist()
    return new_list
if __name__ == '__main__':
    # test_data = get_yaml_test_login(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_luru(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_luru_pope(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_luru_yaop(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_chaxun(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_chaxun1(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_chaxun2(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_xiugai_pope(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    # test_data = get_yaml_test_xiugai_pope(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    test_data = get_yaml_test_yonhu(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))
    print(test_data)

