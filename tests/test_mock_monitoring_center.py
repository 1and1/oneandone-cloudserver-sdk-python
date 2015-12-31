import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService

class TestImage(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	@responses.activate
	def test_list_server_usages(self):

		with open('mock-api/list-monitoring-center-usages.json') as f:
			data = json.load(f)

		server_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_center',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_server_usages()

		self.assertEqual(r[0]['id'], server_id)

	@responses.activate
	def test_get_usage(self):
		
		with open('mock-api/get-usage.json') as f:
			data = json.load(f)

		server_id = data['id']
		period = 'LAST_24H'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_center/%s' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_usage(server_id=server_id, period=period)

		self.assertEqual(r['id'], server_id)

if __name__ == '__main__':
	unittest.main()