import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import Server
from oneandone.client import Hdd

class TestImage(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('USER-API-KEY')

	# 'GET' Methods
	@responses.activate
	def test_list_servers(self):
		
		with open('mock-api/list-servers.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_servers()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_fixed_servers(self):
		
		with open('mock-api/fixed-server-flavors.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/fixed_instance_sizes',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.fixed_server_flavors()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_fixed_server(self):

		with open('mock-api/get-fixed-server.json') as f:
			data = json.load(f)

		fixed_server_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/fixed_instance_sizes/%s' % fixed_server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_fixed_server(fixed_server_id=fixed_server_id)

		self.assertEqual(r['id'], fixed_server_id)

	@responses.activate
	def test_get_server(self):

		with open('mock-api/get-server.json') as f:
			data = json.load(f)

		server_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_server(server_id=server_id)

		self.assertEqual(r['id'], server_id)

	@responses.activate
	def test_get_server_hardware(self):

		with open('mock-api/get-hardware.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_server_hardware(server_id=server_id)

		self.assertEqual(r['vcore'], 1)

	@responses.activate
	def test_list_server_hdds(self):

		with open('mock-api/list-hdds.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware/hdds' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_server_hdds(server_id=server_id)

		self.assertEqual(r[0]['size'], 40)

	@responses.activate
	def test_get_server_hdd(self):

		with open('mock-api/get-hdd.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'
		hdd_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware/hdds/%s' % (server_id, hdd_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_server_hdd(server_id=server_id, hdd_id=hdd_id)

		self.assertEqual(r['id'], hdd_id)

	@responses.activate
	def test_get_server_image(self):

		with open('mock-api/get-server-image.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/image' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_server_image(server_id=server_id)

		self.assertEqual(r['id'], '76EBF29C1250167C8754B2B3D1C05F68')

	@responses.activate
	def test_list_server_ips(self):

		with open('mock-api/list-server-ips.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_server_ips(server_id=server_id)

		self.assertTrue(len(r) > 0)

	@responses.activate
	def test_get_server_ip(self):

		with open('mock-api/get-server-ip.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'
		ip_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s' % (server_id, ip_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_server_ip(server_id=server_id, ip_id=ip_id)

		self.assertEqual(r['id'], ip_id)

	@responses.activate
	def test_list_ip_firewall_policy(self):

		with open('mock-api/list-server-fps.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'
		ip_id = 'IP_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s/firewall_policy' % (server_id, ip_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_ip_firewall_policy(server_id=server_id, ip_id=ip_id)

		self.assertEqual(r['name'], 'Windows')

	@responses.activate
	def test_list_ip_load_balancers(self):

		with open('mock-api/list-server-lbs.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'
		ip_id = 'IP_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s/load_balancers' % (server_id, ip_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_ip_load_balancers(server_id=server_id, ip_id=ip_id)

		self.assertEqual(r[0]['name'], 'My load balancer')

	@responses.activate
	def test_get_server_status(self):

		with open('mock-api/get-server-status.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/status' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")		

		r = self.client.get_server_status(server_id=server_id)

		self.assertEqual(r['state'], 'POWERED_ON')

	@responses.activate
	def test_get_server_dvd(self):

		with open('mock-api/get-server-dvd.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/dvd' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.get_server_dvd(server_id=server_id)

		self.assertEqual(r['name'], 'Windows 2012 - 64 bits')

	@responses.activate
	def test_list_server_private_networks(self):

		with open('mock-api/list-server-pns.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/private_networks' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_server_private_networks(server_id=server_id)

		self.assertEqual(r[0]['name'], 'New private network 1')

	@responses.activate
	def test_private_network_info(self):

		with open('mock-api/get-server-pn.json') as f:
			data = json.load(f)

		server_id = data['servers'][0]['id']
		private_network_id = data['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/private_networks/%s' % (server_id, private_network_id),
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.private_network_info(server_id=server_id, private_network_id=private_network_id)

		self.assertEqual(r['id'], private_network_id)

	@responses.activate
	def test_list_server_snapshots(self):

		with open('mock-api/list-snapshots.json') as f:
			data = json.load(f)

		server_id = 'SERVER_ID'

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/servers/%s/snapshots' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_server_snapshots(server_id=server_id)

		self.assertEqual(r[0]['id'], 'B77E19E062D5818532EFF11C747BD104')

	# 'PUT' Methods
	@responses.activate
	def test_modify_server(self):

		with open('mock-api/modify-server.json') as f:
			data = json.load(f)

		server_id = data['id']
		name = data['name']
		description = data['description']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s' % server_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.modify_server(server_id=server_id, name=name, description=description)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)

	@responses.activate
	def test_modify_server_hardware(self):
		
		with open('mock-api/modify-server-hardware.json') as f:
			data = json.load(f)

		server_id = data['id']
		vcore = data['hardware']['vcore']
		cores_per_processor = data['hardware']['cores_per_processor']
		ram = data['hardware']['ram']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_server_hardware(server_id=server_id, vcore=vcore, ram=ram, test=True)

		self.assertEqual(r['hardware']['vcore'], vcore)
		self.assertEqual(r['hardware']['cores_per_processor'], cores_per_processor)
		self.assertEqual(r['hardware']['ram'], ram)

	@responses.activate
	def test_modify_hdd(self):

		with open('mock-api/modify-server-hdd.json') as f:
			data = json.load(f)

		server_id = data['id']
		hdd_id = data['hardware']['hdds'][0]['id']
		size = data['hardware']['hdds'][0]['size']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware/hdds/%s' % (server_id, hdd_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_hdd(server_id=server_id, hdd_id=hdd_id, size=150, test=True)

		self.assertEqual(r['hardware']['hdds'][0]['size'], size)

	@responses.activate
	def test_add_firewall(self):

		with open('mock-api/add-firewall.json') as f:
			data = json.load(f)

		server_id = data['id']
		ip_id = data['ips'][0]['id']
		firewall_id = data['ips'][0]['firewall_policy']['id']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s/firewall_policy' % (server_id, ip_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_firewall_policy(server_id=server_id, ip_id=ip_id, firewall_id=firewall_id)

		self.assertEqual(r['ips'][0]['firewall_policy']['id'], firewall_id)

	@responses.activate
	def test_modify_server_status(self):

		with open('mock-api/change-server-status.json') as f:
			data = json.load(f)

		server_id = data['id']
		action = 'POWER_OFF'
		method = 'SOFTWARE'

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/status/action' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.modify_server_status(server_id=server_id, action=action, method=method)

		self.assertEqual(r['status']['state'], 'POWERING_OFF')

	@responses.activate
	def test_load_dvd(self):

		with open('mock-api/load-dvd.json') as f:
			data = json.load(f)

		server_id = data['id']
		dvd_id = 'DVD_ID'

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/dvd' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.load_dvd(server_id=server_id, dvd_id=dvd_id)

		self.assertEqual(r['status']['state'], 'CONFIGURING')

	@responses.activate
	def test_restore_snapshot(self):

		with open('mock-api/restore-snapshot.json') as f:
			data = json.load(f)

		server_id = data['id']
		snapshot_id = data['snapshot']['id']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/snapshots/%s' % (server_id, snapshot_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.restore_snapshot(server_id=server_id, snapshot_id=snapshot_id)

		self.assertEqual(r['snapshot']['id'], snapshot_id)

	@responses.activate
	def test_reinstall_image(self):

		with open('mock-api/reinstall-image.json') as f:
			data = json.load(f)

		server_id = data['id']
		image_id = data['image']['id']

		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/servers/%s/image' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.reinstall_image(server_id=server_id, image_id=image_id)

		self.assertEqual(r['image']['id'], image_id)

	# 'DELETE' Methods
	@responses.activate
	def test_delete_server(self):

		with open('mock-api/delete-server.json') as f:
			data = json.load(f)

		server_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_server(server_id=server_id)

		self.assertEqual(r['status']['state'], 'REMOVING')

	@responses.activate
	def test_remove_hdd(self):

		with open('mock-api/remove-hdd.json') as f:
			data = json.load(f)

		server_id = data['id']
		hdd_id = 'HDD_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware/hdds/%s' % (server_id, hdd_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_hdd(server_id=server_id, hdd_id=hdd_id)

		self.assertEqual(r['status']['state'], 'CONFIGURING')

	@responses.activate
	def test_remove_ip(self):

		with open('mock-api/remove-server-ip.json') as f:
			data = json.load(f)

		server_id = data['id']
		ip_id = 'IP_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s' % (server_id, ip_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_ip(server_id=server_id, ip_id=ip_id)

		self.assertNotIn(ip_id, r['ips'])

	@responses.activate
	def test_remove_firewall_policy(self):

		with open('mock-api/remove-firewall-policy.json') as f:
			data = json.load(f)

		server_id = data['id']
		ip_id = data['ips'][0]['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s/firewall_policy' % (server_id, ip_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_firewall_policy(server_id=server_id, ip_id=ip_id)

		self.assertEqual(r['ips'][0]['firewall_policy'], None)

	@responses.activate
	def test_remove_load_balancer(self):

		with open('mock-api/remove-lb.json') as f:
			data = json.load(f)

		server_id = data['id']
		ip_id = data['ips'][0]['id']
		load_balancer_id = 'LOAD_BALANCER_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s/load_balancers/%s' % (server_id, ip_id, load_balancer_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_load_balancer(server_id=server_id, ip_id=ip_id, load_balancer_id=load_balancer_id)

		self.assertEqual(r['ips'][0]['load_balancers'], [])

	@responses.activate
	def test_remove_private_network(self):

		with open('mock-api/remove-pn.json') as f:
			data = json.load(f)

		server_id = data['id']
		private_network_id = 'PRIVATE_NETWORK_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/private_networks/%s' % (server_id, private_network_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.remove_private_network(server_id=server_id, private_network_id=private_network_id)

		self.assertNotIn(private_network_id, r['private_networks'])

	@responses.activate
	def test_eject_dvd(self):

		with open('mock-api/eject-dvd.json') as f:
			data = json.load(f)

		server_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/dvd' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.eject_dvd(server_id=server_id)

		self.assertEqual(r['status']['state'], 'CONFIGURING')

	@responses.activate
	def test_delete_snapshot(self):

		with open('mock-api/delete-snapshot.json') as f:
			data = json.load(f)

		server_id = data['id']
		snapshot_id = 'SNAPSHOT_ID'

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/servers/%s/snapshots/%s' % (server_id, snapshot_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_snapshot(server_id=server_id, snapshot_id=snapshot_id)

		self.assertEqual(r['status']['state'], 'CONFIGURING')

	# 'POST' Methods
	@responses.activate
	def test_create_server(self):

		with open('mock-api/create-server.json') as f:
			data = json.load(f)

		server1 = Server(name=data['name'], description=data['description'], vcore=data['hardware']['vcore'],
						 cores_per_processor=data['hardware']['cores_per_processor'], ram=data['hardware']['ram'],
						 appliance_id='APPLIANCE_ID')
		hdd1 = Hdd(size=40, is_main=True)
		hdds = [hdd1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_server(server=server1, hdds=hdds)

		self.assertEqual(r['name'], server1.specs['name'])
		self.assertEqual(r['status']['state'], 'DEPLOYING')

	@responses.activate
	def test_add_hdd(self):

		with open('mock-api/add-hdd.json') as f:
			data = json.load(f)

		server_id = data['id']
		hdd1 = Hdd(size=40, is_main=False)
		hdds = [hdd1]

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers/%s/hardware/hdds' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_hdd(server_id=server_id, hdds=hdds)

		self.assertEqual(r['status']['state'], 'CONFIGURING')

	@responses.activate
	def test_add_new_ip(self):

		with open('mock-api/add-server-ip.json') as f:
			data = json.load(f)

		server_id = data['id']

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_new_ip(server_id=server_id)

		self.assertTrue(len(r['ips']) > 0)

	@responses.activate
	def test_add_load_balancer(self):

		with open('mock-api/add-lb.json') as f:
			data = json.load(f)

		server_id = data['id']
		ip_id = data['ips'][0]['id']
		load_balancer_id = data['ips'][0]['load_balancers'][0]['id']

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers/%s/ips/%s/load_balancers' % (server_id, ip_id),
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.add_load_balancer(server_id=server_id, ip_id=ip_id, load_balancer_id=load_balancer_id)

		self.assertEqual(r['ips'][0]['load_balancers'][0]['id'], load_balancer_id)

	@responses.activate
	def test_assign_private_network(self):

		with open('mock-api/add-pn.json') as f:
			data = json.load(f)

		server_id = data['id']
		private_network_id = 'PRIVATE_NETWORK_ID'

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers/%s/private_networks' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.assign_private_network(server_id=server_id, private_network_id=private_network_id)

		self.assertEqual(r['private_networks'], None)

	@responses.activate
	def test_create_snapshot(self):

		with open('mock-api/create-snapshot.json') as f:
			data = json.load(f)

		server_id = data['id']
		snapshot_id = data['snapshot']['id']

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers/%s/snapshots' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_snapshot(server_id=server_id)

		self.assertEqual(r['snapshot']['id'], snapshot_id)

	@responses.activate
	def test_clone_server(self):

		with open('mock-api/clone-server.json') as f:
			data = json.load(f)

		server_id = data['id']
		name = data['name']

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/servers/%s/clone' % server_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.clone_server(server_id=server_id, name=name)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['status']['state'], 'DEPLOYING')

if __name__ == '__main__':
	unittest.main()