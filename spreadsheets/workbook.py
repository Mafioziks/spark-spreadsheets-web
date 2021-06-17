from flask import session, request
from pprint import pprint
from livy.api import API
from livy.parser import get_sql_tables


def get_sheets(file):
    """Get spreadsheets contained in workbook"""
    api = API()

    livy_session = session.get('livy')
    if livy_session is None:
        livy_session = api.create_session_ready()

    # TODO: Check if session still exists
    statement = api.send_sql_statement(livy_session['session_id'], f'show tables from {file}')
    if statement['result']['state'] == 'waiting':
        statement = api.wait_statement_finish(statement['session_id'], statement['statement_id'])

    pprint(statement)

    if statement['result']['output'] is None:
        return []

    sheets = []
    for sheet in statement['result']['output']['data']['application/json']['data']:
        sheets.append(sheet[0])

    return get_sql_tables(statement['result'])


def create_sheet():
    """Create new sheet in workbook"""
    api = API()

    livy_session = session.get('livy')
    if livy_session is None:
        livy_session = api.create_session_ready()

    file = request.json['file']
    sheet = request.json['sheet']

    # TODO: Check if session still exists
    query = f'create table {file}.{sheet} (id INT, name VARCHAR(100), date VARCHAR(20)) USING CSV OPTIONS(header=\'true\', nullvalue=\'NA\', timestampFormat=\'yyyy-MM-dd HH:mm:ss\')'
    statement = api.send_sql_statement(livy_session['session_id'], query)
    if statement['result']['state'] == 'waiting':
        statement = api.wait_statement_finish(statement['session_id'], statement['statement_id'])

    pprint(statement)

    if statement['result']['output'] is None:
        return []

    sheets = []
    for sheet in statement['result']['output']['data']['application/json']['data']:
        sheets.append(sheet[0])

    return get_sql_tables(statement['result'])
