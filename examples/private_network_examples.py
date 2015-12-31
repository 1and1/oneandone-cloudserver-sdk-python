# List all private networks
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

private_networks = client.list_private_networks()

# Retrieve a private network
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

private_network = client.get_private_network(private_network_id='')

# List all servers attached to a private network
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

servers = client.list_private_network_servers(private_network_id='')

# Retrieve a private network server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server = client.get_private_network_server(private_network_id='', server_id='')

# Create a private network
from oneandone.client import OneAndOneService
from oneandone.client import PrivateNetwork

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

pn1 = PrivateNetwork(name='Test Name',
                     description='Test Description',
                     network_address='192.168.1.0',
                     subnet_mask='255.255.255.0'
                     )

new_private_network = client.create_private_network(private_network=pn1)

# Attach servers to a private network
from oneandone.client import OneAndOneService
from oneandone.client import AttachServer

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server1 = AttachServer(server_id='')
server2 = AttachServer(server_id='')
servers = [server1, server2]

response = client.attach_private_network_servers(private_network_id='',
		server_ids=servers)

# Modify a private network
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_private_network = client.modify_private_network(private_network_id='',
		name='New Name')

# Delete a private network
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_private_network(private_network_id='')

# Remove private network server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.remove_private_network_server(private_network_id='',
		server_id='')
