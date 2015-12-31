# List all shared storages
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

storages = client.list_shared_storages()

# Retrieve a single shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

storage = client.get_shared_storage(shared_storage_id='')

# List all servers attached to a shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

servers = client.list_servers_attached_storage(shared_storage_id='')

# Retrieve a server attached to a shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server = client.get_shared_storage_server(shared_storage_id='', server_id='')

# Retrieve shared storage credentials
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

credentials = client.get_credentials()

# Create a shared storage
from oneandone.client import OneAndOneService
from oneandone.client import SharedStorage

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

storage1 = SharedStorage(name='Test Storage',
                         description='Test Description',
                         size=50
                         )

new_storage = client.create_shared_storage(shared_storage=storage1)

# Attach servers to a shared storage
from oneandone.client import OneAndOneService
from oneandone.client import AttachServer

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server1 = AttachServer(server_id='', rights='R')
server2 = AttachServer(server_id='', rights='RW')

servers = [server1, server2]

response = client.attach_server_shared_storage(shared_storage_id='',
		server_ids=servers)

# Modify a shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_storage = client.modify_shared_storage(shared_storage_id='',
                                                name='New Name',
                                                description='New Description',
                                                size=100
                                                )

# Change the password for accessing a shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.change_password(password='')

# Delete a shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_shared_storage(shared_storage_id='')

# Detach a server from a shared storage
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.detach_server_shared_storage(shared_storage_id='',
		server_id='')
