import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import SharedStorage, AttachServer

class TestSharedStorage(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('<USER-API-KEY>')

	# 'GET' Methods
	@responses.activate
	def test_list_shared_storages(self):
		
		with open('mock-api/list-storages.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/shared_storages',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_shared_storages()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_shared_storage(self):

		with open('mock-api/get-storage.json') as f:
			data = json.load(f)

		shared_storage_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s' % shared_storage_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_shared_storage(shared_storage_id=shared_storage_id)

		self.assertEqual(r['id'], shared_storage_id)

	@responses.activate
	def test_servers_attached(self):
		
		with open('mock-api/storage-servers.json') as f:
			data = json.load(f)

		shared_storage_id = data[0]['id']
		server_name = data[0]['name']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s/servers' % shared_storage_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_servers_attached_storage(shared_storage_id=shared_storage_id)

		self.assertEqual(r[0]['name'], server_name)

	@responses.activate
	def test_get_server(self):
		
		with open('mock-api/get-server-storage.json') as f:
			data = json.load(f)

		shared_storage_id = 'SHARED_STORAGE_ID'
		server_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s/servers/%s' % (shared_storage_id, server_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_shared_storage_server(shared_storage_id=shared_storage_id, server_id=server_id)

		self.assertEqual(r['id'], server_id)

	@responses.activate
	def test_get_credentials(self):
		
		with open('mock-api/list-credentials.json') as f:
			data = json.load(f)

		kerberos_content_file = data['kerberos_content_file']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/shared_storages/access',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_credentials()

		self.assertEqual(r['kerberos_content_file'], kerberos_content_file)

	# 'POST' Methods
	@responses.activate
	def test_create_shared_storage(self):
		
		with open('mock-api/create-storage.json') as f:
			data = json.load(f)

		storage1 = SharedStorage(name=data['name'], description=data['description'], size=data['size'])

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/shared_storages',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_shared_storage(shared_storage=storage1)

		self.assertEqual(r['name'], storage1.name)
		self.assertEqual(r['description'], storage1.description)
		self.assertEqual(r['size'], storage1.size)

	@responses.activate
	def test_attach_servers(self):

		with open('mock-api/attach-server-storage.json') as f:
			data = json.load(f)

		shared_storage_id = data['id']
		server1 = AttachServer(server_id=data['servers'][0]['id'], rights=data['servers'][0]['rights'])
		server2 = AttachServer(server_id=data['servers'][1]['id'], rights=data['servers'][1]['rights'])
		servers = [server1, server2]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s/servers' % shared_storage_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.attach_server_shared_storage(shared_storage_id=shared_storage_id, server_ids=servers)

		self.assertEqual(r['servers'][0]['id'], server1.server_id)
		self.assertEqual(r['servers'][1]['id'], server2.server_id)

	# 'PUT' Methods
	@responses.activate
	def test_modify_shared_storage(self):
		
		with open('mock-api/modify-storage.json') as f:
			data = json.load(f)

		shared_storage_id = data['id']
		name = data['name']
		description = data['description']
		size = data['size']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s' % shared_storage_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_shared_storage(shared_storage_id=shared_storage_id, name=name, description=description, size=size)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)
		self.assertEqual(r['size'], size)

	@responses.activate
	def test_change_password(self):
		
		with open('mock-api/change-password.json') as f:
			data = json.load(f)

		new_password = 'NEW_PASSWORD'

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/shared_storages/access',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.change_password(password=new_password)

		self.assertEqual(r['state'], 'CONFIGURING')

	# 'DELETE' Methods
	@responses.activate
	def test_delete_shared_storage(self):

		with open('mock-api/delete-storage.json') as f:
			data = json.load(f)

		shared_storage_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s' % shared_storage_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_shared_storage(shared_storage_id=shared_storage_id)		

		self.assertEqual(r['state'], 'REMOVING')

	@responses.activate
	def test_detach_server_ss(self):
		
		with open('mock-api/detach-server-storage.json') as f:
			data = json.load(f)

		shared_storage_id = data['id']
		server_id = 'SERVER_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/shared_storages/%s/servers/%s' % (shared_storage_id, server_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.detach_server_shared_storage(shared_storage_id=shared_storage_id, server_id=server_id)

		self.assertNotEqual(r['servers'][0]['id'], server_id)

if __name__ == '__main__':
	unittest.main()