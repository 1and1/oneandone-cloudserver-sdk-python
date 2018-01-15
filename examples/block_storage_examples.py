# Create a block storage
from oneandone.client import OneAndOneService, BlockStorage

client = OneAndOneService('<API-TOKEN>')

block_storage = BlockStorage(name='My new block storage',
                             description='My block storage description',
                             size=20,
                             datacenter_id='908DC2072407C94C8054610AD5A53B8C')

response = client.create_block_storage(block_storage)

# List all block storages
from oneandone.client import OneAndOneService, BlockStorage

client = OneAndOneService('<API-TOKEN>')

response = client.list_block_storages()

# Retrieve a single block storage
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')

response = client.get_block_storage(block_storage_id='')

# Modify a block storage
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')

response = client.modify_block_storage(block_storage_id='',
                                       name='New name',
                                       description='New Description')

# Attach a server to a block storage
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')

response = client.attach_server_block_storage(block_storage_id='', server_id='')

# Retrieve a server attached to a block storage
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')

response = client.get_block_storage_server(block_storage_id='')

# Detach a server from a block storage
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')

response = client.detach_server_block_storage(block_storage_id='')

# Delete a block storage
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')

response = client.delete_block_storage(block_storage_id='')