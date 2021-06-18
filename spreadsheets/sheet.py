from pprint import pprint
from flask import session
from livy.api import API
from livy.parser import get_output_data_fields


def view(file, sheet):
    api = API()

    livy_session = session.get('livy')
    if None is livy_session:
        livy_session = api.create_session_ready()

    if livy_session['state'] in ('dead', 'killed'):
        return {}

    # TODO: Safe data handling in query
    statement = api.send_sql_statement(livy_session['session_id'], f'SELECT * FROM {file}.{sheet}')
    if statement['result']['state'] == 'waiting':
        statement = api.wait_statement_finish(statement['session_id'], statement['statement_id'])

    if statement['result']['output'] is None:
        return {}

    pprint(statement)
    return {'message': 'Database Created'}, 200


def add():
    return {}


def update():
    return {}


def get_data():
    return {}


def update_data():
    return {}
