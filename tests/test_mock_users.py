import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService

class TestUser(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_users(self):
		
		with open('mock-api/list-users.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/users',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_users()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_user(self):

		with open('mock-api/get-user.json') as f:
			data = json.load(f)

		user_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/users/%s' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_user(user_id=user_id)

		self.assertEqual(r['id'], user_id)

	@responses.activate
	def test_api_info(self):

		with open('mock-api/get-user-api.json') as f:
			data = json.load(f)

		user_id = 'USER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/users/%s/api' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.api_info(user_id=user_id)

		self.assertEqual(r['active'], True)

	@responses.activate
	def test_show_api_key(self):

		with open('mock-api/get-user-api-key.json') as f:
			data = json.load(f)

		user_id = 'USER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/users/%s/api/key' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.show_api_key(user_id=user_id)

		self.assertEqual(r['key'], data['key'])

	@responses.activate
	def test_ips_api_access_allowed(self):

		with open('mock-api/list-user-ips.json') as f:
			data = json.load(f)

		user_id = 'USER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/users/%s/api/ips' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.ips_api_access_allowed(user_id=user_id)

		self.assertEqual(len(r), 3)

	# 'POST' Methods
	@responses.activate
	def test_create_user(self):

		with open('mock-api/create-user.json') as f:
			data = json.load(f)

		name = data['name']
		password = 'examplepassword'
		description = data['description']
		email = data['email']

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/users',
					  body=json.dumps(data), status=201,
					  content_type="application/json")

		r = self.client.create_user(name=name, password=password, description=description, email=email)

		self.assertEqual(r['state'], 'CREATING')
		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)
		self.assertEqual(r['email'], email)

	@responses.activate
	def test_add_user_ip(self):

		with open('mock-api/add-new-ip.json') as f:
			data = json.load(f)

		user_id = data['id']
		ip1 = data['api']['allowed_ips'][2]
		ip2 = data['api']['allowed_ips'][3]
		ips = [ip1, ip2]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/users/%s/api/ips' % user_id,
					  body=json.dumps(data), status=201,
					  content_type="application/json")

		r = self.client.add_user_ip(user_id=user_id, user_ips=ips)

		self.assertEqual(r['api']['allowed_ips'][2], ip1)
		self.assertEqual(r['api']['allowed_ips'][3], ip2)

	# 'PUT' Methods
	@responses.activate
	def test_modify_user(self):

		with open('mock-api/modify-user.json') as f:
			data = json.load(f)

		user_id = data['id']
		description = data['description']
		email = data['email']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/users/%s' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_user(user_id=user_id, description=description, email=email)

		self.assertEqual(r['description'], description)
		self.assertEqual(r['email'], email)

	@responses.activate
	def test_modify_user_api(self):

		with open('mock-api/modify-user-api.json') as f:
			data = json.load(f)

		user_id = data['id']
		active = data['api']['active']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/users/%s/api' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_user_api(user_id=user_id, active=active)

		self.assertEqual(r['api']['active'], active)

	@responses.activate
	def test_change_api_key(self):

		with open('mock-api/change-api-key.json') as f:
			data = json.load(f)

		user_id = data['id']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/users/%s/api/key' % user_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.change_api_key(user_id=user_id)

		self.assertEqual(r['state'], 'CONFIGURING')

	# 'DELETE' Methods
	@responses.activate
	def test_delete_user(self):

		with open('mock-api/delete-user.json') as f:
			data = json.load(f)

		user_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/users/%s' % user_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_user(user_id=user_id)

		self.assertEqual(r['state'], 'REMOVING')

	@responses.activate
	def test_remove_user_ip(self):

		with open('mock-api/delete-ip.json') as f:
			data = json.load(f)

		user_id = data['id']
		ip = 'IP_ADDRESS'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/users/%s/api/ips/%s' % (user_id, ip),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_user_ip(user_id=user_id, ip=ip)

		self.assertEqual(r['api']['allowed_ips'], [])

if __name__ == '__main__':
	unittest.main()