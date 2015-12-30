import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import MonitoringPolicy
from oneandone.client import Threshold
from oneandone.client import Port
from oneandone.client import Process
from oneandone.client import AttachServer

class TestMonitoringPolicy(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_monitoring_policies(self):
		
		with open('mock-api/list-mps.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_monitoring_policies()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_monitoring_policy(self):

		with open('mock-api/get-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s' % monitoring_policy_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_monitoring_policy(monitoring_policy_id=monitoring_policy_id)

		self.assertEqual(r['id'], monitoring_policy_id)

	@responses.activate
	def test_list_ports(self):

		with open('mock-api/list-mp-ports.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/ports' % monitoring_policy_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_monitoring_policy_ports(monitoring_policy_id=monitoring_policy_id)

		self.assertEqual(len(r), 2)

	@responses.activate
	def test_get_port(self):

		with open('mock-api/get-mp-port.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'
		port_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/ports/%s' % (monitoring_policy_id, port_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_monitoring_policy_port(monitoring_policy_id=monitoring_policy_id, port_id=port_id)

		self.assertEqual(r['id'], port_id)

	@responses.activate
	def test_list_processes(self):

		with open('mock-api/list-mp-processes.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/processes' % monitoring_policy_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_monitoring_policy_processes(monitoring_policy_id=monitoring_policy_id)

		self.assertEqual(len(r), 2)

	@responses.activate
	def test_get_process(self):

		with open('mock-api/get-mp-process.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'
		process_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/processes/%s' % (monitoring_policy_id, process_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_monitoring_policy_process(monitoring_policy_id=monitoring_policy_id, process_id=process_id)

		self.assertEqual(r['id'], process_id)

	@responses.activate
	def test_list_servers(self):

		with open('mock-api/list-mp-servers.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/servers' % monitoring_policy_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_monitoring_policy_servers(monitoring_policy_id=monitoring_policy_id)

		self.assertEqual(len(r), 2)

	@responses.activate
	def test_get_server(self):

		with open('mock-api/get-mp-server.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'
		server_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/servers/%s' % (monitoring_policy_id, server_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_monitoring_policy_server(monitoring_policy_id=monitoring_policy_id, server_id=server_id)

		self.assertEqual(r['id'], server_id)

	# 'DELETE' Methods
	@responses.activate
	def test_delete_port_monitoring_policy(self):

		with open('mock-api/remove-port-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		port_id = 'PORT_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/ports/%s' % (monitoring_policy_id, port_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_monitoring_policy_port(monitoring_policy_id=monitoring_policy_id, port_id=port_id)

		self.assertEqual(r['ports'], [])

	@responses.activate
	def test_delete_process(self):

		with open('mock-api/remove-process-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		process_id = 'PROCESS_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/processes/%s' % (monitoring_policy_id, process_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")		

		r = self.client.delete_monitoring_policy_process(monitoring_policy_id=monitoring_policy_id, process_id=process_id)

		self.assertEqual(r['processes'], [])

	@responses.activate
	def test_detach_server(self):

		with open('mock-api/detach-server-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		server_id = 'SERVER_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/servers/%s' % (monitoring_policy_id, server_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.detach_monitoring_policy_server(monitoring_policy_id=monitoring_policy_id, server_id=server_id)

		self.assertEqual(len(r['servers']), 2)
		self.assertEqual(r['state'], 'CONFIGURING')

	@responses.activate
	def test_delete_monitoring_policy(self):

		with open('mock-api/delete-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s' % monitoring_policy_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_monitoring_policy(monitoring_policy_id=monitoring_policy_id)

		self.assertEqual(r['state'], 'REMOVING')

	# 'POST' Methods
	@responses.activate
	def test_create_monitoring_policy(self):

		with open('mock-api/create-mp.json') as f:
			data = json.load(f)

		## MP Object
		monitoring_policy1 = MonitoringPolicy(name=data['name'], email=data['email'], agent=data['agent'])

		## Thresholds
		cpu = Threshold(entity='cpu', warning_value=data['thresholds']['cpu']['warning']['value'], warning_alert=data['thresholds']['cpu']['warning']['alert'],
						critical_value=data['thresholds']['cpu']['critical']['value'], critical_alert=data['thresholds']['cpu']['critical']['alert'])
		ram = Threshold(entity='ram', warning_value=data['thresholds']['ram']['warning']['value'], warning_alert=data['thresholds']['ram']['warning']['alert'],
						critical_value=data['thresholds']['ram']['critical']['value'], critical_alert=data['thresholds']['ram']['critical']['alert'])
		disk = Threshold(entity='disk', warning_value=data['thresholds']['disk']['warning']['value'], warning_alert=data['thresholds']['disk']['warning']['alert'],
						critical_value=data['thresholds']['disk']['critical']['value'], critical_alert=data['thresholds']['disk']['critical']['alert'])
		transfer = Threshold(entity='transfer', warning_value=data['thresholds']['transfer']['warning']['value'], warning_alert=data['thresholds']['transfer']['warning']['alert'],
						critical_value=data['thresholds']['transfer']['critical']['value'], critical_alert=data['thresholds']['transfer']['critical']['alert'])
		internal_ping = Threshold(entity='internal_ping', warning_value=data['thresholds']['internal_ping']['warning']['value'], warning_alert=data['thresholds']['internal_ping']['warning']['alert'],
						critical_value=data['thresholds']['internal_ping']['critical']['value'], critical_alert=data['thresholds']['internal_ping']['critical']['alert'])
		thresholds = [cpu, ram, disk, transfer, internal_ping]

		## Ports
		port1 = Port(protocol=data['ports'][0]['protocol'], port=data['ports'][0]['port'], alert_if=data['ports'][0]['alert_if'],
					 email_notification=data['ports'][0]['email_notification'])
		ports = [port1]

		## Processes
		process1 = Process(process=data['processes'][0]['process'], alert_if=data['processes'][0]['alert_if'],
						   email_notification=data['processes'][0]['email_notification'])
		processes = [process1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies',
					  body=json.dumps(data), status=201,
					  content_type="application/json")

		r = self.client.create_monitoring_policy(monitoring_policy=monitoring_policy1, thresholds=thresholds, ports=ports, processes=processes)

		self.assertEqual(r['name'], monitoring_policy1.specs['name'])
		self.assertEqual(r['email'], monitoring_policy1.specs['email'])
		self.assertEqual(r['agent'], monitoring_policy1.specs['agent'])
		self.assertEqual(r['ports'][0]['protocol'], port1.specs['protocol'])
		self.assertEqual(r['processes'][0]['process'], process1.process_set['process'])

	@responses.activate
	def test_add_port(self):

		with open('mock-api/add-port-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		port1 = Port(protocol=data['ports'][0]['protocol'], port=data['ports'][0]['port'], alert_if='NOT_RESPONDING',
					 email_notification=True)
		ports = [port1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/ports' % monitoring_policy_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_port(monitoring_policy_id=monitoring_policy_id, ports=ports)

		self.assertEqual(r['ports'][0]['protocol'], port1.specs['protocol'])
		self.assertEqual(r['ports'][0]['port'], port1.specs['port'])

	@responses.activate
	def test_add_process(self):

		with open('mock-api/add-process-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = 'MONITORING_POLICY_ID'
		process1 = Process(process=data[2]['process'], alert_if=data[2]['alert_if'], email_notification=data[2]['email_notifications'])
		processes = [process1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/processes' % monitoring_policy_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_process(monitoring_policy_id=monitoring_policy_id, processes=processes)

		self.assertEqual(r[2]['process'], process1.process_set['process'])
		self.assertEqual(r[2]['alert_if'], process1.process_set['alert_if'])
		self.assertEqual(r[2]['email_notifications'], process1.process_set['email_notification'])

	@responses.activate
	def test_attach_server(self):

		with open('mock-api/add-server-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		server1 = AttachServer(server_id='92AA60BEC8333A21EDB9EAAA61852860')
		servers = [server1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/servers' % monitoring_policy_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.attach_monitoring_policy_server(monitoring_policy_id=monitoring_policy_id, servers=servers)

		self.assertEqual(r['state'], 'CONFIGURING')

	# 'PUT' Methods
	@responses.activate
	def test_modify_port(self):

		with open('mock-api/modify-port-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		port_id = 'PORT_ID'
		edit_port = Port(port=data['ports'][0]['port'], alert_if='NOT_RESPONDING', email_notification=False)

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/ports/%s' % (monitoring_policy_id, port_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_port(monitoring_policy_id=monitoring_policy_id, port_id=port_id, port=edit_port, test=True)

		self.assertEqual(r['ports'][0]['port'], edit_port.specs['port'])

	@responses.activate
	def test_modify_process(self):

		with open('mock-api/modify-process-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']
		process_id = data['processes'][0]['process']
		edit_process = Process(alert_if='NOT_RUNNING', email_notification=False)

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s/processes/%s' % (monitoring_policy_id, process_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_process(monitoring_policy_id=monitoring_policy_id, process_id=process_id, process=edit_process, test=True)

		self.assertEqual(r['processes'][0]['process'], process_id)

	@responses.activate
	def test_modify_monitoring_policy(self):

		with open('mock-api/modify-mp.json') as f:
			data = json.load(f)

		monitoring_policy_id = data['id']

		cpu = Threshold(entity='cpu', warning_value=80, warning_alert=True, critical_value=90, critical_alert=True)
		ram = Threshold(entity='ram', warning_value=80, warning_alert=True, critical_value=90, critical_alert=True)
		disk = Threshold(entity='disk', warning_value=70, warning_alert=True, critical_value=80, critical_alert=True)

		thresholds = [cpu, ram, disk]

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/monitoring_policies/%s' % monitoring_policy_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_monitoring_policy(monitoring_policy_id=monitoring_policy_id, thresholds=thresholds, test=True)

		self.assertEqual(r['thresholds']['cpu']['warning']['value'], 90)

if __name__ == '__main__':
	unittest.main()