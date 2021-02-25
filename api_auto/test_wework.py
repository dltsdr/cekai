import re,random

import requests,pytest


def test_create_data():
    "userid, name, mobile"
    #  %08d  8个0
    data = [("kenan" + str(x),"柯南","138%08d"%x)
            for x in range(20)]
    print(data)
    return data

class TestWework:

    #fixtrue方法toke获取
    @pytest.fixture(scope="session")
    def token(self):
        requests_params = {
            "corpid":"wwdf8d39f6d699b1f3",
            "corpsecret":"8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg"}

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=requests_params)
        print(r.json())
        return r.json()["access_token"]

    # #获取token
    # def test_get_token(self):
    #     requests_params = {
    #         "corpid":"wwdf8d39f6d699b1f3",
    #         "corpsecret":"8fj9_sHJFZwqgGX6Ks6HCJ-a9P52W4g2wMizEMr6UWg"}
    #
    #     r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #                      params=requests_params)
    #     print(r.json())
    #     return r.json()["access_token"]

    #创建成员
    def test_create(self, token, userid, mobile, name="柯南", department=None):

        if department is None:
            department = [1]
        requests_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department}

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                      json=requests_body
                      )
        return r.json()

    #获取成员
    def test_get(self,token,userid):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    #更新成员
    def test_update(self,token,userid,name="柯南2",monile="13876728190"):
        requests_body = {
            "userid": userid,
            "name": name,
            "monile":monile
        }

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                      json=requests_body
                      )
        return r.json()

    #删除成员
    def test_delete(self,token,userid):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()


    #整体测试
    @pytest.mark.parametrize("userid,name,mobile",test_create_data())
    def test_wework(self,token,userid,name,mobile):
        userid="kenan123"

        try:
            assert "created" == self.test_create(token,userid,mobile)["errmsg"]
        except AssertionError as e:
            #__str__()提取报错信息
            if "mobile existed" in e.__str__():
                #re正则匹配
                re_userid = re.findall(":(.*)'$",e.__str__())[0]
                self.test_delete(token,re_userid)
                assert "created" == self.test_create(token, userid, mobile)["errmsg"]

        assert name == self.test_get(token,userid)["name"]

        assert "updated" == self.test_update(token,userid,name="柯南666")["errmsg"]
        assert "柯南666"== self.test_get(token, userid)["name"]

        assert "deleted" == self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]



