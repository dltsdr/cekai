from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import yaml,random

class Test():
    def setup_method(self,method):
        options = Options()
        #和浏览器打开的调试端口进行调试
        options.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        #self.driver = webdriver.Chrome()

    #将cookies存入yaml中
    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        print(cookie)
        with open("cookies.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    #读取yaml中的cookies
    def test_login(self):
        phone="136"+str(random.randint(11111111,99999999))
        dr = self.driver
        dr.get("https://work.weixin.qq.com/")
        with open("cookies.yaml",encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                dr.add_cookie(cookie)
        dr.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(3)
        #点击添加成员
        dr.find_element_by_xpath("//div[@class='ww_operationBar']/a[@class='qui_btn ww_btn js_add_member']").click()
        sleep(3)
        #添加人员信息
        dr.find_element_by_id("username").send_keys("webui")
        dr.find_element_by_id("memberAdd_acctid").send_keys("webui321")
        dr.find_element_by_id("memberAdd_phone").send_keys(phone)
        dr.find_element_by_xpath("//form[@class='js_member_editor_form']/div[1]/a[2]").click()
        sleep(2)
        phone_find = "//td[@title="+phone+"]"
        try:
            dr.find_element_by_xpath(phone_find).is_displayed()
            print("电话为"+phone+"的成员添加成功")
        except BaseException as msg:
            print(msg)
            print("电话为"+phone_find+"的成员添加失败")


