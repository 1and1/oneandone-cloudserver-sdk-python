# List all usages
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

usages = client.list_usages(period='LAST_24H')
