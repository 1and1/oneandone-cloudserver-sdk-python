import os
import re
import json
import unittest
import responses

from oneandone.client import OneAndOneService


class TestRecoveryAppliance(unittest.TestCase):
    def setUp(self):
        self.client = OneAndOneService('USER-API-KEY')

    @responses.activate
    def test_list_recovery_appliances(self):
        with open('mock-api/list-recovery-appliances.json') as f:
            data = json.load(f)

        appliance_name = data[0]['name']

        responses.add(responses.GET,
                      'https://cloudpanel-api.1and1.com/v1/recovery_appliances',
                      body=json.dumps(data), status=200,
                      content_type="application/json")

        r = self.client.list_recovery_images()

        self.assertEqual(r[0]['name'], appliance_name)

    @responses.activate
    def test_get_recovery_appliances(self):
        with open('mock-api/get-recovery-appliance.json') as f:
            data = json.load(f)

        appliance_id = data['id']

        responses.add(responses.GET,
                      'https://cloudpanel-api.1and1.com/v1/recovery_appliances/%s' % appliance_id,
                      body=json.dumps(data), status=200,
                      content_type="application/json")

        r = self.client.get_recovery_image(image_id=appliance_id)

        self.assertEqual(r['id'], appliance_id)


if __name__ == '__main__':
    unittest.main()
