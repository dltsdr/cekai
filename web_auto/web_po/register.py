from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Register:
    """
    注册页面的po
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def register(self):
        dr = self.driver
        """
        输入内容
        点击下拉框
        :return:
        """
        dr.find_element(By.CSS_SELECTOR,"#corp_name").send_keys("测试企业名称")
        dr.find_element(By.CSS_SELECTOR,"#manager_name").send_keys("MrD")
        return True