from base_api import BaseApi
import yaml
from string import Template

class GetToken(BaseApi):
    _corpid = "wwdf8d39f6d699b1f3"
    _corpsecret = "8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg"

    def template(self):
        with open("../api/get_token.yaml") as f:
            data = {
                "corpid":self._corpid,
                "corpsecret":self._corpsecret
            }
            #模板替换
            re = Template(f.read()).substitute(data)
            return yaml.safe_load(re)


    def get_token(self):
        #把请求信息转化为一个规范的字典结构体

        req = self.template()
        r = self.requests_http(req)
        print(r.json())
        return r
