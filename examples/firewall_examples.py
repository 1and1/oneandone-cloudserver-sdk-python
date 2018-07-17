import os
import time
from oneandone.client import OneAndOneService
from oneandone.client import FirewallPolicy, FirewallPolicyRule
from oneandone.client import AttachServer
from oneandone.client import Server, Hdd

token = os.getenv('ONEANDONE_TOKEN')
client = OneAndOneService(token)

server_appliances = client.list_appliances(q='ubuntu')

for appliance in server_appliances:
    if appliance['type'] == "IMAGE":
        break

# Create a Server
server1 = Server(name='Test Server12',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1,
                 ram=2,
                 appliance_id=appliance['id'],
                 server_type='cloud'
                 )

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]

new_server = client.create_server(server=server1, hdds=hdds)

print server1.wait_for()

serverResp = client.get_server(server_id=new_server['id'])

# Create a firewall
fp1 = FirewallPolicy(name='Python Test Firewall Policy12',
		description='Test Description')

rule1 = FirewallPolicyRule(protocol='TCP', port=80, source='0.0.0.0', action='allow')

rule2 = FirewallPolicyRule(protocol='UDP', port=443, source='0.0.0.0', action='allow')

rules = [rule1, rule2]


new_firewall = client.create_firewall_policy(firewall_policy=fp1,
		firewall_policy_rules=rules)

fp1.wait_for()

# Attach servers to a firewall
server11 = AttachServer(server_ip_id=serverResp['ips'][0]['id'])
servers = [server11]


response = client.attach_server_firewall_policy(firewall_id=new_firewall['id'],
		server_ips=servers)


# List all firewall policies
firewall_policies = client.list_firewall_policies()

# Retrieve a single firewall
firewall_policy = client.get_firewall(firewall_id=new_firewall['id'])

# List all servers attached to a firewall
servers = client.list_firewall_servers(firewall_id=new_firewall['id'])

# Retrieve a server attached to a firewall
server = client.get_firewall_server(firewall_id=new_firewall['id'], server_ip_id=serverResp['ips'][0]['id'])

# Add rules to a firewall
new_rule1 = FirewallPolicyRule(protocol='TCP', port=90, source='0.0.0.0')

new_rule2 = FirewallPolicyRule(protocol='TCP', port=333, source='0.0.0.0')

new_rules = [new_rule1, new_rule2]


new_rule = client.add_firewall_policy_rule(firewall_id=new_firewall['id'],
		firewall_policy_rules=new_rules)

# List all rules of a firewall
rules = client.list_firewall_policy_rules(firewall_id=new_firewall['id'])

# Retrieve a firewall rule
rule = client.get_firewall_policy_rule(firewall_id=new_firewall['id'], rule_id=new_rule['rules'][0]['id'])

# Modify a firewall
modified_firewall = client.modify_firewall(firewall_id=new_firewall['id'], name='New Name',
		description='New Description')

# Remove a firewall rule
response = client.remove_firewall_rule(firewall_id=new_firewall['id'], rule_id=new_rule['rules'][0]['id'])

print fp1.wait_for()
print server1.wait_for()

# Delete the server
response = client.delete_server(server_id=new_server['id'], keep_ips=None, keep_hdds=None)
server1.wait_deleted()

print fp1.wait_for()
# Delete a firewall
response = client.delete_firewall(firewall_id=new_firewall['id'])


