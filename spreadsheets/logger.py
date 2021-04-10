import requests
from pprint import pprint


def log_request(request: requests.Request):
    print('Request:')
    if None is not request:
        pprint(request.url)
        pprint(request.headers)
        pprint(request.data)
    else:
        pprint(None)


def log_response(response: requests.Response):
    print('Response:')
    if None is not response:
        pprint(response.url)
        pprint(response.headers)
        pprint(response.status_code)
        pprint(response.text)
    else:
        pprint(None)

