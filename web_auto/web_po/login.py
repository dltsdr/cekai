from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from web_auto.web_po.register import Register


class Login:
    """
    登录页面po
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver
    def scan(self):
        """
        扫描二维码
        :return
        """
        pass

    def goto_register(self):
        """
        点击企业登录
        进入到注册的po
        """
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self.driver)