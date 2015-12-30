import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import FirewallPolicy
from oneandone.client import FirewallPolicyRule
from oneandone.client import AttachServer

class TestFirewallPolicy(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_policies(self):
		
		with open('mock-api/list-firewalls.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/firewall_policies',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_firewall_policies()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_policy(self):

		with open('mock-api/get-firewall.json') as f:
			data = json.load(f)

		firewall_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s' % firewall_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_firewall(firewall_id=firewall_id)

		self.assertEqual(r['id'], firewall_id)

	@responses.activate
	def test_list_firewall_servers(self):
		
		with open('mock-api/list-server-ips-fp.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'
		server_ip_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/server_ips' % firewall_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_firewall_servers(firewall_id=firewall_id)

		self.assertEqual(r[0]['id'], server_ip_id)

	@responses.activate
	def test_get_firewall_server(self):

		with open('mock-api/get-server-ip-fp.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'
		server_ip_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/server_ips/%s' % (firewall_id, server_ip_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_firewall_server(firewall_id=firewall_id, server_ip_id=server_ip_id)

		self.assertEqual(r['id'], server_ip_id)

	@responses.activate
	def test_list_policy_rules(self):

		with open('mock-api/list-fp-rules.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'
		rule_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/rules' % firewall_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_firewall_policy_rules(firewall_id=firewall_id)

		self.assertEqual(r[0]['id'], rule_id)

	@responses.activate
	def test_get_policy_rule(self):

		with open('mock-api/get-fp-rule.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'
		rule_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/rules/%s' % (firewall_id, rule_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_firewall_policy_rule(firewall_id=firewall_id, rule_id=rule_id)

		self.assertEqual(r['id'], rule_id)

	# 'PUT' Methods
	@responses.activate
	def test_modify_firewall(self):
		
		with open('mock-api/modify-fp.json') as f:
			data = json.load(f)

		firewall_id = data['id']
		name = data['name']
		description = data['description']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s' % firewall_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_firewall(firewall_id=firewall_id, description=description)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)

	# 'POST' Methods
	@responses.activate
	def test_create_firewall_policy(self):
		
		with open('mock-api/create-fp.json') as f:
			data = json.load(f)

		fp1 = FirewallPolicy(name=data['name'], description=data['description'])
		rule1 = FirewallPolicyRule(protocol=data['rules'][0]['protocol'], port_from=data['rules'][0]['port_from'], port_to=data['rules'][0]['port_to'],
								   source=data['rules'][0]['source'])
		rule2 = FirewallPolicyRule(protocol=data['rules'][1]['protocol'], port_from=data['rules'][1]['port_from'], port_to=data['rules'][1]['port_to'],
								   source=data['rules'][1]['source'])
		rules = [rule1, rule2]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/firewall_policies',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_firewall_policy(firewall_policy=fp1, firewall_policy_rules=rules)

		self.assertEqual(r['name'], fp1.specs['name'])
		self.assertEqual(r['description'], fp1.specs['description'])
		self.assertEqual(r['rules'][0]['protocol'], rule1.rule_set['protocol'])
		self.assertEqual(r['rules'][1]['protocol'], rule2.rule_set['protocol'])

	@responses.activate
	def test_assign_servers(self):

		with open('mock-api/assign-ip-fp.json') as f:
			data = json.load(f)

		firewall_id = data['id']
		server1 = AttachServer(server_ip_id=data['server_ips'][0]['id'])
		servers = [server1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/server_ips' % firewall_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.attach_server_firewall_policy(firewall_id=firewall_id, server_ips=servers)

		self.assertEqual(r['id'], firewall_id)
		self.assertEqual(r['server_ips'][0]['id'], server1.server_ip_id)

	@responses.activate
	def test_add_rule(self):

		with open('mock-api/add-rule-fp.json') as f:
			data = json.load(f)

		firewall_id = data['id']
		rule1 = FirewallPolicyRule(protocol=data['rules'][2]['protocol'], port_from=data['rules'][2]['port_from'], port_to=data['rules'][2]['port_to'],
								   source=data['rules'][2]['source'])
		rules = [rule1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/rules' % firewall_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_firewall_policy_rule(firewall_id=firewall_id, firewall_policy_rules=rules)

		self.assertEqual(r['rules'][2]['protocol'], rule1.rule_set['protocol'])
		self.assertEqual(r['rules'][2]['port_from'], rule1.rule_set['port_from'])
		self.assertEqual(r['rules'][2]['port_to'], rule1.rule_set['port_to'])
		self.assertEqual(r['rules'][2]['source'], rule1.rule_set['source'])

	# 'DELETE' Methods
	@responses.activate
	def test_remove_server_firewall(self):
		
		with open('mock-api/remove-ip-fp.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'
		server_ip_id = 'SERVER_IP_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/server_ips/%s' % (firewall_id, server_ip_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_firewall_server(firewall_id=firewall_id, server_ip_id=server_ip_id)

		self.assertEqual(r['state'], 'CONFIGURING')
		self.assertEqual(r['server_ips'], [])

	@responses.activate
	def test_remove_firewall_rule(self):
		
		with open('mock-api/delete-rule-fp.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'
		rule_id = 'RULE_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s/rules/%s' % (firewall_id, rule_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_firewall_rule(firewall_id=firewall_id, rule_id=rule_id)

		self.assertNotEqual(len(r['rules']), 3)

	@responses.activate
	def test_delete_firewall(self):

		with open('mock-api/delete-fp.json') as f:
			data = json.load(f)

		firewall_id = 'FIREWALL_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/firewall_policies/%s' % firewall_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_firewall(firewall_id=firewall_id)

		self.assertEqual(r['state'], 'REMOVING')

if __name__ == '__main__':
	unittest.main()