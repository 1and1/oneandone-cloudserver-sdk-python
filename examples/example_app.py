from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd, LoadBalancer, LoadBalancerRule
from oneandone.client import FirewallPolicy, FirewallPolicyRule

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

# Create Load Balancer
lb1 = LoadBalancer(name='Example App LB',
                   description='Test Description',
                   health_check_test='TCP',
                   health_check_interval=40,
                   persistence=True,
                   persistence_time=1200,
                   method='ROUND_ROBIN'
                  )

rule1 = LoadBalancerRule(protocol='TCP', port_balancer=80, port_server=80,
	source='0.0.0.0')
rule2 = LoadBalancerRule(protocol='TCP', port_balancer=9999, port_server=8888,
	source='0.0.0.0')

rules = [rule1, rule2]

new_load_balancer = client.create_load_balancer(load_balancer=lb1,
	load_balancer_rules=rules)

## Wait for Load Balancer to go live
print 'Creating load balancer...'
lb1.wait_for()

# Create Firewall Policy
fp1 = FirewallPolicy(name='Example App FP', description='Test Description')


rule1 = FirewallPolicyRule(protocol='TCP', port_from=80, port_to=80,
	source='0.0.0.0')

rule2 = FirewallPolicyRule(protocol='UDP', port_from=443, port_to=443,
	source='0.0.0.0')

rules = [rule1, rule2]


new_firewall = client.create_firewall_policy(firewall_policy=fp1,
	firewall_policy_rules=rules)

## Wait for Firewall Policy to go live
print 'Creating firewall policy...'
fp1.wait_for()

# Create Server
server1 = Server(name='Example App Server',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1, 
                 ram=2, 
                 appliance_id='D9DBA7D7F7E9C8200A493CE9013C4605'
                 )

hdd1 = Hdd(size=120, is_main=True)
hdd2 = Hdd(size=60, is_main=False)

hdds = [hdd1, hdd2]

new_server = client.create_server(server=server1, hdds=hdds)

## Wait for the Server to go live
print 'Creating new server...'
server1.wait_for()

# Add an IP to the server
new_ip = client.add_new_ip(server_id=new_server['id'])

# Add Load Balancer to New Server
lb_response = client.add_load_balancer(server_id=new_server['id'],
	ip_id=new_ip['ips'][1]['id'], load_balancer_id=new_load_balancer['id'])

## Wait for Load Balancer to be added
print 'Adding load balancer to Server...'
server1.wait_for()

# Add Firewall Policy to New Server
fw_response = client.add_firewall_policy(server_id=new_server['id'],
	ip_id=new_ip['ips'][1]['id'], firewall_id=new_firewall['id'])

## Wait for Firewall Policy to be added
print 'Adding firewall policy to Server...'
server1.wait_for()
print 'Everything looks good!'

# Cleanup the rubbish
print 'Cleaning up the mess we just made...\n'

print 'Deleting server...'
deleted_server = client.delete_server(server_id=new_server['id'])
print 'Deleting load balancer...'
deleted_lb = client.delete_load_balancer(load_balancer_id=new_load_balancer['id'])
print 'Deleting firewall...'
deleted_fw = client.delete_firewall(firewall_id=new_firewall['id'])

print '\nAll done!'

