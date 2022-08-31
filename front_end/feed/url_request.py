import json

import requests

methods = {"POST": requests.post, "PUT": requests.put, "DELETE": requests.delete}


def submit_request(url, data=None, token=None, method="PUT") -> json:
    if data is None and method == "GET":
        response = requests.get(url)
        return response
    try:
        sender = methods[method]
        response = sender(
            url=url, headers={"Authorization": f"Bearer {token}"}, json=data
        )
        return response
    except KeyError:
        pass
