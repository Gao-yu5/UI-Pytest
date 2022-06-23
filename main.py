import pytest
import allure
import os



if __name__ == '__main__':
    pytest.main(["-s", "./test_scripts", "--alluredir=./report/result", "--clean-alluredir"])
    os.system("allure generate ./report/result/ -o report/html --clean")
    # shutil.copy('./environment.properties', './report/temp')
    # os.system('allure serve ./report/temp')