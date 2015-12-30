import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService

class TestDVD(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	@responses.activate
	def test_list_dvds(self):

		with open('mock-api/list-dvds.json') as f:
			data = json.load(f)

		iso_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/dvd_isos',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_dvds()

		self.assertEqual(r[0]['id'], iso_id)

	@responses.activate
	def test_get_dvd(self):

		with open('mock-api/get-dvd.json') as f:
			data = json.load(f)

		iso_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/dvd_isos/%s' % iso_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_dvd(iso_id=iso_id)

		self.assertEqual(r['id'], iso_id)

if __name__ == '__main__':
	unittest.main()