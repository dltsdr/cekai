import requests


class GetToken:
    _corpid = "wwdf8d39f6d699b1f3"
    _corpsecret = "8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg"

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self._corpid,
            "corpsecret": self._corpsecret
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        return r
