from selenium.webdriver.common.by import By
from time import sleep
from web_auto.test_wework.add_member import AddMember
from web_auto.test_wework.base_page import BasePage


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加成员index_service_cnt_itemWrap
        :return:
        """

        self._driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap").click()
        sleep(3)
        return AddMember(self._driver)
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