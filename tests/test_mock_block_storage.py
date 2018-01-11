import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import BlockStorage

class TestBlockStorage(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_block_storages(self):
		
		with open('mock-api/list-block-storages.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/block_storages',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_block_storages()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_block_storage(self):

		with open('mock-api/get-block-storage.json') as f:
			data = json.load(f)

		block_storage_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/block_storages/%s' % block_storage_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_block_storage(block_storage_id=block_storage_id)

		self.assertEqual(r['id'], block_storage_id)

	@responses.activate
	def test_get_block_storage_server(self):
		block_storage_id = '6AD2F180B7B666539EF75A02FE227084'

		with open('mock-api/get-block-storage-server.json') as f:
			data = json.load(f)

		block_storage_id = 'BLOCK_STORAGE_ID'
		server_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/block_storages/%s/server' % (block_storage_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_block_storage_server(block_storage_id=block_storage_id)

		self.assertEqual(r['id'], server_id)

	# 'PUT' Methods
	@responses.activate
	def test_modify_block_storage(self):

		with open('mock-api/modify-block-storage.json') as f:
			data = json.load(f)

		block_storage_id = data['id']
		name = data['name']
		description = data['description']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/block_storages/%s' % block_storage_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_block_storage(block_storage_id=block_storage_id, name=name, description=description)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)

	# 'POST' Methods
	@responses.activate
	def test_create_block_storage(self):

		with open('mock-api/create-block-storage.json') as f:
			data = json.load(f)

		blks1 = BlockStorage(name=data['name'],
						   description=data['description'],
						   size=data['size'],
						   datacenter_id=data['datacenter_id'])

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/block_storages',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_block_storage(blks1)

		self.assertEqual(r['name'], data['name'])

	@responses.activate
	def test_attach_server_block_storage(self):

		with open('mock-api/attach-server-block-storage.json') as f:
			data = json.load(f)

		block_storage_id= 'BLOCK_STORAGE_ID'

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/block_storages/%s/server' % block_storage_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.attach_block_storage_servers(block_storage_id=block_storage_id, server_id='638ED28205B1AFD7ADEF569C725DD85F')

		self.assertEqual(r['server']['id'], '638ED28205B1AFD7ADEF569C725DD85F')

	# 'DELETE' Methods
	@responses.activate
	def test_delete_block_storage(self):

		with open('mock-api/delete-block-storage.json') as f:
			data = json.load(f)

		block_storage_id= data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/block_storages/%s' % block_storage_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_block_storage(block_storage_id=block_storage_id)

		self.assertEqual(r['state'], 'REMOVING')

if __name__ == '__main__':
	unittest.main()