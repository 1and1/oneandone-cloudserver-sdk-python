# List all users
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

users = client.list_users()

# Retrieve a user
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

user = client.get_user(user_id='')

# Retrieve a user's API privileges
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

api_info = client.api_info(user_id='')

# Retrieve a user's API key
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

api_key = client.show_api_key(user_id='')

# List IPs from which API access is allowed for a user
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

ips_allowed = client.ips_api_access_allowed(user_id='')

# Create user
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

new_user = client.create_user(name='Test User',
                              password='testing123',
                              email='test@example.com',
                              description='Test Description'
                              )

# Add new IPs to the user
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

ip1 = '12.54.127.11'
ip2 = '14.97.4.171'

ips = [ip1, ip2]

response = client.add_user_ip(user_id='', user_ips=ips)

# Modify user information
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.modify_user(user_id='', description='', email='', password='',
		state='ACTIVE')

# Modify a user's API privileges
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.modify_user_api(user_id='', active=True)

# Change a user's API key
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.change_api_key(user_id='')

# Delete a user
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_user(user_id='')

# Remove an IP
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.remove_user_ip(user_id='', ip='14.97.4.171')
