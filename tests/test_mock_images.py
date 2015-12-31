import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService
from oneandone.client import Image

class TestImage(unittest.TestCase):

	def setUp(self):
		self.client = OneAndOneService('<USER-API-KEY>')

	@responses.activate
	def test_list_images(self):
		
		with open('mock-api/list-images.json') as f:
			data = json.load(f)

		test_id = data[0]['id']

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/images',
					  body=json.dumps(data), status=200,
					  content_type="application/json")

		r = self.client.list_images()

		self.assertEqual(r[0]['id'], test_id)

	@responses.activate
	def test_get_image(self):

		with open('mock-api/get-image.json') as f:
			data = json.load(f)
		
		image_id = data["id"]

		responses.add(responses.GET, 'https://cloudpanel-api.1and1.com/v1/images/%s' % image_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")
		
		r = self.client.get_image(image_id=image_id)

		self.assertEqual(r['id'], image_id)

	@responses.activate
	def test_edit_image(self):

		with open('mock-api/edit-image.json') as f:
			data = json.load(f)

		image_id = data['id']
		name = data['name']
		description = data['description']
		frequency = data['frequency']
		
		responses.add(responses.PUT, 'https://cloudpanel-api.1and1.com/v1/images/%s' % image_id,
					  body=json.dumps(data), status=200,
					  content_type="application/json")
		
		r = self.client.modify_image(image_id=image_id, description=description)

		self.assertEqual(r['name'], name)
		self.assertEqual(r['description'], description)
		self.assertEqual(r['frequency'], frequency)

	@responses.activate
	def test_create_image(self):
		
		with open('mock-api/create-image.json') as f:
			data = json.load(f)

		image1 = Image(server_id=data['server_id'], name=data['name'],
				description='Test Description', frequency=data['frequency'],
				num_images=data['num_images'])

		responses.add(responses.POST, 'https://cloudpanel-api.1and1.com/v1/images',
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.create_image(image=image1)

		self.assertEqual(r['server_id'], image1.server_id)
		self.assertEqual(r['name'], image1.name)
		self.assertEqual(r['frequency'], image1.frequency)
		self.assertEqual(r['num_images'], image1.num_images)

	@responses.activate
	def test_delete_image(self):
		
		with open('mock-api/delete-image.json') as f:
			data = json.load(f)

		image_id = data['id']

		responses.add(responses.DELETE, 'https://cloudpanel-api.1and1.com/v1/images/%s' % image_id,
					  body=json.dumps(data), status=202,
					  content_type="application/json")

		r = self.client.delete_image(image_id=image_id)

		self.assertEqual(r['state'], 'REMOVING')

if __name__ == '__main__':
	unittest.main()