import os
from oneandone.client import OneAndOneService

token = os.getenv('ONEANDONE_TOKEN')

client = OneAndOneService(token)

# List all users
users = client.list_users()

# Retrieve a user
user = client.get_user(user_id='')

# Retrieve a user's API privileges
api_info = client.api_info(user_id='')

# Retrieve a user's API key
api_key = client.show_api_key(user_id='')

# Retrieve users current permissions
user_permissions = client.show_user_permissions()

# List IPs from which API access is allowed for a user
ips_allowed = client.ips_api_access_allowed(user_id='')

# Create user
new_user = client.create_user(name='Test User',
                              password='testing123',
                              email='test@example.com',
                              description='Test Description'
                              )

# Add new IPs to the user
ip1 = '12.54.127.11'
ip2 = '14.97.4.171'

ips = [ip1, ip2]

response = client.add_user_ip(user_id='', user_ips=ips)

# Modify user information
response = client.modify_user(user_id='', description='', email='', password='',
		state='ACTIVE')

# Modify a user's API privileges
response = client.modify_user_api(user_id='', active=True)

# Change a user's API key
response = client.change_api_key(user_id='')

# Delete a user
response = client.delete_user(user_id='')

# Remove an IP
response = client.remove_user_ip(user_id='', ip='14.97.4.171')
