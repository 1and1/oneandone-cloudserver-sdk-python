# List all load balancers
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

load_balancers = client.list_load_balancers()

# Retrieve a single load balancer
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

load_balancer = client.get_load_balancer(load_balancer_id='')

# List all servers attached to a load balancer
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

servers = client.list_load_balancer_servers(load_balancer_id='')

# Retrieve a load balancer server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server = client.get_load_balancer_server(load_balancer_id='', server_ip_id='')

# List all load balancer rules
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

rules = client.load_balancer_rules(load_balancer_id='')

# Retrieve a load balancer rule
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

rule = client.get_load_balancer_rule(load_balancer_id='', rule_id='')

# Create a load balancer
from oneandone.client import OneAndOneService
from oneandone.client import LoadBalancer, LoadBalancerRule

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

lb1 = LoadBalancer(name='Test Load Balancer',
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

# Attach servers to a load balancer
from oneandone.client import OneAndOneService
from oneandone.client import AttachServer

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server1 = AttachServer(server_ip_id='')
server2 = AttachServer(server_ip_id='')
servers = [server1, server2]


response = client.attach_load_balancer_server(load_balancer_id='',
		server_ips=servers)

# Add rules to a load balancer
from oneandone.client import OneAndOneService
from oneandone.client import LoadBalancerRule

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

rule1 = LoadBalancerRule(protocol='TCP', port_balancer=99, port_server=99,
		source='0.0.0.0')
rule2 = LoadBalancerRule(protocol='TCP', port_balancer=125, port_server=521,
		source='0.0.0.0')
rules = [rule1, rule2]


response = client.add_load_balancer_rule(load_balancer_id='',
		load_balancer_rules=rules)

# Modify a load balancer
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_load_balancer = client.modify_load_balancer(name='New Name',
		description='New Description', health_check_test='NONE',
		persistence=False, method='LEAST_CONNECTIONS')

# Delete a load balancer
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_load_balancer(load_balancer_id='')

# Remove server from a load balancer
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.remove_load_balancer_server(load_balancer_id='',
		server_ip_id='')

# Remove load balancer rule
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.remove_load_balancer_rule(load_balancer_id='', rule_id='')

