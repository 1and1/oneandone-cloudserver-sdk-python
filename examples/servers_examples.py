# List all servers
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

servers = client.list_servers()

# Retrieve a single server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

server = client.get_server(server_id='')

# List fixed server flavors
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

fixed_servers = client.fixed_server_flavors()

# Retrieve information about a fixed server flavor
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

fixed_server = client.get_fixed_server(fixed_server_id='')

# List baremetal models
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

fixed_servers = client.list_baremetal_models()

# Retrieve information about a baremetal model
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

fixed_server = client.get_baremetal_model(model_id='')

# Retrieve information about a server's hardware
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

hardware = client.get_server_hardware(server_id='')

# List a server's HDDs
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

hdds = client.list_server_hdds(server_id='')

# Retrieve a single HDD
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

hdd = client.get_server_hdd(server_id='', hdd_id='')

# Retrieve a server's image
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

image = client.get_server_image(server_id='')

# List a server's IPs
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

ips = client.list_server_ips(server_id='')

# Retrieve a single server IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

ip = client.get_server_ip(server_id='', ip_id='')

# List all firewall policies attached to a server's IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

firewalls = client.list_ip_firewall_policy(server_id='', ip_id='')

# List all load balancers attached to a server's IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

load_balancers = client.list_ip_load_balancers(server_id='', ip_id='')

# Retrieve a server's status
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

status = client.get_server_status(server_id='')

# Retrieve a server's DVD info
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

dvd_info = client.get_server_dvd(server_id='')

# List a server's private networks
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

private_networks = client.list_server_private_networks(server_id='')

# Retrieve a single private network
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

private_network = client.private_network_info(server_id='',
                                              private_network_id='')

# List all server snapshots
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

snapshots = client.list_server_snapshots(server_id='')

# Create a cloud server
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd

client = OneAndOneService('API-TOKEN')

server1 = Server(name='Test Server',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1,
                 ram=2,
                 appliance_id='',
                 server_type='cloud'
                 )

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]

new_server = client.create_server(server=server1, hdds=hdds)

# Create a baremetal server
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd

client = OneAndOneService('API-TOKEN')

server1 = Server(name='Test Server',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1,
                 ram=2,
                 appliance_id='',
                 server_type='baremetal',
                 baremetal_model_id=''
                 )

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]

new_server = client.create_server(server=server1, hdds=hdds)

# Add a new HDD to a server
from oneandone.client import OneAndOneService
from oneandone.client import Hdd

client = OneAndOneService('API-TOKEN')

hdd2 = Hdd(size=40, is_main=False)
hdds = [hdd2]

response = client.add_hdd(server_id='', hdds=hdds)

# Add a new IP to a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.add_new_ip(server_id='')

# Add a load balancer to a server IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.add_load_balancer(server_id='', ip_id='', load_balancer_id='')

# Assign a private network to a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.assign_private_network(server_id='', private_network_id='')

# Create a server snapshot
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

new_snapshot = client.create_snapshot(server_id='')

# Clone a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

cloned_server = client.clone_server(server_id='', name='Clone Server')

# Modify a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.modify_server(server_id='', name='New Name',
                                description='New Description')

# Modify server hardware
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.modify_server_hardware(server_id='', vcore=2, ram=6)

# Modify a HDD
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.modify_hdd(server_id='', hdd_id='', size=80)

# Add a firewall policy to a server's IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.add_firewall_policy(server_id='', ip_id='', firewall_id='')

# Modify a server's status
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.modify_server_status(server_id='', action='REBOOT',
                                       method='SOFTWARE')

# Stop a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.stop_server(server_id='')

# Start a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.start_server(server_id='')

# Load a DVD into a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.load_dvd(server_id='', dvd_id='')

# Restore a snapshot
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.restore_snapshot(server_id='', snapshot_id='')

# Reinstall an image
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.reinstall_image(server_id='', image_id='')

# Delete a server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.delete_server(server_id='')

# Remove a server's HDD
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.remove_hdd(server_id='', hdd_id='')

# Release an IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.remove_ip(server_id='', ip_id='')

# Remove a load balancer from a server IP
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.remove_load_balancer(server_id='', ip_id='',
                                       load_balancer_id='')

# Remove a private network from the server
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.remove_private_network(server_id='', private_network_id='')

# Eject a DVD
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.eject_dvd(server_id='')

# Remove a snapshot
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.delete_snapshot(server_id='', snapshot_id='')
