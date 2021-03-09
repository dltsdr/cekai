from api_auto.api.wework import WeWork
from api_auto.api.util import Util
import requests


class TestWork:
    #获取成员
    def test_get(self):
        print(WeWork().test_get("DuanZhiYu"))

    #创建成员
    def test_create(self):
        print(WeWork().test_create("kenan888","18972654678"))

    #更新成员
    def test_update(self):
        print(WeWork().test_update("kenan888"))

    #删除成员
    def test_delete(self):
        print(WeWork().test_delete("kenan888"))

    def test_session(self):
        s = requests.session()

    #生成一次token，可作用于所有用例，下面举例是get取得用户信息
    def test_session(self):
        s = requests.session()
        s.params = {"access_token":Util().get_token()}
        res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=DuanZhiYu")
        print(res.json())
