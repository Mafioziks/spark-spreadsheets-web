import unittest
import requests
import TestBase
from unittest_data_provider import data_provider


class TestingFilesApi(unittest.TestCase):
    _base_uri = 'http://localhost:5000/api/'

    filesDataProvider = lambda: (
        ({}, {'status_code': 200}),
    )

    @data_provider(filesDataProvider)
    def test_get_files(self, filters, expected):
        response = requests.get(self._base_uri + 'spreadsheet/files')
        json_response = response.json()
        self.assertEqual((expected['status_code'], 200)[expected['status_code'] is None], response.status_code)

        if 200 != response.status_code:
            self.assertIsNone(json_response.error)
            return

        self.assertTrue(isinstance(json_response, list), json_response)

    def test_get_file(self, id, expected):
        pass

    def test_get_spreadsheet(self, id, expected):
        pass