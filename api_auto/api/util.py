import requests
class Util:

    #获取token
    def get_token(self):
        requests_params = {
            "corpid":"wwdf8d39f6d699b1f3",
            "corpsecret":"8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg"}

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=requests_params)
        print(r.json())
        return r.json()["access_token"]