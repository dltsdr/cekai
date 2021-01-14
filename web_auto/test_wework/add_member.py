from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
#from web_auto.test_wework.base_page import BasePage
from cekai.web_auto.test_wework.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        """
        添加成员页面，实现成员添加
        :return:
        """
        find = self.find
        find(By.ID, "username").send_keys("D")
        find(By.ID, "memberAdd_acctid").send_keys("16234")
        find(By.ID, "memberAdd_phone").send_keys("17347638617")
        find(By.CSS_SELECTOR, ".js_btn_save").click()


        pass