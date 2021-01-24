import requests, json

# Create a handler for our read (GET) spark sessions
def read():
    """
    This function responds to a request for /api/session
    with the complete lists of people

    :return:        sorted list of people
    """
    try:
        link = 'http://127.0.0.1'
        port = 8998
        data = {'kind': 'pyspark'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{link}:{port}/sessions', data=json.dumps(data), headers=headers)
    except requests.exceptions.ConnectionError:
        return {'Exception': 'Connection exception'}

    return response.json()
