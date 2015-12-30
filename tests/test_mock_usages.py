import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService

class TestUsages(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	@responses.activate
	def test_list_usages(self):

		with open('mock-api/list-usages.json') as f:
			data = json.load(f)

		server_id = data['SERVERS'][0]['id']
		period = "LAST_24H"

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/usages',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_usages(period=period)

		self.assertEqual(r['SERVERS'][0]['id'], server_id)


if __name__ == '__main__':
	unittest.main()