import os
from oneandone.client import OneAndOneService
from oneandone.client import Vpn

token = os.getenv('ONEANDONE_TOKEN')

client = OneAndOneService(token)
# List all vpns
vpns = client.list_vpns()

# Create a vpn
vpn1 = Vpn(name="python vpn",
		   description="test vpn")
new_vpn = client.create_vpn(vpn1)
print vpn1.wait_for()

# Retrieve a single vpn
vpn = client.get_vpn(vpn_id=new_vpn['id'])

# Download vpn configurations
vpn = client.download_config(vpn_id=new_vpn['id'], file_path='c:\\'+new_vpn['name'])

# Modify a vpn
modified_vpn = client.modify_vpn(vpn_id=new_vpn['id'], name='New Name',
		description='New Description')

# Delete a vpn
response = client.delete_vpn(vpn_id=new_vpn['id'])
