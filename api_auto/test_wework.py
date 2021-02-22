import requests

class TestWework:
    #获取token
    def test_get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwdf8d39f6d699b1f3&corpsecret=8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg")
        print(r.text)