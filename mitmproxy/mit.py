from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    #对请求过滤
    if "quote.json" in flow.request.pretty_url:
        with open("test.json",encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
        )