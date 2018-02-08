# List all of the images available for recovering purposes
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

recovery_appliances = client.list_recovery_images()

# Retrieve a specific appliance
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

recovery_appliance = client.get_recovery_image(image_id='')
