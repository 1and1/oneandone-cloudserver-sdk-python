# List all images
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

images = client.list_images()

# Retrieve an image
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

image = client.get_image(image_id='')

# Create an image
from oneandone.client import OneAndOneService
from oneandone.client import Image

client = OneAndOneService('API-TOKEN')

image1 = Image(server_id='',
               name='Test Image',
               description='Test Description',
               frequency='WEEKLY',
               num_images=1
               )

new_image = client.create_image(image=image1)

# Modify an image
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

modified_image = client.modify_image(image_id='',
                                     name='New Image Name',
                                     description='New Description',
                                     frequency='ONCE'
                                     )

# Delete an image
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')

response = client.delete_image(image_id='')
