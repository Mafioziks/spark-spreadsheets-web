import requests, json


link = 'http://127.0.0.1'
port = 8998
headers = {'Content-Type': 'application/json'}


def start():
    try:
        data = {'kind': 'pyspark'}
        return requests.post(f'{link}:{port}/sessions', data=json.dumps(data), headers=headers)
    except requests.exceptions.ConnectionError:
        return None


# Create a handler for our read (GET) spark sessions
def read():
    """
    This function responds to a request for /api/session
    with the complete lists of people

    :return:        sorted list of people
    """
    response = start()
    if response is None:
        return {'error': 'Connection exception'}

    return response.json()
