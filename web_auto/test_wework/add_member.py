from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from web_auto.test_wework.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        """
        添加成员页面，实现成员添加
        :return:
        """
        dr = self._driver
        dr.find_element(By.ID, "username").send_keys("D")
        dr.find_element(By.ID, "memberAdd_acctid").send_keys("16234")
        dr.find_element(By.ID, "memberAdd_phone").send_keys("17347638617")
        dr.find_element(By.CSS_SELECTOR, ".js_btn_save").click()


        pass