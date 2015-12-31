# List all DVDs
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

dvds = client.list_dvds()

# Retrieve a DVD
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

dvd = client.get_dvd(iso_id='')
