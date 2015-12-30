# List all public IPs
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

public_ips = client.list_public_ips()

# Retrieve a public IP
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

public_ip = client.get_public_ip(ip_id='')

# Create a public IP
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

new_public_ip = client.create_public_ip(reverse_dns='example.com')

# Modify a public IP
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_ip = client.modify_public_ip(ip_id='', reverse_dns='newexample.com')

# Delete a public IP
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_public_ip(ip_id='')

