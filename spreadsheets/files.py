from livy.api import API
from flask import session
from pprint import pprint


def list_files():
    # TODO: session need to be started from one connection and shared if there will be users
    api = API()

    livy_session = session.get('livy')
    if livy_session is None:
        livy_session = api.create_session_ready()
        session['livy'] = livy_session

    if livy_session is None or livy_session['state'] in ('dead', 'killed'):
        return []

    list_databases = api.send_sql_statement(livy_session['session_id'], 'show databases')
    if 'statement_id' not in list_databases:
        # TODO: Check if Livy session valid...?
        api.session_end(list_databases['session_id'])
        session.pop('livy')
        return []

    if list_databases['result']['state'] == 'waiting':
        pprint(list_databases)
        list_databases = api.wait_statement_finish(list_databases['session_id'], list_databases['statement_id'])

    pprint(list_databases)
    # api.session_end(list_databases['session_id'])
    if list_databases['result']['output'] is None:
        return []

    databases = []
    for database in list_databases['result']['output']['data']['application/json']['data']:
        databases.append(database[0])

    return databases, 200


def create(data):
    api = API()

    livy_session = session.get('livy')
    if None is livy_session:
        livy_session = api.create_session_ready()

    if livy_session['state'] in ('dead', 'killed'):
        return {}

    # TODO: Safe data handling in query
    livy_statement = api.send_sql_statement(livy_session['session_id'], f'CREATE DATABASE IF NOT EXISTS {data["name"]}')
    if livy_statement['result']['state'] == 'waiting':
        livy_statement = api.wait_statement_finish(livy_statement['session_id'], livy_statement['statement_id'])

    if livy_statement['result']['output'] is None:
        return {}

    pprint(livy_statement)
    return {'message': 'Database Created'}, 200
