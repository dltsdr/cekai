from api_auto.api.wework import WeWork
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
