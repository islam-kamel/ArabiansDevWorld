import json

import urllib3

http = urllib3.PoolManager()


def send_request(url, method="GET") -> json:
    response = http.request(method, url)
    json_response = json.loads(response.data)
    print(json_response)
    return json_response
