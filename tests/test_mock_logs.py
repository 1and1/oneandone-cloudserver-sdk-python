import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService

class TestLogs(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('API-USER-KEY')

	@responses.activate
	def test_list_logs(self):
		
		with open('mock-api/list-logs.json') as f:
			data = json.load(f)

		test_id = data[0]['id']
		period = 'LAST_24H'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/logs',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_logs(period=period)

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_log(self):

		with open('mock-api/get-log.json') as f:
			data = json.load(f)

		log_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/logs/%s' % log_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_log(log_id=log_id)

		self.assertEqual(r['id'], log_id)

if __name__ == '__main__':
	unittest.main()