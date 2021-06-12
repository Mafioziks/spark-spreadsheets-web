import time
import json
import requests
import textwrap
import livysession
import spreadsheets.logger

from pprint import pprint


def listing():
    # TODO: session need to be started from one connection and shared if there will be users
    session_response = livysession.start()

    if session_response is None:
        return {'error': 'Failed to start a session'}

    if 'location' not in session_response.headers:
        return {'error': 'Session location not provided by livy', 'livy_status': session_response.status_code}

    spreadsheets.logger.log_response(session_response)
    session_path = session_response.headers['location']
    url = livysession.link + ':' + str(livysession.port) + session_path + '/state'

    while True:
        r = requests.get(url, headers=livysession.headers)
        if r.json()['state'] != 'starting':
            break
        time.sleep(1)

    url = livysession.link + ':' + str(livysession.port) + session_path + '/statements'

    data = {
        'code': textwrap.dedent("show databases"),
        'kind': 'sql'
    }

    r = requests.post(url, data=json.dumps(data), headers=livysession.headers)
    spreadsheets.logger.log_response(r)
    while r.json()['state'] != 'waiting':
        r = requests.post(url, data=json.dumps(data), headers=livysession.headers)
        spreadsheets.logger.log_response(r)
        time.sleep(1)

    url = livysession.link + ':' + str(livysession.port) + session_path + '/statements/' + str(r.json()['id'])

    r = requests.get(url, headers=livysession.headers)
    spreadsheets.logger.log_response(r)

    while r.json()['state'] == 'waiting' or r.json()['state'] == 'running':
        time.sleep(1)
        r = requests.get(url, headers=livysession.headers)
        spreadsheets.logger.log_response(r)

    return r.json()['output']['data']['application/json']['data'][0], 200

def create(data):
    pprint('Data:')
    pprint(data)
    # TODO: session need to be started from one connection and shared if there will be users
    session_response = livysession.start()

    if session_response is None:
        return {'error': 'Failed to start a session'}

    if 'location' not in session_response.headers:
        return {'error': 'Session location not provided by livy', 'livy_status': session_response.status_code}

    spreadsheets.logger.log_response(session_response)
    session_path = session_response.headers['location']
    url = livysession.link + ':' + str(livysession.port) + session_path + '/state'

    while True:
        r = requests.get(url, headers=livysession.headers)
        if r.json()['state'] != 'starting':
            break
        time.sleep(1)

    url = livysession.link + ':' + str(livysession.port) + session_path + '/statements'

    data = {
        'code': textwrap.dedent("CREATE DATABASE IF NOT EXISTS " + data['name']),
        'kind': 'sql'
    }

    r = requests.post(url, data=json.dumps(data), headers=livysession.headers)
    spreadsheets.logger.log_response(r)
    while r.json()['state'] != 'waiting':
        r = requests.post(url, data=json.dumps(data), headers=livysession.headers)
        spreadsheets.logger.log_response(r)
        time.sleep(1)

    url = livysession.link + ':' + str(livysession.port) + session_path + '/statements/' + str(
        r.json()['id'])

    r = requests.get(url, headers=livysession.headers)
    spreadsheets.logger.log_response(r)

    while r.json()['state'] == 'waiting' or r.json()['state'] == 'running':
        time.sleep(1)
        r = requests.get(url, headers=livysession.headers)
        spreadsheets.logger.log_response(r)

    return {'message': 'Database Created'}, 200
