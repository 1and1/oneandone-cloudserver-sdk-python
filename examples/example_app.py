from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd, LoadBalancer, LoadBalancerRule
from oneandone.client import FirewallPolicy, FirewallPolicyRule

client = OneAndOneService('<API-Token>')


# Create Load Balancer
lb1 = LoadBalancer(name='Example App LB', description='Example Description',
  health_check_test='TCP', health_check_interval=40, persistence=True,
  persistence_time=1200, method='ROUND_ROBIN')

rule1 = LoadBalancerRule(protocol='TCP', port_balancer=80, port_server=80,
	source='0.0.0.0')

rules = [rule1]

new_load_balancer = client.create_load_balancer(load_balancer=lb1,
	load_balancer_rules=rules)

## Wait for Load Balancer to go live
print 'Creating load balancer...'
print lb1.wait_for()


# Create Firewall Policy
fp1 = FirewallPolicy(name='Example App FP', description='Test Description')

rule1 = FirewallPolicyRule(protocol='TCP', port_from=80, port_to=80,
	source='0.0.0.0')

rules = [rule1]

new_firewall = client.create_firewall_policy(firewall_policy=fp1,
	firewall_policy_rules=rules)

## Wait for Firewall Policy to go live
print 'Creating firewall policy...'
print fp1.wait_for()


# Create Server
server1 = Server(name='Example App Server',
  fixed_instance_size_id='65929629F35BBFBA63022008F773F3EB',
  appliance_id='6C902E5899CC6F7ED18595EBEB542EE1',
  datacenter_id='5091F6D8CBFEF9C26ACE957C652D5D49')

new_server = client.create_server(server=server1)

## Wait for the Server to go live
print 'Creating new server...'
print server1.wait_for()


# Add Load Balancer to New Server
lb_response = client.add_load_balancer(server_id=new_server['id'],
	ip_id=server1.first_ip['id'], load_balancer_id=new_load_balancer['id'])

## Wait for Load Balancer to be added
print 'Adding load balancer to Server...'
print server1.wait_for()


# Add Firewall Policy to New Server
fw_response = client.add_firewall_policy(server_id=new_server['id'],
	ip_id=server1.first_ip['id'], firewall_id=new_firewall['id'])

## Wait for Firewall Policy to be added
print 'Adding firewall policy to Server...'
print server1.wait_for()
print 'Everything looks good!'


# Cleanup the rubbish
print 'Cleaning up the mess we just made...\n'

print 'Deleting server...'
client.delete_server(server_id=new_server['id'])

print 'Deleting load balancer...'
client.delete_load_balancer(load_balancer_id=new_load_balancer['id'])

print 'Deleting firewall...'
client.delete_firewall(firewall_id=new_firewall['id'])

print '\nAll done!'