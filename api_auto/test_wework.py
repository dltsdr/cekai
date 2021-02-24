import requests

class TestWework:
    #获取token
    def test_get_token(self):
        requests_params = {
            "corpid":"wwdf8d39f6d699b1f3",
            "corpsecret":"8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg"}

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=requests_params)
        print(r.json())
        return r.json()["access_token"]

    #创建成员
    def test_create(self):
        access_token = self.test_get_token()
        requests_body = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13800000000",
            "department": [1]}

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}",
                      json=requests_body
                      )
        print(r.json())

    #获取成员
    def test_get(self):
        access_token = self.test_get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid=DouXinPeng")
        print(r.json())


    #更新成员
    def test_update(self):
        access_token = self.get_token()
        requests_body = {
            "userid": "DuanZhiYu",
            "position": "TESTER"}

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}",
                      json=requests_body
                      )
        print(r.json())