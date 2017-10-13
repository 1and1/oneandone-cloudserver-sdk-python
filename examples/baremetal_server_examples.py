import os

from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd

token = os.getenv('ONEANDONE_TOKEN')

client = OneAndOneService(token)
print "creating bare metal server"
server_appliances = client.list_appliances(q='centos7-64min')

baremetal_model = client.list_baremetal_models(q='BMC_L')


# Create a server
server1 = Server(name='Python baremetal Server',
                 description='Server Description',
                 server_type='baremetal',
                 baremetal_model_id=baremetal_model[0]['id'],
                 appliance_id=server_appliances[0]['id']
                 )

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]
new_server = client.create_server(server=server1)
print server1.wait_for()

# Add a new HDD to a server
print "add a new HDD to the server"
hdd2 = Hdd(size=40, is_main=False)
hdds = [hdd2]

response = client.add_hdd(server_id=new_server['id'], hdds=hdds)
print server1.wait_for()

# Add a new IP to a server.
print "add a new IP to the server"
response = client.add_new_ip(server_id=new_server['id'], ip_type='IPV4')
print server1.wait_for()

# Modify a server
print "Rename server"
response = client.modify_server(server_id=new_server['id'], name='New baremetal Name',
                                description='New Description')
print server1.wait_for()

# Modify a server's status
print "Reboot server"
response = client.modify_server_status(server_id=new_server['id'], action='REBOOT',
                                       method='SOFTWARE')
print server1.wait_for()
# Retrieve a single server
print "Retrieve server"
server = client.get_server(server_id=new_server['id'])

# Retrieve information about a server's hardware
print "Retrieve information about a server's hardware"
hardware = client.get_server_hardware(server_id=new_server['id'])
print hardware

# List a server's HDDs
print "List a server's HDDs"
hdds = client.list_server_hdds(server_id=new_server['id'])
print len(hdds) + " found"

# Retrieve a server's status
print "Retrieve a server's status"
status = client.get_server_status(server_id=new_server['id'])
print status

# Delete a server
print "Deleting the server"
response = client.delete_server(server_id=new_server['id'])
