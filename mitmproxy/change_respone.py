from mitmproxy import http
import json

def response(flow:http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][0]['quote']['name'] = "abcd123456"
        flow.response.text = json.dumps(data)