# List all firewall policies
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

firewall_policies = client.list_firewall_policies()

# Retrieve a single firewall
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

firewall_policy = client.get_firewall(firewall_id='')

# List all servers attached to a firewall
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

servers = client.list_firewall_servers(firewall_id='')

# Retrieve a server attached to a firewall
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server = client.get_firewall_server(firewall_id='', server_ip_id='')

# List all rules of a firewall
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

rules = client.list_firewall_policy_rules(firewall_id='')

# Retrieve a firewall rule
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

rule = client.get_firewall_policy_rule(firewall_id='', rule_id='')

# Create a firewall
from oneandone.client import OneAndOneService
from oneandone.client import FirewallPolicy, FirewallPolicyRule

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

fp1 = FirewallPolicy(name='Test Firewall Policy',
		description='Test Description')


rule1 = FirewallPolicyRule(protocol='TCP', port_from=80, port_to=80,
		source='0.0.0.0')

rule2 = FirewallPolicyRule(protocol='UDP', port_from=443, port_to=443,
		source='0.0.0.0')

rules = [rule1, rule2]


new_firewall = client.create_firewall_policy(firewall_policy=fp1,
		firewall_policy_rules=rules)

# Add rules to a firewall
from oneandone.client import OneAndOneService
from oneandone.client import FirewallPolicyRule

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

new_rule1 = FirewallPolicyRule(protocol='TCP', port_from=90, port_to=90,
		source='0.0.0.0')

new_rule2 = FirewallPolicyRule(protocol='TCP', port_from=333, port_to=333,
		source='0.0.0.0')

new_rules = [new_rule1, new_rule2]


response = client.add_firewall_policy_rule(firewall_id='',
		firewall_policy_rules=new_rules)

# Attach servers to a firewall
from oneandone.client import OneAndOneService
from oneandone.client import AttachServer

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server1 = AttachServer(server_ip_id='')

server2 = AttachServer(server_ip_id='')

servers = [server1, server2]


response = client.attach_server_firewall_policy(firewall_id='',
		server_ips=servers)

# Modify a firewall
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_firewall = client.modify_firewall(name='New Name',
		description='New Description')

# Delete a firewall
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_firewall(firewall_id='')

# Remove a firewall rule
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.remove_firewall_rule(firewall_id='', rule_id='')

# Remove a firewall server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.remove_firewall_server(firewall_id='', server_ip_id='')
