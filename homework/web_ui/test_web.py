from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import yaml

class Test():
    def setup_method(self,method):
        options = Options()
        #和浏览器打开的调试端口进行调试
        options.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        #self.driver = webdriver.Chrome()

    # def teardown_method(self,method):
    #     sleep(5)
    #     self.driver.quit()

    def test_(self):
        # dr = self.driver
        #dr.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.ID, "menu_index").click()

    def test_wework(self):
        self.driver.get("https://work.weixin.qq.com/")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851890906062'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'jb9uD8ZUYhgAHsaqXLaJ9cidktcCWy-eCLyWh3rV7JAeXff0ludXbfRmcQkbQuAf7qXvJqr8zVMgDIM5rxE-bTHJP5f7Sb4EE3qOwyw9TqovdLudV95DNk-pVfXYWXxM2iKeI-lDW3bWNS2yg09p4aPb9l-BZBMAlmP_vEVm63Ikjfu7rDFrDp-LuNHKgpmHwA_UBD593pzgsoxNSznVNf980Ia9vHTkGtLd03DiVRkqxioUfnpPNtB0KufWAPpebOITSIvap3boEN9s1N21fQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851890906062'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324953149697'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'TMysB7Kdx3rZLJ2aGu87ObKTnJ6354BgzkrRXYBe0e2OYIjLk7MSOmxGji00ymu9'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5798250'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641697907, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609932344,1609933019,1609933683,1610161907'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1610161907'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1967743098705182'}, {'domain': '.qq.com', 'expiry': 1610248322, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1481080812.1609932344'}, {'domain': 'work.weixin.qq.com', 'expiry': 1610191733, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3c5h7nb'}, {'domain': '.qq.com', 'expiry': 1610161967, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641697906, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1673233922, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1568189764.1604302372'}, {'domain': '.work.weixin.qq.com', 'expiry': 1612753924, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        print(self.driver.get_cookies())
        #expiry是cookie过期字段，去掉此字段cookie会生效
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            #把字典加入driver的cookie
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        print(cookie)
        with open("cookies.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)