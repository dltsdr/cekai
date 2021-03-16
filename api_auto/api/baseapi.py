import requests,json

class BaseApi:
    params = {}
    def send(self, data):
        #查看requests源码，发现传入请求方式get或者post可控制按照那种请求方式，进行请求
        raw_data = json.dumps(data)
        print(raw_data)
        for key,value in self.params.items():
           raw_data =  raw_data.replace("${"+key+"}",value)
           print(raw_data)
        data = json.loads(raw_data)
        print(data)
        return requests.request(**data).json()