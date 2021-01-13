from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from web_auto.test_wework.add_member import AddMember


class Index:
    def __init__(self):
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        #self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def goto_add_member(self):
        """
        添加成员index_service_cnt_itemWrap
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap").click()
        sleep(3)
        return AddMember(self.driver)
        pass

    def goto_import_address(self):
        """
        导入通讯录
        :return:
        """
        pass
    def goto_join_number(self):
        """
        成员加入
        :return:
        """