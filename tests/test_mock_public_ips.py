import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService

class TestPublicIP(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_public_ips(self):
		
		with open('mock-api/list-public-ips.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/public_ips',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_public_ips()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_public_ip(self):
		ip_id = '9DB3E4FFEAA6BD8C7007B821C0E868D6'

		with open('mock-api/get-public-ip.json') as f:
			data = json.load(f)

		ip_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/public_ips/%s' % ip_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_public_ip(ip_id=ip_id)

		self.assertEqual(r['id'], ip_id)

	# 'POST' Methods
	@responses.activate
	def test_create_public_ip(self):

		with open('mock-api/create-public-ip.json') as f:
			data = json.load(f)

		ip_id = data['id']
		reverse_dns = data['reverse_dns']

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/public_ips',
					  body=json.dumps(data), status=201,
					  content_type="application/json")

		r = self.client.create_public_ip(reverse_dns=reverse_dns)

		self.assertEqual(r['id'], ip_id)
		self.assertEqual(r['reverse_dns'], reverse_dns)

	# 'PUT' Methods
	@responses.activate
	def test_modify_public_ip(self):

		with open('mock-api/modify-public-ip.json') as f:
			data = json.load(f)

		ip_id = data['id']
		reverse_dns = data['reverse_dns']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/public_ips/%s' % ip_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_public_ip(ip_id=ip_id, reverse_dns=reverse_dns)

		self.assertEqual(r['reverse_dns'], reverse_dns)

	# 'DELETE' Methods
	@responses.activate
	def test_delete_public_ip(self):

		with open('mock-api/delete-public-ip.json') as f:
			data = json.load(f)

		ip_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/public_ips/%s' % ip_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.delete_public_ip(ip_id=ip_id)

		self.assertEqual(r['state'], 'CONFIGURING')

if __name__ == '__main__':
	unittest.main()
