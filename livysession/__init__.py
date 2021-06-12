import requests, json
from flask import request
from pprint import pprint


link = 'http://127.0.0.1'
port = 8998
headers = {'Content-Type': 'application/json'}
__response__ = None


def start():
    try:
        data = {'kind': 'pyspark'}
        __response__ = requests.post(f'{link}:{port}/sessions', data=json.dumps(data), headers=headers)
        return __response__
    except requests.exceptions.ConnectionError:
        return None


def get_session_id():
    start()
    if __response__ is None:
        return {'error': 'Failed to start a session'}

    if 'location' not in __response__.headers:
        return {'error': 'Session location not provided by livy', 'livy_status': __response__.status_code}

    spreadsheets.logger.log_response(session_response)
    location = __response__.headers['location'].split('/')
    session_id = location[len(location) - 1]
    url = session.link + ':' + str(session.port) + __response__.headers['location'] + '/state'

    while True:
        r = requests.get(url, headers=headers)
        if r.json()['state'] != 'starting':
            break
        time.sleep(1)

    return session_id


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


def end(id):
    try:
        pprint(f'{link}:{port}/sessions/' + str(id))
        __response__ = requests.delete(f'{link}:{port}/sessions/' + str(id), headers=headers)
        pprint(__response__)
        return {}
    except requests.exceptions.ConnectionError:
        return {}, 500