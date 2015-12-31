import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import PrivateNetwork, AttachServer

class TestPrivateNetwork(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_private_networks(self):
		
		with open('mock-api/list-private-networks.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/private_networks',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_private_networks()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_private_network(self):

		with open('mock-api/get-private-network.json') as f:
			data = json.load(f)

		private_network_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s' % private_network_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_private_network(private_network_id=private_network_id)

		self.assertEqual(r['id'], private_network_id)

	@responses.activate
	def test_list_servers(self):

		with open('mock-api/list-pn-servers.json') as f:
			data = json.load(f)

		private_network_id = 'PRIVATE_NETWORK_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s/servers' % private_network_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_private_network_servers(private_network_id=private_network_id)

		self.assertEqual(len(r), 2)

	@responses.activate
	def test_get_server(self):
		private_network_id = 'B944DB7D0575A828A7091CC774069A8B'
		server_id = 'AAAF4FDE974D6E5564654FF7FAB4C869'

		with open('mock-api/get-pn-server.json') as f:
			data = json.load(f)

		private_network_id = 'PRIVATE_NETWORK_ID'
		server_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s/servers/%s' % (private_network_id, server_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_private_network_server(private_network_id=private_network_id, server_id=server_id)

		self.assertEqual(r['id'], server_id)

	# 'PUT' Methods
	@responses.activate
	def test_modify_private_network(self):

		with open('mock-api/modify-pn.json') as f:
			data = json.load(f)

		private_network_id = data['id']
		name = data['name']
		description = data['description']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s' % private_network_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_private_network(private_network_id=private_network_id, name=name, description=description)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)

	# 'POST' Methods
	@responses.activate
	def test_create_private_network(self):

		with open('mock-api/create-pn.json') as f:
			data = json.load(f)

		pn1 = PrivateNetwork(name=data['name'])

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/private_networks',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_private_network(private_network=pn1)

		self.assertEqual(r['name'], pn1.name)

	@responses.activate
	def test_attach_servers(self):

		with open('mock-api/attach-server-pn.json') as f:
			data = json.load(f)

		private_network_id= 'PRIVATE_NETWORK_ID'
		server1 = AttachServer(server_id=data[2]['id'])
		servers = [server1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s/servers' % private_network_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.attach_private_network_servers(private_network_id=private_network_id, server_ids=servers)

		self.assertEqual(r[2]['id'], server1.server_id)

	# 'DELETE' Methods
	@responses.activate
	def test_remove_server_private_network(self):

		with open('mock-api/remove-server-pn.json') as f:
			data = json.load(f)

		private_network_id= data['id']
		server_id = 'SERVER_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s/servers/%s' % (private_network_id, server_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_private_network_server(private_network_id=private_network_id, server_id=server_id)

		self.assertEqual(len(r['servers']), 1)

	@responses.activate
	def test_delete_private_network(self):

		with open('mock-api/delete-pn.json') as f:
			data = json.load(f)

		private_network_id= data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/private_networks/%s' % private_network_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_private_network(private_network_id=private_network_id)

		self.assertEqual(r['state'], 'REMOVING')

if __name__ == '__main__':
	unittest.main()