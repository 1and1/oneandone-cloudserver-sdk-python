# List all logs
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

logs = client.list_logs(period='LAST_24H')

# Retrieve a log
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

log = client.get_log(log_id='')
