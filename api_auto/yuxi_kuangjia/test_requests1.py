import requests
import base64,json

def test_encode():
    url = "http://127.0.0.1:9999/demo1.txt"
    r = requests.get(url=url)
    res = json.loads(base64.b64decode(r.content))
    print(res)