import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import SshKey

class TestPrivateNetwork(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_ssh_keys(self):
		
		with open('mock-api/list-ssh-keys.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/ssh_keys',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_ssh_keys()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_ssh_key(self):

		with open('mock-api/get-ssh-key.json') as f:
			data = json.load(f)

		ssh_key_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/ssh_keys/%s' % ssh_key_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_ssh_key(ssh_key_id=ssh_key_id)

		self.assertEqual(r['id'], ssh_key_id)

	# 'PUT' Methods
	@responses.activate
	def test_modify_ssh_key(self):

		with open('mock-api/modify-ssh-key.json') as f:
			data = json.load(f)

		ssh_key_id = data['id']
		name = data['name']
		description = data['description']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/ssh_keys/%s' % ssh_key_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_ssh_key(ssh_key_id=ssh_key_id, name=name, description=description)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)

	# 'POST' Methods
	@responses.activate
	def test_create_ssh_key(self):

		with open('mock-api/create-ssh-key.json') as f:
			data = json.load(f)

		ssh1 = SshKey(name=data['name'], description=data['description'], public_key=data['public_key'])

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/ssh_keys',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_ssh_key(ssh_key=ssh1)

		self.assertEqual(r['name'], ssh1.name)

	@responses.activate
	def test_delete_ssh_key(self):

		with open('mock-api/delete-ssh-key.json') as f:
			data = json.load(f)

		ssh_key_id= data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s' % ssh_key_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_private_network(ssh_key_id=ssh_key_id)

		self.assertEqual(r['state'], 'DELETING')

if __name__ == '__main__':
	unittest.main()