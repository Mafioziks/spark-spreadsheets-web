import requests, textwrap, json
import session
from pprint import pprint
import time

import spreadsheets.logger


def listing():
    # TODO: session need to be started from one connection and shared if there will be users
    session_response = session.start()

    if session_response is None:
        return {'error': 'Failed to start a session'}

    if 'location' not in session_response.headers:
        return {'error': 'Session location not provided by livy', 'livy_status': session_response.status_code}

    spreadsheets.logger.log_response(session_response)
    url = session.link + ':' + str(session.port) + session_response.headers['location'] + '/state'

    while True:
        r = requests.get(url, headers=session.headers)
        if r.json()['state'] != 'starting':
            break
        time.sleep(1)

    url = session.link + ':' + str(session.port) + session_response.headers['location'] + '/statements'

    data = {
        'code': textwrap.dedent("show databases"),
        'kind': 'sql'
    }

    r = requests.post(url, data=json.dumps(data), headers=session.headers)
    spreadsheets.logger.log_response(r)
    while r.json()['state'] != 'waiting':
        r = requests.post(url, data=json.dumps(data), headers=session.headers)
        spreadsheets.logger.log_response(r)
        time.sleep(1)

    url = session.link + ':' + str(session.port) + session_response.headers['location'] + '/statements/' + str(r.json()['id'])

    r = requests.get(url, headers=session.headers)
    spreadsheets.logger.log_response(r)

    while r.json()['state'] == 'waiting' or r.json()['state'] == 'running':
        time.sleep(1)
        r = requests.get(url, headers=session.headers)
        spreadsheets.logger.log_response(r)

    return r.json()['output']['data']['application/json']['data'][0]
