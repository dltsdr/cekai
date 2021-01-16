from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_auto.web_po.login import Login
from web_auto.web_po.register import Register


class Index:
    """
    首页
    """
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        点击立即注册
        进入到注册的po
        :return:
        """
        #立即注册
        self.driver.find_element(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self.driver)

    def goto_add_member(self):
        pass