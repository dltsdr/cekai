import  requests
from requests.auth import HTTPBasicAuth

#cookies请求
def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {"Cookies":"hogwarts=school"}
    cookie_data = {"hogwarts":"school"}
    r = requests.get(url=url,headers = header,cookies = cookie_data)
    print(r.request.headers)

#auth请求
def test_auth():
    r = requests.get(url="https://httpbin.testing-studio.com/banaba/123",
                     auth = HTTPBasicAuth("banana","123"))
    print(r.text)