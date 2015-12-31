# List all the of appliances that you can use for creating a server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server_appliances = client.list_appliances()

# Retrieve a specific appliance
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server_appliance = client.get_appliance(appliance_id='')
