from unittest import TestCase
from api_auto.yuxi_kuangjia.env_test import env_demo


class TestApi(TestCase):

    data = {
        "method":"get",
        "url":"http://testing-studio:9999/demo1.txt",
        "headers":None
    }

    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)