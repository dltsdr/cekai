import requests

class Test_Demo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.json())
        print(r.text)
        print(r.status_code)
        assert  r.status_code == 200