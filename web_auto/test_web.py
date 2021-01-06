from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Test():
    def setup_method(self,method):
        options = Options()
        #和浏览器打开的调试端口进行调试
        options.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    # def teardown_method(self,method):
    #     sleep(5)
    #     self.driver.quit()

    def test_(self):
        # dr = self.driver
        #dr.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.ID, "menu_index").click()

    def test_wework(self):
        self.driver.get("https://work.weixin.qq.com/")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851890906062'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851890906062'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324953149697'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'TMysB7Kdx3rZLJ2aGu87OTsZ7j6Lifdua0FjUjbKYnvUjA2Ira1KHEYXONVtpQd6'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1782055'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'mdm_8VuoKfXP7Zrb4_5PidqP7TDCH3ogaTUvwgvK0ImkhHtpDtz2a2HMREfvepD8aeyDAwM4v3QDLtl8u4mGHfRL2k9g0B7mJjGfeSCn7ebOpITaesnX8kWsQnRo14X3oUAEShL5THOaMG38oykYaClh-EkX4cKRrGeyR-IZmUMhzsa1G9yLeZmVaDZ0JW8Ze77jaFGl4IrbFI2qBl4ihEfb_Wgxc8DXCDogqoJYo5jAhEd3_d7kPQAUg8j7bhnGQSG4A76LR0r509ohH_JSTQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609935648'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '319385823288795'}, {'domain': 'work.weixin.qq.com', 'expiry': 1609963870, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1q52ig0'}, {'domain': '.qq.com', 'expiry': 1610021923, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1481080812.1609932344'}, {'domain': '.qq.com', 'expiry': 1924082746, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_8623295166533'}, {'domain': '.qq.com', 'expiry': 1637201575, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'R1C6Q0y5v6l6j585X765s8k8O5'}, {'domain': '.work.weixin.qq.com', 'expiry': 1612527648, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641471648, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609932344,1609933019,1609933683'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8193769266'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '7133389824'}, {'domain': '.qq.com', 'expiry': 2147483515, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '8acfe18b21b478402a9617177b88a778616caf2469ecd7eb79d672bbc8014ec3'}, {'domain': '.qq.com', 'expiry': 2147483569, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'kB7QKdzGND'}, {'domain': '.qq.com', 'expiry': 1673007523, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1568189764.1604302372'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635838370, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}]
        print(self.driver.get_cookies())
        #expiry是cookie过期字段，去掉此字段cookie会生效
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")

            #把字典加入driver的cookie
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")