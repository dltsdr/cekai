import yaml
from api_auto.api.util import Util
from api_auto.api.baseapi import BaseApi

class WeWork(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token


    #创建成员
    def test_create(self, userid, mobile, name="柯南", department=None):

        if department is None:
            department = "1"

        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department}
        # }
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        with open("../api/wework.yaml",encoding="utf-8") as f:
            data = yaml.load(f)
        return self.send(data["create"])

    #获取成员
    def test_get(self,userid):

        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"}

        return self.send(data)

    #更新成员
    def test_update(self,userid,name="柯南2"):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "json": {
                "userid": userid,
                "name": name}
            }
        return self.send(data)

    #删除成员
    def test_delete(self,userid):

        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        }

        return self.send(data)


    #整体测试

    def test_wework(self,token,userid,name,mobile):

        try:
            assert "created" == self.test_create(token,userid,mobile,name)["errmsg"]
        except AssertionError as e:
            #__str__()提取报错信息
            if "mobile existed" in e.__str__():
                #re正则匹配
                re_userid = re.findall(":(.*)'",e.__str__())[0]
                self.test_delete(token,re_userid)
                assert "created" == self.test_create(token, userid, mobile,name)["errmsg"]

        assert name == self.test_get(token,userid)["name"]

        assert "updated" == self.test_update(token,userid,name="柯南666")["errmsg"]
        assert "柯南666"== self.test_get(token, userid)["name"]

        assert "deleted" == self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]



