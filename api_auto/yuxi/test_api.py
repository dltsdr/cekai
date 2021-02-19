import requests
from jsonpath import jsonpath
from hamcrest import *

class Test_Demo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.json())
        print(r.text)
        print(r.status_code)
        assert  r.status_code == 200

    #get query请求
    def test_query(self):
        payload={
            "level" : 1,
            "name" : "seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert  r.status_code == 200


    #post from请求
    def test_post_from(self):
        payload={
            "level" : 1,
            "name" : "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert  r.status_code == 200


    #header请求,断言
    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h":"header demo"})
        print(r.text)
        assert  r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"

    #post json请求
    def test_hogwarts_json(self):
        r = requests.post('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name']=='开源项目'
        print(jsonpath(r.json(),'$..name'))
        assert jsonpath(r.json(),'$..name')[0] == '开源项目'


    #使用hamcrest断言
    def test_hamcrest(self):
        r = requests.post('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('开源项目'))