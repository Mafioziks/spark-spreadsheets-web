import textwrap
import requests
from pprint import pprint
import json
import time


class API:
    """API class responsible for communication with Livy

    Class has methods for managing different tasks related with livy excluding storing data in itself.
    """
    # TODO: Need to implement configuration getting from configuration file or environment variables
    _link = 'http://127.0.0.1'
    _port = 8998
    _headers = {'Content-Type': 'application/json'}

    def create_session(self):
        try:
            data = {'kind': 'pyspark'}
            response = requests.post(
                f'{self._link}:{self._port}/sessions',
                data=json.dumps(data),
                headers=self._headers
            )
            return response
        except requests.exceptions.ConnectionError:
            return None

    def create_session_ready(self):
        response = self.create_session()

        if response is None:
            pprint('Session not created')
            return None

        if 'location' not in response.headers:
            pprint('Location not provided in session - no session created. Status code: ' + str(response.status_code))
            return None

        location = response.headers['location'].split('/')
        session_id = location[len(location) - 1]

        while True:
            state_response = requests.get(
                f'{self._link}:{self._port}/sessions/{session_id}/state',
                headers=self._headers
            )

            if state_response.json()['state'] != 'starting':
                break
            time.sleep(1)

        if state_response.json()['state'] not in ('idle', 'busy'):
            pprint('Session is started but not good state returned:')
            pprint(state_response.json()['state'])
            return None

        return {
            'session_id': session_id,
            'state': state_response.json()['state']
        }

    def session_end(self, session_id: int):
        """Finish Livy session"""
        try:
            response = requests.delete(f'{self._link}:{self._port}/sessions/' + str(session_id), headers=self._headers)
            return {'session_id': session_id, 'result': response.json()}
        except requests.exceptions.ConnectionError:
            return {'session_id': session_id, 'result': None}

    def send_sql_statement(self, session_id, statement):
        url = f'{self._link}:{self._port}/sessions/{session_id}/statements'
        data = {
            'code': textwrap.dedent(statement),
            'kind': 'sql'
        }

        statement_response = requests.post(url, data=json.dumps(data), headers=self._headers)
        response_data = statement_response.json()
        pprint(response_data)
        if 'id' not in response_data or response_data['id'] is None:
            return {
                'session_id': session_id,
                'result': response_data
            }

        return {
            'session_id': session_id,
            'statement_id': int(statement_response.json()['id']),
            'result': statement_response.json()
        }

    def wait_statement_finish(self, session_id: int, statement_id: int):
        """Wait till statement finishes and get result of finished statement

        :param session_id:
        :param statement_id:
        :return:
        """
        status_response = self.get_statement_current_status(session_id, statement_id)
        while status_response.json()['state'] in ('waiting', 'running'):
            time.sleep(1)
            status_response = self.get_statement_current_status(session_id, statement_id)

        return {
            'session_id': session_id,
            'statement_id': statement_id,
            'result': status_response.json()
        }

    def get_statement_current_status(self, session_id: int, statement_id: int):
        """Get statement information at current moment

        :param session_id:
        :param statement_id:
        :return:
        """
        url = f'{self._link}:{self._port}/sessions/{session_id}/statements/{statement_id}'
        return requests.get(url, headers=self._headers)
