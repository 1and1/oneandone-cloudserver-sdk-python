import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import LoadBalancer
from oneandone.client import LoadBalancerRule
from oneandone.client import AttachServer

class TestLoadBalancer(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_load_balancers(self):

		with open('mock-api/list-load-balancers.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/load_balancers',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_load_balancers()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_load_balancer(self):

		with open('mock-api/get-load-balancer.json') as f:
			data = json.load(f)

		load_balancer_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s' % load_balancer_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_load_balancer(load_balancer_id=load_balancer_id)

		self.assertEqual(r['id'], load_balancer_id)

	@responses.activate
	def test_list_servers_load_balancer(self):

		with open('mock-api/list-lb-servers.json') as f:
			data = json.load(f)

		load_balancer_id = 'LOAD_BALANCER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/server_ips' % load_balancer_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_load_balancer_servers(load_balancer_id=load_balancer_id)

		self.assertEqual(len(r), 2)

	@responses.activate
	def test_get_load_balancer_server(self):

		with open('mock-api/get-lb-server.json') as f:
			data = json.load(f)

		load_balancer_id = 'LOAD_BALANCER_ID'
		server_ip_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/server_ips/%s' % (load_balancer_id, server_ip_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_load_balancer_server(load_balancer_id=load_balancer_id, server_ip_id=server_ip_id)

		self.assertEqual(r['id'], server_ip_id)

	@responses.activate
	def test_load_balancer_rules(self):

		with open('mock-api/list-lb-rules.json') as f:
			data = json.load(f)

		load_balancer_id = 'LOAD_BALANCER_ID'
		first_rule_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/rules' % load_balancer_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.load_balancer_rules(load_balancer_id=load_balancer_id)

		self.assertEqual(r[0]['id'], first_rule_id)

	@responses.activate
	def test_get_load_balancer_rule(self):

		with open('mock-api/get-lb-rule.json') as f:
			data = json.load(f)

		load_balancer_id = 'LOAD_BALANCER_ID'
		rule_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/rules/%s' % (load_balancer_id, rule_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_load_balancer_rule(load_balancer_id=load_balancer_id, rule_id=rule_id)

		self.assertEqual(r['id'], rule_id)		

	# 'PUT' Methods
	@responses.activate
	def test_modify_load_balancer(self):

		with open('mock-api/modify-lb.json') as f:
			data = json.load(f)

		load_balancer_id = data['id']
		name = data['name']
		description = data['description']
		method = data['method']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s' % load_balancer_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_load_balancer(load_balancer_id=load_balancer_id, name=name, description=description, method=method)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)
		self.assertEqual(r['method'], method)

	# 'POST' Methods
	@responses.activate
	def test_create_load_balancer(self):
		lb1 = LoadBalancer(name='Unit Test', health_check_test='TCP', health_check_interval=20, persistence=True, persistence_time=200,
			method='LEAST_CONNECTIONS')
		rule1 = LoadBalancerRule(protocol='TCP', port_balancer=22, port_server=22)
		rules = [rule1]

		with open('mock-api/create-lb.json') as f:
			data = json.load(f)

		lb1 = LoadBalancer(name=data['name'], health_check_test=data['health_check_test'], health_check_interval=data['health_check_interval'],
						   persistence=data['persistence'], persistence_time=data['persistence_time'], method=data['method'])
		
		rule1 = LoadBalancerRule(protocol=data['rules'][0]['protocol'], port_balancer=data['rules'][0]['port_balancer'],
								 port_server=data['rules'][0]['port_server'])
		rule2 = LoadBalancerRule(protocol=data['rules'][1]['protocol'], port_balancer=data['rules'][1]['port_balancer'],
								 port_server=data['rules'][1]['port_server'])
		rules = [rule1, rule2]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/load_balancers',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_load_balancer(load_balancer=lb1, load_balancer_rules=rules)

		self.assertEqual(r['name'], lb1.specs['name'])
		self.assertEqual(r['health_check_test'], lb1.specs['health_check_test'])
		self.assertEqual(r['health_check_interval'], lb1.specs['health_check_interval'])
		self.assertEqual(r['method'], lb1.specs['method'])

	@responses.activate
	def test_attach_server_load_balancer(self):

		with open('mock-api/assign-server-lb.json') as f:
			data = json.load(f)

		load_balancer_id = data['id']
		server1 = AttachServer(server_ip_id=data['server_ips'][0]['id'])

		servers = [server1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/server_ips' % load_balancer_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.attach_load_balancer_server(load_balancer_id=load_balancer_id, server_ips=servers)

		self.assertEqual(r['server_ips'][0]['id'], server1.server_ip_id)

	@responses.activate
	def test_add_rule_load_balancer(self):

		with open('mock-api/add-rule-lb.json') as f:
			data = json.load(f)

		load_balancer_id = 'LOAD_BALANCER_ID'
		rule1 = LoadBalancerRule(protocol=data['rules'][0]['protocol'], port_balancer=data['rules'][0]['port_balancer'],
								 port_server=data['rules'][0]['port_server'])
		rule2 = LoadBalancerRule(protocol=data['rules'][1]['protocol'], port_balancer=data['rules'][1]['port_balancer'],
								 port_server=data['rules'][1]['port_server'])
		rule3 = LoadBalancerRule(protocol=data['rules'][2]['protocol'], port_balancer=data['rules'][2]['port_balancer'],
								 port_server=data['rules'][2]['port_server'])
		rules = [rule1, rule2, rule3]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/rules' % load_balancer_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_load_balancer_rule(load_balancer_id=load_balancer_id, load_balancer_rules=rules)

		self.assertEqual(len(r['rules']), 3)

	# 'DELETE' Methods
	@responses.activate
	def test_remove_load_balancer_server(self):

		with open('mock-api/detach-server-lb.json') as f:
			data = json.load(f)

		load_balancer_id = data['id']
		server_ip_id = 'SERVER_IP_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/server_ips/%s' % (load_balancer_id, server_ip_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_load_balancer_server(load_balancer_id=load_balancer_id, server_ip_id=server_ip_id)

		self.assertEqual(r['server_ips'], [])

	@responses.activate
	def test_remove_rule(self):

		with open('mock-api/remove-rule-lb.json') as f:
			data = json.load(f)

		load_balancer_id = data['id']
		rule_id = 'RULE_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s/rules/%s' % (load_balancer_id, rule_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_load_balancer_rule(load_balancer_id=load_balancer_id, rule_id=rule_id)

		self.assertEqual(len(r['rules']), 2)

	@responses.activate
	def test_delete_load_balancer(self):
		load_balancer_id = '2652331583F5C01BA803016A60E94CAE'

		with open('mock-api/delete-lb.json') as f:
			data = json.load(f)

		load_balancer_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/load_balancers/%s' % load_balancer_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_load_balancer(load_balancer_id=load_balancer_id)

		self.assertEqual(r['state'], 'REMOVING')

if __name__ == '__main__':
	unittest.main()