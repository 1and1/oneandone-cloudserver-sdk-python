# List all usages and alerts of monitoring servers
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

usages = client.list_server_usages()

# Retrieve the usages and alerts for a monitoring server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

usage = client.get_usage(server_id='', period='LAST_24H')
