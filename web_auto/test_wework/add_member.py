from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddMember:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def add_member(self):
        dr = self.driver
        dr.find_element(By.ID, "username").send_keys("D")
        dr.find_element(By.ID, "memberAdd_acctid").send_keys("16234")
        dr.find_element(By.ID, "memberAdd_phone").send_keys("17347638617")
        dr.find_element(By.CSS_SELECTOR, ".js_btn_save").click()


        pass