import requests
class BaseApi:


    def requests_http(self,req):

        r = requests.request(**req)
        #类似于转为字典形式,他俩本质上一致
        #r = requests.request(method="get", url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params={"corpid": self._corpid, "corpsecret": self._corpsecret})
        return r



