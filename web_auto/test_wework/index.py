from selenium.webdriver.common.by import By
from time import sleep
#from web_auto.test_wework.add_member import AddMember
from cekai.web_auto.test_wework.base_page import BasePage
from cekai.web_auto.test_wework.add_member import AddMember


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加成员index_service_cnt_itemWrap
        :return:
        """
        find = self.find
        def add_member_condition(x):
            elements_len = len(self.finds(By.ID,"username"))
            if elements_len <= 0:
                find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
            return elements_len > 0


        find(By.CSS_SELECTOR,"#menu_contacts").click()
        sleep(2)
        #self.wait_for_click((By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)"))
        self.wait_for_condition(add_member_condition).click()
        return AddMember(self._driver)

    def goto_import_address(self):
        """
        导入通讯录x
        :return:
        """
        pass
    def goto_join_number(self):
        """
        成员加入
        :return:
        """