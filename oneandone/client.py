import requests
import urllib
import json
import time

# 1and1 Object Classes


class OneAndOneService(object):

    # Init Function
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.header = {'X-TOKEN': self.api_token}
        self.success_codes = (200, 201, 202)

    def __repr__(self):
        return 'OneAndOneService: api_token=%s, base_url=%s' % (self.api_token,
                self.base_url)

    # Server Functions

    # 'GET' methods

    def list_servers(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/servers' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def fixed_server_flavors(self):

        # Perform Request
        url = '%s/servers/fixed_instance_sizes' % self.base_url

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_fixed_server(self, fixed_server_id=None):

        # Error Handling
        if(fixed_server_id == None):
            raise ValueError('fixed_server_id is a required parameter')

        # Perform Request
        url = ('%s/servers/fixed_instance_sizes/%s' %
            (self.base_url, fixed_server_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server_hardware(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/hardware' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_server_hdds(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/hardware/hdds' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server_hdd(self, server_id=None, hdd_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(hdd_id == None):
            raise ValueError('hdd_id is a required parameter')

        # Perform Request
        url = ('%s/servers/%s/hardware/hdds/%s' %
            (self.base_url, server_id, hdd_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server_image(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/image' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_server_ips(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/ips' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server_ip(self, server_id=None, ip_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/ips/%s' % (self.base_url, server_id, ip_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_ip_firewall_policy(self, server_id=None, ip_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        url = ('%s/servers/%s/ips/%s/firewall_policy' %
            (self.base_url, server_id, ip_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_ip_load_balancers(self, server_id=None, ip_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        url = ('%s/servers/%s/ips/%s/load_balancers' %
            (self.base_url, server_id, ip_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server_status(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/status' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_server_dvd(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/dvd' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_server_private_networks(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/private_networks' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def private_network_info(self, server_id=None, private_network_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')

        # Perform Request
        url = ('%s/servers/%s/private_networks/%s' %
            (self.base_url, server_id, private_network_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_server_snapshots(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = '%s/servers/%s/snapshots' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' methods

    def modify_server(self, server_id=None, name=None, description=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(name == None):
            raise ValueError('name is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'description': description
        }

        url = '%s/servers/%s' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_server_hardware(self, server_id=None,
            fixed_instance_size_id=None, vcore=None, cores_per_processor=None,
            ram=None, test=False):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Use 'test' flag to skip this block when running unit test
        if(test == False):

            # Prevent hot decreasing of server hardware, allow cold decreasing.
            server_specs = self.get_server_hardware(server_id=server_id)

            server_status = self.get_server_status(server_id=server_id)

            if(server_status['state'] == 'POWERED_ON'):
                if(vcore != None):
                    if(server_specs['vcore'] > vcore):
                        raise ValueError(('Cannot perform a hot decrease of '
                                          'server CPU.  The new value must be '
                                          'greater than current value.'))
                if(ram != None):
                    if(server_specs['ram'] > ram):
                        raise ValueError(('Cannot perform a hot decrease of '
                                          'server RAM.  The new value must be '
                                          'greater than current value.'))

        # Perform Request
        data = {
            'fixed_instance_size_id': fixed_instance_size_id,
            'vcore': vcore,
            'cores_per_processor': cores_per_processor,
            'ram': ram
        }

        url = '%s/servers/%s/hardware' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_hdd(self, server_id=None, hdd_id=None, size=None, test=False):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(hdd_id == None):
            raise ValueError('hdd_id is a required parameter')

        # Use 'test' flag to skip this block when running unit test
        if(test == False):

            # Make sure size argument is valid.  HDD size can't be decreased.
            old_hdd = self.get_server_hdd(server_id=server_id, hdd_id=hdd_id)

            if(size != None):
                if(old_hdd['size'] > size):
                    raise ValueError('HDD size can never be decreased. '
                                     'Must be greater than or equal to the '
                                     'current HDD size.')

        # Perform Request
        data = {'size': size}

        url = ('%s/servers/%s/hardware/hdds/%s' %
            (self.base_url, server_id, hdd_id))

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def add_firewall_policy(self, server_id=None, ip_id=None, firewall_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')

        # Perform Request
        data = {'id': firewall_id}

        url = ('%s/servers/%s/ips/%s/firewall_policy' %
            (self.base_url, server_id, ip_id))

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_server_status(self, server_id=None, action=None, method='SOFTWARE'):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(action == None):
            raise ValueError('action is a required parameter')

        # Make sure user is passing in correct arguments
        if(action != 'POWER_ON' and action != 'POWER_OFF' and
                action != 'REBOOT'):
            raise ValueError(('action must be set to "POWER_ON",'
                              '"POWER_OFF", or "REBOOT".'))

        if(method != 'HARDWARE' and method != 'SOFTWARE'):
            raise ValueError(('method must be set to either '
                              '"HARDWARE" or "SOFTWARE".'))

        # Perform Request
        data = {
            'action': action,
            'method': method
        }

        url = '%s/servers/%s/status/action' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def stop_server(self, server_id=None, method='SOFTWARE'):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Make sure user is passing in correct arguments
        if(method != 'HARDWARE' and method != 'SOFTWARE'):
            raise ValueError(('method must be set to either '
                              '"HARDWARE" or "SOFTWARE".'))

        # Perform Request
        data = {
            'action': 'POWER_OFF',
            'method': method
        }

        url = '%s/servers/%s/status/action' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def start_server(self, server_id=None, method='SOFTWARE'):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Make sure user is passing in correct arguments
        if(method != 'HARDWARE' and method != 'SOFTWARE'):
            raise ValueError(('method must be set to either '
                              '"HARDWARE" or "SOFTWARE".'))

        # Perform Request
        data = {
            'action': 'POWER_ON',
            'method': method
        }

        url = '%s/servers/%s/status/action' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def load_dvd(self, server_id=None, dvd_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(dvd_id == None):
            raise ValueError('dvd_id is a required parameter')

        # Perform Request
        data = {'id': dvd_id}

        url = '%s/servers/%s/dvd' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def restore_snapshot(self, server_id=None, snapshot_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(snapshot_id == None):
            raise ValueError('snapshot_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/servers/%s/snapshots/%s' %
            (self.base_url, server_id, snapshot_id))

        r = requests.put(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def reinstall_image(self, server_id=None, image_id=None, password=None,
            firewall_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(image_id == None):
            raise ValueError('image_id is a required parameter')

        # Create firewall object, if necessary
        firewall_policy = {'id': firewall_id}

        # Perform Request
        data = {
            'id': image_id,
            'password': password,
            'firewall_policy': firewall_policy
        }

        url = '%s/servers/%s/image' % (self.base_url, server_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' methods

    def delete_server(self, server_id=None, keep_ips=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'
        parameters = {'keep_ips': keep_ips}

        url = '%s/servers/%s' % (self.base_url, server_id)

        r = requests.delete(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_hdd(self, server_id=None, hdd_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(hdd_id == None):
            raise ValueError('hdd_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/servers/%s/hardware/hdds/%s' %
            (self.base_url, server_id, hdd_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_ip(self, server_id=None, ip_id=None, keep_ip=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'
        parameters = {'keep_ip': keep_ip}

        url = '%s/servers/%s/ips/%s' % (self.base_url, server_id, ip_id)

        r = requests.delete(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_firewall_policy(self, server_id=None, ip_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/servers/%s/ips/%s/firewall_policy' %
            (self.base_url, server_id, ip_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_load_balancer(self, server_id=None, ip_id=None,
            load_balancer_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/servers/%s/ips/%s/load_balancers/%s' %
            (self.base_url, server_id, ip_id, load_balancer_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_private_network(self, server_id=None, private_network_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/servers/%s/private_networks/%s' %
            (self.base_url, server_id, private_network_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def eject_dvd(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/servers/%s/dvd' % (self.base_url, server_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def delete_snapshot(self, server_id=None, snapshot_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(snapshot_id == None):
            raise ValueError('snapshot_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/servers/%s/snapshots/%s' %
            (self.base_url, server_id, snapshot_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' methods

    def add_new_ip(self, server_id=None, ip_type=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_type != None) and (ip_type != 'IPV4'):
            raise ValueError(("ip_type.  Only type 'IPV4' is currently "
                              "supported."))

        # Perform Request
        data = {'type': ip_type}

        url = '%s/servers/%s/ips' % (self.base_url, server_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def add_load_balancer(self, server_id=None, ip_id=None,
            load_balancer_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        # Perform Request
        data = {'load_balancer_id': load_balancer_id}

        url = ('%s/servers/%s/ips/%s/load_balancers' %
            (self.base_url, server_id, ip_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def assign_private_network(self, server_id=None, private_network_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')

        # Perform Request
        data = {'id': private_network_id}

        url = '%s/servers/%s/private_networks' % (self.base_url, server_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def create_snapshot(self, server_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/servers/%s/snapshots' % (self.base_url, server_id)

        r = requests.post(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def clone_server(self, server_id=None, name=None, datacenter_id=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(name == None):
            raise ValueError('name is a required parameter')

        # Perform Request
        data = {
                'name': name,
                'datacenter_id': datacenter_id
        }

        url = '%s/servers/%s/clone' % (self.base_url, server_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def create_server(self, server=None, hdds=None):

        # Error Handling
        if(server == None):
            raise ValueError(('server is a required parameter. Make '
                              'sure you pass a Server object.'))

        # Unpack hdds
        if hdds:
            hdd = []

            for value in hdds:
                hdd.append(value.specs)

            # Add hdds to server object
            server.specs['hardware']['hdds'] = hdd

        # Clean dictionary
        for key, value in server.specs['hardware'].items():
            if value == None:
                del server.specs['hardware'][key]

        # Build URL and perform request
        url = '%s/servers' % self.base_url

        r = requests.post(url, headers=self.header, json=server.specs)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new server_id back to calling Server object
        response = r.json()

        server.specs.update(server_id=response['id'])
        server.specs.update(api_token=self.header)
        server.first_password = response['first_password']

        return r.json()

    def add_hdd(self, server_id=None, hdds=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(hdds == None):
            raise ValueError(('hdds is a required parameter.  Make '
                              'sure you pass a list with at least '
                              'one Hdd object.'))

        # Unpack hdds
        hdd = []

        for value in hdds:
            hdd.append(value.specs)

        # Perform Request
        data = {'hdds': hdd}

        url = '%s/servers/%s/hardware/hdds' % (self.base_url, server_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Image Functions

    # 'GET' Methods

    def list_images(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/images' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_image(self, image_id=None):

        # Error Handling
        if(image_id == None):
            raise ValueError('image_id is a required parameter')

        # Perform Request

        url = '%s/images/%s' % (self.base_url, image_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_image(self, image=None):

        # Error Handling
        if(image.server_id == None):
            raise ValueError('server_id is a required parameter')
        if(image.name == None):
            raise ValueError('name is a required parameter')
        if(image.frequency == None):
            raise ValueError('frequency is a required parameter')
        if(image.num_images == None):
            raise ValueError('num_images is a required parameter')

        # Perform Request
        data = {
            'server_id': image.server_id,
            'name': image.name,
            'frequency': image.frequency,
            'num_images': image.num_images,
            'description': image.description
        }

        url = '%s/images' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new image_id back to calling Image object
        response = r.json()

        image.specs.update(image_id=response['id'])
        image.specs.update(api_token=self.header)

        return r.json()

    # 'DELETE' Methods

    def delete_image(self, image_id=None):

        # Error Handling
        if(image_id == None):
            raise ValueError('image_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/images/%s' % (self.base_url, image_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_image(self, image_id=None, name=None, description=None,
            frequency=None):

        # Error Handling
        if(image_id == None):
            raise ValueError('image_id is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'frequency': frequency,
            'description': description
        }

        url = '%s/images/%s' % (self.base_url, image_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Shared Storage Functions

    # 'GET' Methods

    def list_shared_storages(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/shared_storages' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_shared_storage(self, shared_storage_id=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id is a required parameter')

        # Perform Request
        url = '%s/shared_storages/%s' % (self.base_url, shared_storage_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_servers_attached_storage(self, shared_storage_id=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id is a required parameter')

        # Perform Request
        url = ('%s/shared_storages/%s/servers' %
            (self.base_url, shared_storage_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_shared_storage_server(self, shared_storage_id=None, server_id=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id parameter is required')
        if(server_id == None):
            raise ValueError('server_id parameter is required')

        # Perform Request
        url = ('%s/shared_storages/%s/servers/%s' %
            (self.base_url, shared_storage_id, server_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_credentials(self):

        # Perform Request
        url = '%s/shared_storages/access' % self.base_url

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_shared_storage(self, shared_storage=None):

        # Error Handling
        if(shared_storage.name == None):
            raise ValueError('name is a required parameter')
        if(shared_storage.size == None):
            raise ValueError('size is a required parameter')

        # Perform Request
        data = {
            'name': shared_storage.name,
            'description': shared_storage.description,
            'size': shared_storage.size,
            'datacenter_id': shared_storage.datacenter_id
        }

        url = '%s/shared_storages' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new shared_storage_id back to calling SharedStorage object
        response = r.json()

        shared_storage.specs.update(shared_storage_id=response['id'])
        shared_storage.specs.update(api_token=self.header)

        return r.json()

    def attach_server_shared_storage(self, shared_storage_id=None,
            server_ids=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id is a required parameter')
        if(server_ids == None):
            raise ValueError(('server_ids is a required parameter.  '
                              'Must attach at least one server'))

        # Unpack servers
        servers = []

        for value in server_ids:
            servers.append({'id': value.server_id, 'rights': value.rights})

        # Perform Request
        data = {'servers': servers}

        url = ('%s/shared_storages/%s/servers' %
            (self.base_url, shared_storage_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_shared_storage(self, shared_storage_id=None, name=None,
            description=None, size=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'description': description,
            'size': size
        }

        url = '%s/shared_storages/%s' % (self.base_url, shared_storage_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def change_password(self, password=None):

        # Error Handlong
        if(password == None):
            raise ValueError(('password is a required parameter. '
                              'password must contain at least 8 characters.'))

        # Perform Request
        data = {'password': password}

        url = '%s/shared_storages/access' % self.base_url

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_shared_storage(self, shared_storage_id=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/shared_storages/%s' % (self.base_url, shared_storage_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def detach_server_shared_storage(self, shared_storage_id=None,
            server_id=None):

        # Error Handling
        if(shared_storage_id == None):
            raise ValueError('shared_storage_id is a required parameter')
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/shared_storages/%s/servers/%s' %
            (self.base_url, shared_storage_id, server_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Firewall Policy Functions

    # 'GET' Methods

    def list_firewall_policies(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/firewall_policies' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_firewall(self, firewall_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')

        # Perform Request
        url = '%s/firewall_policies/%s' % (self.base_url, firewall_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_firewall_servers(self, firewall_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')

        # Perform Request
        url = ('%s/firewall_policies/%s/server_ips' %
            (self.base_url, firewall_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_firewall_server(self, firewall_id=None, server_ip_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')
        if(server_ip_id == None):
            raise ValueError('server_ip_id is a required parameter')

        # Perform Request
        url = ('%s/firewall_policies/%s/server_ips/%s' %
            (self.base_url, firewall_id, server_ip_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_firewall_policy_rules(self, firewall_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')

        # Perform Request
        url = '%s/firewall_policies/%s/rules' % (self.base_url, firewall_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_firewall_policy_rule(self, firewall_id=None, rule_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')
        if(rule_id == None):
            raise ValueError('rule_id is a required parameter')

        # Perform Request
        url = ('%s/firewall_policies/%s/rules/%s' %
            (self.base_url, firewall_id, rule_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_firewall(self, firewall_id=None, name=None, description=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'description': description
        }

        url = '%s/firewall_policies/%s' % (self.base_url, firewall_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_firewall_policy(self, firewall_policy=None,
            firewall_policy_rules=None):

        # Error Handling
        if(firewall_policy.specs['name'] == None):
            raise ValueError(('Policy name is required.  Make sure your '
                              'FirewallPolicy object was initialized with '
                              'a name parameter'))
        if(firewall_policy_rules == None):
            raise ValueError(('firewall_policy_rules is required.  Make sure '
                              'you pass a list with at least one '
                              'FirewallPolicyRule object.'))

        # Unpack Rules
        rules = []

        for value in firewall_policy_rules:
            rules.append(value.rule_set)


        # Attach rules and Perform Request
        firewall_policy.specs['rules'] = rules

        url = '%s/firewall_policies' % self.base_url

        r = requests.post(url, headers=self.header, json=firewall_policy.specs)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new firewall_id back to calling FirewallPolicy object
        response = r.json()

        firewall_policy.specs.update(firewall_id=response['id'])
        firewall_policy.specs.update(api_token=self.header)

        return r.json()

    def add_firewall_policy_rule(self, firewall_id=None,
            firewall_policy_rules=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')
        if(firewall_policy_rules == None):
            raise ValueError(('firewall_policy_rules is required.  Make '
                              'sure you pass a list with at least one '
                              'FirewallPolicyRule object'))

        # Unpack rules
        rules = []

        for value in firewall_policy_rules:
            rules.append(value.rule_set)

        # Perform Request
        data = {'rules': rules}

        url = '%s/firewall_policies/%s/rules' % (self.base_url, firewall_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def attach_server_firewall_policy(self, firewall_id=None, server_ips=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')
        if(server_ips == None):
            raise ValueError(('server_ips is required. Make sure you pass '
                              'a list with at least one AttachServer object'))

        # Unpack servers
        servers = []

        for value in server_ips:
            servers.append(value.server_ip_id)

        # Perform Request
        data = {'server_ips': servers}

        url = ('%s/firewall_policies/%s/server_ips' %
            (self.base_url, firewall_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_firewall(self, firewall_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/firewall_policies/%s' % (self.base_url, firewall_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_firewall_rule(self, firewall_id=None, rule_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')
        if(rule_id == None):
            raise ValueError('rule_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/firewall_policies/%s/rules/%s' %
            (self.base_url, firewall_id, rule_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_firewall_server(self, firewall_id=None, server_ip_id=None):

        # Error Handling
        if(firewall_id == None):
            raise ValueError('firewall_id is a required parameter')
        if(server_ip_id == None):
            raise ValueError('server_ip_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/firewall_policies/%s/server_ips/%s' %
            (self.base_url, firewall_id, server_ip_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Load Balancer Functions

    # 'GET' Methods

    def list_load_balancers(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/load_balancers' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_load_balancer(self, load_balancer_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        # Perform Request
        url = '%s/load_balancers/%s' % (self.base_url, load_balancer_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_load_balancer_servers(self, load_balancer_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        # Perform Request
        url = ('%s/load_balancers/%s/server_ips' %
            (self.base_url, load_balancer_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_load_balancer_server(self, load_balancer_id=None,
            server_ip_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')
        if(server_ip_id == None):
            raise ValueError('server_ip_id is a required parameter')

        # Perform Request
        url = ('%s/load_balancers/%s/server_ips/%s' %
            (self.base_url, load_balancer_id, server_ip_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def load_balancer_rules(self, load_balancer_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        # Perform Request
        url = '%s/load_balancers/%s/rules' % (self.base_url, load_balancer_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_load_balancer_rule(self, load_balancer_id=None, rule_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')
        if(rule_id == None):
            raise ValueError('rule_id is a required parameter')

        # Perform Request
        url = ('%s/load_balancers/%s/rules/%s' %
            (self.base_url, load_balancer_id, rule_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_load_balancer(self, load_balancer_id=None, name=None,
            description=None, health_check_test=None,
            health_check_interval=None, health_check_path=None,
            health_check_parse=None, persistence=None, persistence_time=None,
            method=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        if(method != None and method != 'ROUND_ROBIN' and
                   method != 'LEAST_CONNECTIONS'):
            raise ValueError(('method must be set to either "ROUND_ROBIN" '
                              'or "LEAST_CONNECTIONS".'))

        if(health_check_test != None and health_check_test != 'TCP'):
            raise ValueError(('health_check_test must be set to "TCP". '
                              '"HTTP" is not currently supported.'))

        if(health_check_interval < 5 and health_check_interval > 300):
            raise ValueError(('health_check_interval must be an integer '
                              'between 5 and 300.'))

        if(persistence_time < 30 and persistence_time > 1200):
            raise ValueError(('persistence_time must be an integer '
                              'between 30 and 1200.'))

        # Perform Request
        data = {
            'name': name,
            'description': description,
            'health_check_test': health_check_test,
            'health_check_interval': health_check_interval,
            'health_check_path': health_check_path,
            'health_check_parse': health_check_parse,
            'persistence': persistence,
            'persistence_time': persistence_time,
            'method': method
        }

        url = '%s/load_balancers/%s' % (self.base_url, load_balancer_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_load_balancer(self, load_balancer=None,
            load_balancer_rules=None):

        # Error Handling
        if(load_balancer == None):
            raise ValueError(('load_balancer parameter is required.  Must '
                              'pass a LoadBalancer object.'))
        if(load_balancer_rules == None):
            raise ValueError(('load_balancer_rules parameter is required. '
                              'Must pass a list with at least one '
                              'LoadBalancerRule object.'))
        if(load_balancer.specs['method'] != None and
                load_balancer.specs['method'] != 'ROUND_ROBIN' and
                load_balancer.specs['method'] != 'LEAST_CONNECTIONS'):
            raise ValueError(('method must be set to either "ROUND_ROBIN" '
                              'or "LEAST_CONNECTIONS".'))

        # Unpack rules
        rules = []

        for value in load_balancer_rules:
            rules.append(value.rule_set)

        # Perform Request
        load_balancer.specs['rules'] = rules

        url = '%s/load_balancers' % self.base_url

        r = requests.post(url, headers=self.header, json=load_balancer.specs)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new load_balancer_id back to calling LoadBalancer object
        response = r.json()

        load_balancer.specs.update(load_balancer_id=response['id'])
        load_balancer.specs.update(api_token=self.header)

        return r.json()

    def attach_load_balancer_server(self, load_balancer_id=None,
            server_ips=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter.')
        if(server_ips == None):
            raise ValueError(('server_ips is a required parameter. Must '
                              'pass a list with at least one AttachServer '
                              'object'))

        # Unpack servers
        servers = []

        for value in server_ips:
            servers.append(value.server_ip_id)

        # Perform Request
        data = {'server_ips': servers}

        url = ('%s/load_balancers/%s/server_ips' %
            (self.base_url, load_balancer_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def add_load_balancer_rule(self, load_balancer_id=None,
            load_balancer_rules=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter.')
        if(load_balancer_rules == None):
            raise ValueError(('load_balancer_rules is a required '
                              'parameter. Must pass a list with at least one '
                              'LoadBalancerRule object'))

        # Unpack rules
        rules = []

        for value in load_balancer_rules:
            rules.append(value.rule_set)

        # Perform Request
        data = {'rules': rules}

        url = ('%s/load_balancers/%s/rules' %
            (self.base_url, load_balancer_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_load_balancer(self, load_balancer_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/load_balancers/%s' % (self.base_url, load_balancer_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_load_balancer_server(self, load_balancer_id=None,
            server_ip_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter.')
        if(server_ip_id == None):
            raise ValueError('server_ip_id is a required parameter.')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/load_balancers/%s/server_ips/%s' %
            (self.base_url, load_balancer_id, server_ip_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_load_balancer_rule(self, load_balancer_id=None, rule_id=None):

        # Error Handling
        if(load_balancer_id == None):
            raise ValueError('load_balancer_id is a required parameter.')
        if(rule_id == None):
            raise ValueError('rule_id is a required parameter.')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/load_balancers/%s/rules/%s' %
            (self.base_url, load_balancer_id, rule_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Public IP Functions

    # 'GET' Methods

    def list_public_ips(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/public_ips' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_public_ip(self, ip_id=None):

        # Error Handling
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        url = '%s/public_ips/%s' % (self.base_url, ip_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_public_ip(self, reverse_dns=None, ip_type=None,
            datacenter_id=None):

        # Error Handling
        if(ip_type != 'IPV4' and ip_type != None):
            raise ValueError('ip_type must be set to "IPV4".')

        # Perform Request
        data = {
            'reverse_dns': reverse_dns,
            'type': ip_type,
            'datacenter_id': datacenter_id
        }

        url = '%s/public_ips' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_public_ip(self, ip_id=None, reverse_dns=None):

        # Error Handling
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        data = {'reverse_dns': reverse_dns}

        url = '%s/public_ips/%s' % (self.base_url, ip_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_public_ip(self, ip_id=None):

        # Error Handling
        if(ip_id == None):
            raise ValueError('ip_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/public_ips/%s' % (self.base_url, ip_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Private Network Functions

    # 'GET' Methods

    def list_private_networks(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/private_networks' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_private_network(self, private_network_id):

        # Error Handling
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')

        # Perform Request
        url = '%s/private_networks/%s' % (self.base_url, private_network_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_private_network_servers(self, private_network_id=None):

        # Error Handling
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')

        # Perform Request
        url = ('%s/private_networks/%s/servers' %
            (self.base_url, private_network_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_private_network_server(self, private_network_id=None,
            server_id=None):

        # Error Handling
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = ('%s/private_networks/%s/servers/%s' %
            (self.base_url, private_network_id, server_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_private_network(self, private_network=None):

        # Error Handling
        if(private_network.name == None):
            raise ValueError('name is a required parameter')

        # Perform Request
        data = {
            'name': private_network.name,
            'description': private_network.description,
            'network_address': private_network.network_address,
            'subnet_mask': private_network.subnet_mask,
            'datacenter_id': private_network.datacenter_id
        }

        url = '%s/private_networks' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new private_network_id back to calling PrivateNetwork object
        response = r.json()

        private_network.specs.update(private_network_id=response['id'])
        private_network.specs.update(api_token=self.header)

        return r.json()

    def attach_private_network_servers(self, private_network_id=None,
            server_ids=None):

        # Error Handling
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')
        if(server_ids == None):
            raise ValueError(('server_ids is a required parameter.  Make '
                              'sure you pass a list with at least one '
                              'server_id string'))

        # Unpack servers
        servers = []

        for value in server_ids:
            servers.append(value.server_id)

        # Perform Request
        data = {'servers': servers}

        url = ('%s/private_networks/%s/servers' %
            (self.base_url, private_network_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_private_network(self, private_network_id=None, name=None,
            description=None, network_address=None, subnet_mask=None):

        # Perform Request
        data = {
            'name': name,
            'description': description,
            'network_address': network_address,
            'subnet_mask': subnet_mask
        }

        url = '%s/private_networks/%s' % (self.base_url, private_network_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_private_network(self, private_network_id=None):

        # Error Handling
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/private_networks/%s' % (self.base_url, private_network_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_private_network_server(self, private_network_id=None,
            server_id=None):

        # Error Handling
        if(private_network_id == None):
            raise ValueError('private_network_id is a required parameter')
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/private_networks/%s/servers/%s' %
            (self.base_url, private_network_id, server_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Monitoring Center Functions

    # 'GET' Methods

    def list_server_usages(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/monitoring_center' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_usage(self, server_id=None, period='LAST_24H',
            start_date=None, end_date=None):

        # Error Handling
        if(server_id == None):
            raise ValueError('server_id is a required parameter')
        if(period == 'CUSTOM'):
            if(start_date == None):
                raise ValueError(('start_date parameter is required when '
                                  'using CUSTOM period'))
            if(end_date == None):
                raise ValueError(('end_date parameter is required when '
                                  'using CUSTOM period'))

        # Perform Request
        parameters = {
            'period': period,
            'start_date': start_date,
            'end_date': end_date
        }

        url = '%s/monitoring_center/%s' % (self.base_url, server_id)

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Monitoring Policy Functions

    # 'GET' Methods

    def list_monitoring_policies(self, page=None, per_page=None,
            sort=None, q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/monitoring_policies' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_monitoring_policy(self, monitoring_policy_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s' %
            (self.base_url, monitoring_policy_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_monitoring_policy_ports(self, monitoring_policy_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s/ports' %
            (self.base_url, monitoring_policy_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_monitoring_policy_port(self, monitoring_policy_id=None,
            port_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(port_id == None):
            raise ValueError('port_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s/ports/%s' %
            (self.base_url, monitoring_policy_id, port_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_monitoring_policy_processes(self, monitoring_policy_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s/processes' %
            (self.base_url, monitoring_policy_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_monitoring_policy_process(self, monitoring_policy_id=None,
            process_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(process_id == None):
            raise ValueError('process_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s/processes/%s' %
            (self.base_url, monitoring_policy_id, process_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def list_monitoring_policy_servers(self, monitoring_policy_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s/servers' %
            (self.base_url, monitoring_policy_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_monitoring_policy_server(self, monitoring_policy_id=None,
            server_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        url = ('%s/monitoring_policies/%s/servers/%s' %
            (self.base_url, monitoring_policy_id, server_id))

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_monitoring_policy(self, monitoring_policy_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/monitoring_policies/%s' %
            (self.base_url, monitoring_policy_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def delete_monitoring_policy_port(self, monitoring_policy_id=None,
            port_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(port_id == None):
            raise ValueError('port_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/monitoring_policies/%s/ports/%s' %
            (self.base_url, monitoring_policy_id, port_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def delete_monitoring_policy_process(self, monitoring_policy_id=None,
            process_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(process_id == None):
            raise ValueError('process_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/monitoring_policies/%s/processes/%s' %
            (self.base_url, monitoring_policy_id, process_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def detach_monitoring_policy_server(self, monitoring_policy_id=None,
            server_id=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(server_id == None):
            raise ValueError('server_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = ('%s/monitoring_policies/%s/servers/%s' %
            (self.base_url, monitoring_policy_id, server_id))

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_monitoring_policy(self, monitoring_policy=None,
            thresholds=None, ports=None, processes=None):

        # Error Handling
        if(monitoring_policy == None):
            raise ValueError(('monitoring_policy is a required parameter. '
                              'Make sure you pass a MonitoringPolicy object.'))
        if(thresholds == None):
            raise ValueError(('thresholds is a required parameter.  Make '
                              'sure you pass a list with all 5 Threshold '
                              'objects(cpu, ram, disk, transfer, '
                              'internal_ping).'))
        if(ports == None):
            raise ValueError(('ports is a required parameter.  Make sure '
                              'you pass a list with at least one Port object.'))
        if(processes == None):
            raise ValueError(('processes is a required parameter.  Make '
                              'sure you pass a list with at least one '
                              'Process object.'))

        # Unpack Thresholds
        new_thresholds = {}

        for value in thresholds:
            new_thresholds[value.entity] = {
                'warning': {
                    'value': value.warning_value,
                    'alert': value.warning_alert
                },
                'critical': {
                    'value': value.critical_value,
                    'alert': value.critical_alert
                }
            }

        # Unpack Ports
        new_ports = []

        for value in ports:
            new_ports.append(value.specs)

        # Unpack Processes
        new_processes = []

        for value in processes:
            new_processes.append(value.process_set)

        # Add Ports, Processes, and Thresholds to Monitoring Policy object
        monitoring_policy.specs['thresholds'] = new_thresholds
        monitoring_policy.specs['ports'] = new_ports
        monitoring_policy.specs['processes'] = new_processes

        # Perform Request
        url = '%s/monitoring_policies' % self.base_url

        r = requests.post(url, headers=self.header,
                json=monitoring_policy.specs)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new monitoring_policy_id back to calling MonitoringPolicy object
        response = r.json()

        monitoring_policy.specs.update(monitoring_policy_id=response['id'])
        monitoring_policy.specs.update(api_token=self.header)

        return r.json()

    def add_port(self, monitoring_policy_id=None, ports=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(ports == None):
            raise ValueError(('ports is a required parameter. Make sure you '
                              'send in a list with at least one Port object'))

        # Unpack ports
        new_ports = []

        for value in ports:
            new_ports.append(value.specs)

        # Perform Request
        data = {'ports': new_ports}

        url = ('%s/monitoring_policies/%s/ports' %
            (self.base_url, monitoring_policy_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def add_process(self, monitoring_policy_id=None, processes=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(processes == None):
            raise ValueError(('processes is a required parameter. Make '
                              'sure you send in a list with at least one '
                              'Process object'))

        # Unpack processes
        new_processes = []

        for value in processes:
            new_processes.append(value.process_set)

        # Perform Request
        data = {'processes': new_processes}

        url = ('%s/monitoring_policies/%s/processes' %
            (self.base_url, monitoring_policy_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def attach_monitoring_policy_server(self, monitoring_policy_id=None,
            servers=None):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(servers == None):
            raise ValueError(('servers is a required parameter. Make sure '
                              'you send in a list with at least one '
                              'AttachServer object'))

        # Unpack servers
        add_servers = []

        for value in servers:
            add_servers.append(value.server_id)

        # Perform Request
        data = {'servers': add_servers}

        url = ('%s/monitoring_policies/%s/servers' %
            (self.base_url, monitoring_policy_id))

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_monitoring_policy(self, monitoring_policy_id=None,
            monitoring_policy=None, thresholds=None, test=False):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')

        # Use flag to skip this live API call when running unit test
        if(test == False):
            # Make request for existing monitoring policy object
            json = self.get_monitoring_policy(
                    monitoring_policy_id=monitoring_policy_id)

            # Update policy specs with new values, if necessary.
            if(monitoring_policy):
                if(json['name'] != monitoring_policy.specs['name']):
                    if(monitoring_policy.specs['name'] != None):
                        json['name'] = monitoring_policy.specs['name']

                if(json['description'] !=
                    monitoring_policy.specs['description']):
                    if(monitoring_policy.specs['description'] != None):
                        json['description'] = monitoring_policy.specs['description']

                if(json['email'] != monitoring_policy.specs['email']):
                    if(monitoring_policy.specs['email'] != None):
                        json['email'] = monitoring_policy.specs['email']

            # Unpack thresholds
            if(thresholds):
                new_thresholds = {}

                for value in thresholds:
                    new_thresholds[value.entity] = {
                        'warning': {
                            'value': value.warning_value,
                            'alert': value.warning_alert
                        },
                        'critical': {
                            'value': value.critical_value,
                            'alert': value.critical_alert
                        }
                    }

                # Compare all threshold values and update, if necessary.
                threshold_entities = ['cpu', 'ram', 'disk', 'transfer',
                    'internal_ping']

                for value in threshold_entities:

                    if(value in new_thresholds.keys()):
                        if(json['thresholds'][value]['warning']['value'] !=
                                new_thresholds[value]['warning']['value']):
                            json['thresholds'][value]['warning']['value'] = new_thresholds[value]['warning']['value']

                        if(json['thresholds'][value]['warning']['alert'] !=
                                new_thresholds[value]['warning']['alert']):
                            json['thresholds'][value]['warning']['alert'] = new_thresholds[value]['warning']['alert']

                        if(json['thresholds'][value]['critical']['value'] !=
                                new_thresholds[value]['critical']['value']):
                            json['thresholds'][value]['critical']['value'] = new_thresholds[value]['critical']['value']

                        if(json['thresholds'][value]['critical']['alert'] !=
                                new_thresholds[value]['critical']['alert']):
                            json['thresholds'][value]['critical']['alert'] = new_thresholds[value]['critical']['alert']

            # Perform Request
            data = {
                'name': json['name'],
                'description': json['description'],
                'email': json['email'],
                'thresholds': json['thresholds']
            }

            url = ('%s/monitoring_policies/%s' %
                (self.base_url, monitoring_policy_id))

            r = requests.put(url, headers=self.header, json=data)

        else:
            # Mock Request for Unit Testing
            r = requests.put(self.base_url + '/monitoring_policies/%s' %
                (monitoring_policy_id), headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_port(self, monitoring_policy_id=None, port_id=None, port=None,
            test=False):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(port_id == None):
            raise ValueError('port_id is a required parameter')

        # Use flag to skip this live API call when running unit test
        if(test == False):
            # Make request for existing port object
            json = self.get_monitoring_policy_port(
                monitoring_policy_id=monitoring_policy_id, port_id=port_id)
            del json['id']

            # Update port object with new values, if necessary.
            if(json['alert_if'] != port.specs['alert_if']):
                if(port.specs['alert_if'] != None):
                    json['alert_if'] = port.specs['alert_if']

            if(json['email_notification'] != port.specs['email_notification']):
                if(port.specs['email_notification'] != None):
                    json['email_notification'] = port.specs['email_notification']

            # Perform Request
            data = {'ports': json}

            url = ('%s/monitoring_policies/%s/ports/%s' %
                (self.base_url, monitoring_policy_id, port_id))

            r = requests.put(url, headers=self.header, json=data)

        else:
            # Mock Request for Unit Testing
            r = requests.put(self.base_url + '/monitoring_policies/%s/ports/%s' %
                    (monitoring_policy_id, port_id), headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_process(self, monitoring_policy_id=None, process_id=None,
            process=None, test=False):

        # Error Handling
        if(monitoring_policy_id == None):
            raise ValueError('monitoring_policy_id is a required parameter')
        if(process_id == None):
            raise ValueError('process_id is a required parameter')

        # Use flag to skip this live API call when running unit test
        if(test == False):
            # Make request for existing process object
            json = self.get_monitoring_policy_process(
                monitoring_policy_id=monitoring_policy_id,
                process_id=process_id)
            del json['id']

            # Update process object with new values, if necessary.
            if(json['alert_if'] != process.process_set['alert_if']):
                if(process.process_set['alert_if'] != None):
                    json['alert_if'] = process.process_set['alert_if']

            if(json['email_notification'] !=
                process.process_set['email_notification']):
                if(process.process_set['email_notification'] != None):
                    json['email_notification'] = process.process_set['email_notification']

            # Perform Request
            data = {'processes': json}

            url = ('%s/monitoring_policies/%s/processes/%s' %
                (self.base_url, monitoring_policy_id, process_id))

            r = requests.put(url, headers=self.header, json=data)

        else:
            # Mock Request for Unit Testing
            r = requests.put(self.base_url + '/monitoring_policies/%s/processes/%s' %
                (monitoring_policy_id, process_id), headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Log Functions

    # 'GET' Methods

    def list_logs(self, page=None, per_page=None, sort=None, q=None,
            fields=None, period='LAST_24H', start_date=None, end_date=None):

        # Error Handling
        if(period == 'CUSTOM'):
            if(start_date == None):
                raise ValueError(('start_date parameter is required when '
                                  'using CUSTOM period'))
            if(end_date == None):
                raise ValueError(('end_date parameter is required when '
                                  'using CUSTOM period'))

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields,
            'period': period,
            'start_date': start_date,
            'end_date': end_date
        }

        url = '%s/logs' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_log(self, log_id=None):

        # Error Handling
        if(log_id == None):
            raise ValueError('log_id parameter is required')

        # Perform Request
        url = '%s/logs/%s' % (self.base_url, log_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # User Functions

    # 'GET' Methods

    def list_users(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/users' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_user(self, user_id=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')

        # Perform Request
        url = '%s/users/%s' % (self.base_url, user_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def api_info(self, user_id=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')

        # Perform Request
        url = '%s/users/%s/api' % (self.base_url, user_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def show_api_key(self, user_id=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')

        # Perform Request
        url = '%s/users/%s/api/key' % (self.base_url, user_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def ips_api_access_allowed(self, user_id=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')

        # Perform Request
        url = '%s/users/%s/api/ips' % (self.base_url, user_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_user(self, name=None, password=None, email=None,
            description=None):

        # Error Handling
        if(name == None):
            raise ValueError('name is a required parameter')
        if(password == None):
            raise ValueError('password is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'password': password,
            'email': email,
            'description': description
        }

        url = '%s/users' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def add_user_ip(self, user_id=None, user_ips=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')
        if(user_ips == None):
            raise ValueError(('user_ips is a required parameter. Make '
                              'sure you pass a list with at least '
                              'one IP string.'))

        # Unpack IPs
        ips = []

        for value in user_ips:
            ips.append(value)

        # Perform Request
        data = {'ips': ips}

        url = '%s/users/%s/api/ips' % (self.base_url, user_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_user(self, user_id=None, description=None, email=None,
            password=None, state=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')
        if(password != None) and (len(password) < 8):
            raise ValueError('password must be at least 8 characters long')
        if(state != None) and (state != 'ACTIVE') and (state != 'DISABLE'):
            raise ValueError('state should be set to "ACTIVE" or "DISABLE".')

        # Perform Request
        data = {
            'description': description,
            'email': email,
            'password': password,
            'state': state
        }

        url = '%s/users/%s' % (self.base_url, user_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_user_api(self, user_id=None, active=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')
        if(active != None) and (active != True) and (active != False):
            raise ValueError('active parameter only accepts a boolean value')

        # Perform Request
        data = {'active': active}

        url = '%s/users/%s/api' % (self.base_url, user_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def change_api_key(self, user_id=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/users/%s/api/key' % (self.base_url, user_id)

        r = requests.put(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_user(self, user_id=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/users/%s' % (self.base_url, user_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_user_ip(self, user_id=None, ip=None):

        # Error Handling
        if(user_id == None):
            raise ValueError('user_id is a required parameter')
        if(ip == None):
            raise ValueError('ip is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/users/%s/api/ips/%s' % (self.base_url, user_id, ip)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Usage Functions

    # 'GET' Methods

    def list_usages(self, page=None, per_page=None, sort=None, q=None,
            fields=None, period='LAST_24H', start_date=None, end_date=None):

        # Error Handling
        if(period == 'CUSTOM'):
            if(start_date == None):
                raise ValueError(('start_date parameter is required when '
                                  'using CUSTOM period'))
            if(end_date == None):
                raise ValueError(('end_date parameter is required when '
                                  'using CUSTOM period'))

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields,
            'period': period,
            'start_date': start_date,
            'end_date': end_date
        }

        url = '%s/usages' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Server Appliance Functions

    # 'GET' Methods

    def list_appliances(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/server_appliances' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_appliance(self, appliance_id=None):

        # Error Handling
        if(appliance_id == None):
            raise ValueError('appliance_id is a required parameter')

        # Perform Request
        url = '%s/server_appliances/%s' % (self.base_url, appliance_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # DVD Functions

    # 'GET' Methods

    def list_dvds(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/dvd_isos' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_dvd(self, iso_id=None):

        # Error Handling
        if(iso_id == None):
            raise ValueError('iso_id parameter is required')

        # Perform Request
        url = '%s/dvd_isos/%s' % (self.base_url, iso_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Datacenter Functions

    # 'GET' Methods

    def list_datacenters(self, page=None, per_page=None, sort=None,
            q=None, fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/datacenters' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_datacenter(self, datacenter_id=None):

        # Error Handling
        if(datacenter_id == None):
            raise ValueError('datacenter_id parameter is required')

        # Perform Request
        url = '%s/datacenters/%s' % (self.base_url, datacenter_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Pricing Functions

    # 'GET' Methods

    def pricing(self):

        # Perform Request
        url = '%s/pricing' % self.base_url

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Ping Functions

    # 'GET' Methods

    def ping(self):

        # Perform Request
        url = '%s/ping' % self.base_url

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Ping Auth Functions

    # 'GET' Methods

    def ping_auth(self):

        # Perform Request
        url = '%s/ping_auth' % self.base_url

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # VPN Functions

    # 'GET' Methods

    def list_vpns(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/vpns' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_vpn(self, vpn_id=None):

        # Error Handling
        if(vpn_id == None):
            raise ValueError('vpn_id is a required parameter')

        # Perform Request

        url = '%s/vpns/%s' % (self.base_url, vpn_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def download_config(self, vpn_id=None):

        # Error Handling
        if(vpn_id == None):
            raise ValueError('vpn_id is a required parameter')

        # Perform Request

        url = '%s/vpns/%s/configuration_file' % (self.base_url, vpn_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_vpn(self, vpn=None):

        # Perform Request
        data = {
            'name': vpn.name,
            'description': vpn.description,
            'datacenter_id': vpn.datacenter_id
        }

        url = '%s/vpns' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        # Assign new image_id back to calling Image object
        response = r.json()

        vpn.specs.update(vpn_id=response['id'])
        vpn.specs.update(api_token=self.header)

        return r.json()

    # 'DELETE' Methods

    def delete_vpn(self, vpn_id=None):

        # Error Handling
        if(vpn_id == None):
            raise ValueError('vpn_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/vpns/%s' % (self.base_url, vpn_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_vpn(self, vpn_id=None, name=None, description=None):

        # Error Handling
        if(vpn_id == None):
            raise ValueError('vpn_id is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'description': description
        }

        url = '%s/vpns/%s' % (self.base_url, vpn_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


    # Role Functions

    # 'GET' Methods

    def list_roles(self, page=None, per_page=None, sort=None, q=None,
            fields=None):

        # Perform Request
        parameters = {
            'page': page,
            'per_page': per_page,
            'sort': sort,
            'q': q,
            'fields': fields
        }

        url = '%s/roles' % self.base_url

        r = requests.get(url, headers=self.header, params=parameters)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_role(self, role_id=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request

        url = '%s/roles/%s' % (self.base_url, role_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def permissions(self, role_id=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request

        url = '%s/roles/%s/permissions' % (self.base_url, role_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def role_users(self, role_id=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request

        url = '%s/roles/%s/users' % (self.base_url, role_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def get_role_user(self, role_id=None, user_id=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        url = '%s/roles/%s/users/%s' % (self.base_url, role_id, user_id)

        r = requests.get(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'POST' Methods

    def create_role(self, name=None):

        # Perform Request
        data = {
            'name': name
        }

        url = '%s/vpns' % self.base_url

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def add_users(self, role_id=None, users=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        data = {
            'users': users
        }

        url = '%s/roles/%s/users' % (self.base_url, role_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def clone_role(self, role_id=None, name=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        data = {
            'name': name
        }

        url = '%s/roles/%s/clone' % (self.base_url, role_id)

        r = requests.post(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'DELETE' Methods

    def delete_role(self, role_id=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/roles/%s' % (self.base_url, role_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def remove_user(self, role_id=None, user_id=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        self.header['content-type'] = 'application/json'

        url = '%s/roles/%s/users/%s' % (self.base_url, role_id, user_id)

        r = requests.delete(url, headers=self.header)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    # 'PUT' Methods

    def modify_role(self, role_id=None, name=None, description=None,
        state=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        data = {
            'name': name,
            'description': description,
            'state': state
        }

        url = '%s/roles/%s' % (self.base_url, role_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def modify_permissions(self, role_id=None, servers=None, images=None,
          shared_storages=None, firewalls=None, load_balancers=None, ips=None,
          private_networks=None, vpns=None, monitoring_centers=None,
          monitoring_policies=None, backups=None, logs=None, users=None,
          roles=None, usages=None, interactive_invoices=None):

        # Error Handling
        if(role_id == None):
            raise ValueError('role_id is a required parameter')

        # Perform Request
        data = {
            'servers': servers,
            'images': images,
            'sharedstorages': shared_storages,
            'firewalls': firewalls,
            'loadbalancers': load_balancers,
            'ips': ips,
            'privatenetwork': private_networks,
            'vpn': vpns,
            'monitoringcenter': monitoring_centers,
            'monitoringpolicies': monitoring_policies,
            'backups': backups,
            'logs': logs,
            'users': users,
            'roles': roles,
            'usages': usages,
            'interactiveinvoice': interactive_invoices
        }

        url = '%s/roles/%s/permissions' % (self.base_url, role_id)

        r = requests.put(url, headers=self.header, json=data)

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()


# Utility Classes

class Server(object):

    # Init Function
    def __init__(self, name=None, description=None,
            fixed_instance_size_id=None, vcore=None, cores_per_processor=None,
            ram=None, appliance_id=None, password=None, power_on=None,
            firewall_policy_id=None, ip_id=None, load_balancer_id=None,
            monitoring_policy_id=None, datacenter_id=None, rsa_key=None):

        self.first_password = None
        self.first_ip = None

        self.specs = {
            'name': name,
            'description': description,
            'hardware': {
                'fixed_instance_size_id': fixed_instance_size_id,
                'vcore': vcore,
                'cores_per_processor': cores_per_processor,
                'ram': ram
            },
            'appliance_id': appliance_id,
            'password': password,
            'power_on': power_on,
            'firewall_policy_id': firewall_policy_id,
            'ip_id': ip_id,
            'load_balancer_id': load_balancer_id,
            'monitoring_policy_id': monitoring_policy_id,
            'datacenter_id': datacenter_id,
            'rsa_key': rsa_key
        }

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('Server: name=%s, description=%s, fixed_instance_size_id=%s, '
                'vcore=%s, cores_per_processor=%s, ram=%s, appliance_id=%s, '
                'password=%s, power_on=%s, firewall_policy_id=%s, ip_id=%s, '
                'load_balancer_id=%s, monitoring_policy_id=%s, '
                'rsa_key=%s, datacenter_id=%s, first_password=%s, '
                'first_ip=%s' %
                    (self.specs['name'], self.specs['description'],
                     self.specs['hardware']['fixed_instance_size_id'],
                     self.specs['hardware']['vcore'],
                     self.specs['hardware']['cores_per_processor'],
                     self.specs['hardware']['ram'],
                     self.specs['appliance_id'], self.specs['password'],
                     self.specs['power_on'], self.specs['firewall_policy_id'],
                     self.specs['ip_id'], self.specs['load_balancer_id'],
                     self.specs['monitoring_policy_id'],
                     self.specs['rsa_key'], self.specs['datacenter_id'],
                     self.first_password, self.first_ip))

    def get(self):

        # Perform Request
        url = ('%s/servers/%s' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def hardware(self):

        # Perform Request
        url = ('%s/servers/%s/hardware' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def hdds(self):

        # Perform Request
        url = ('%s/servers/%s/hardware/hdds' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def image(self):

        # Perform Request
        url = ('%s/servers/%s/image' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def ips(self):

        # Perform Request
        url = ('%s/servers/%s/ips' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def status(self):

        # Perform Request
        url = ('%s/servers/%s/status' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def dvd(self):

        # Perform Request
        url = ('%s/servers/%s/dvd' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def private_networks(self):

        # Perform Request
        url = ('%s/servers/%s/private_networks' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def snapshots(self):

        # Perform Request
        url = ('%s/servers/%s/snapshots' %
            (self.base_url, self.specs['server_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=15):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial server status
        url = '%s/servers/%s' % (self.base_url, self.specs['server_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        server_state = response['status']['state']
        percent = response['status']['percent']

        # Keep polling the server's status until good
        while (server_state not in self.good_states) or (percent != None):

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            server_state = response['status']['state']
            percent = response['status']['percent']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

            # Parse for first IP address
            if len(response['ips']) == 1:
                self.first_ip = response['ips'][0]

        return {'duration': duration}



class Hdd(object):

    # Init Function
    def __init__(self, size=None, is_main=None):
        self.specs = {
            'size': size,
            'is_main': is_main
        }

    def __repr__(self):
        return ('HDD: size=%s, is_main=%s' %
            (self.specs['size'], self.specs['is_main']))

class AttachServer(object):

    # Init Function
    def __init__(self, server_id=None, rights=None, server_ip_id=None):
        self.server_id = server_id
        self.rights = rights
        self.server_ip_id = server_ip_id

    def __repr__(self):
        return ('AttachServer: server_id=%s, rights=%s, server_ip_id=%s' %
            (self.server_id, self.rights, self.server_ip_id))

class Image(object):

    # Init Function
    def __init__(self, server_id=None, name=None, description=None,
            frequency=None, num_images=None):

        self.server_id = server_id
        self.name = name
        self.description = description
        self.frequency = frequency
        self.num_images = num_images

        self.specs = {}

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('Image: server_id=%s, name=%s, description=%s, '
                'frequency=%s, num_images=%s' % (self.server_id,
                    self.name, self.description, self.frequency,
                    self.num_images))

    def get(self):

        # Perform Request
        url = ('%s/images/%s' %
            (self.base_url, self.specs['image_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=15):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/images/%s' % (self.base_url, self.specs['image_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        image_state = response['state']

        # Keep polling the server's status until good
        while image_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            image_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}

class SharedStorage(object):

    # Init Function
    def __init__(self, name=None, description=None, size=None,
            datacenter_id=None):

        self.name = name
        self.description = description
        self.size = size
        self.datacenter_id = datacenter_id

        self.specs = {}

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('Shared Storage: name=%s, description=%s, size=%s' %
                (self.name, self.description, self.size, self.datacenter_id))

    def get(self):

        # Perform Request
        url = ('%s/shared_storages/%s' %
            (self.base_url, self.specs['shared_storage_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def servers(self):

        # Perform Request
        url = ('%s/shared_storages/%s/servers' %
            (self.base_url, self.specs['shared_storage_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=5):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/shared_storages/%s' % (self.base_url,
            self.specs['shared_storage_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        shared_storage_state = response['state']

        # Keep polling the server's status until good
        while shared_storage_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            shared_storage_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}

class FirewallPolicyRule(object):

    # Init Function
    def __init__(self, protocol=None, port_from=None, port_to=None,
            source=None):

        self.rule_set = {
            'protocol': protocol,
            'port_from': port_from,
            'port_to': port_to,
            'source': source
        }

    def __repr__(self):
        return ('FirewallPolicyRule: protocol=%s, port_from=%s, '
                'port_to=%s, source=%s' %
                (self.rule_set['protocol'], self.rule_set['port_from'],
                    self.rule_set['port_to'], self.rule_set['source']))

class FirewallPolicy(object):

    # Init Function
    def __init__(self, name=None, description=None):
        self.specs = {
            'name': name,
            'description': description
        }

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('FirewallPolicy: name=%s, description=%s' %
            (self.specs['name'], self.specs['description']))

    def get(self):

        # Perform Request
        url = ('%s/firewall_policies/%s' %
            (self.base_url, self.specs['firewall_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def ips(self):

        # Perform Request
        url = ('%s/firewall_policies/%s/server_ips' %
            (self.base_url, self.specs['firewall_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def rules(self):

        # Perform Request
        url = ('%s/firewall_policies/%s/rules' %
            (self.base_url, self.specs['firewall_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=5):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/firewall_policies/%s' % (self.base_url, self.specs['firewall_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        firewall_state = response['state']

        # Keep polling the server's status until good
        while firewall_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            firewall_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}

class LoadBalancerRule(object):

    # Init Function
    def __init__(self, protocol=None, port_balancer=None, port_server=None,
            source=None):

        self.rule_set = {
            'protocol': protocol,
            'port_balancer': port_balancer,
            'port_server': port_server,
            'source': source
        }

    def __repr__(self):
        return ('LoadBalancerRule: protocol=%s, port_balancer=%s, '
                'port_server=%s, source=%s' % (self.rule_set['protocol'],
                    self.rule_set['port_balancer'],
                    self.rule_set['port_server'], self.rule_set['source']))

class LoadBalancer(object):

    # Init Function
    def __init__(self, health_check_path=None, health_check_parse=None,
            name=None, description=None, health_check_test=None,
            health_check_interval=None, persistence=None,
            persistence_time=None, method=None, datacenter_id=None):

        self.specs = {
            'health_check_path': health_check_path,
            'health_check_parse': health_check_parse,
            'name': name,
            'description': description,
            'health_check_test': health_check_test,
            'health_check_interval': health_check_interval,
            'persistence': persistence,
            'persistence_time': persistence_time,
            'method': method,
            'datacenter_id': datacenter_id
        }

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('LoadBalancer: health_check_path=%s, health_check_parse=%s, '
                'name=%s, description=%s, health_check_test=%s, '
                'health_check_interval=%s, persistence=%s, '
                'persistence_time=%s, method=%s, datacenter_id=%s' %
                (self.specs['health_check_path'],
                    self.specs['health_check_parse'], self.specs['name'],
                    self.specs['description'], self.specs['health_check_test'],
                    self.specs['health_check_interval'],
                    self.specs['persistence'], self.specs['persistence_time'],
                    self.specs['method'], self.datacenter_id))

    def get(self):

        # Perform Request
        url = ('%s/load_balancers/%s' %
            (self.base_url, self.specs['load_balancer_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def ips(self):

        # Perform Request
        url = ('%s/load_balancers/%s/server_ips' %
            (self.base_url, self.specs['load_balancer_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def rules(self):

        # Perform Request
        url = ('%s/load_balancers/%s/rules' %
            (self.base_url, self.specs['load_balancer_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=5):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/load_balancers/%s' % (self.base_url,
            self.specs['load_balancer_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        load_balancer_state = response['state']

        # Keep polling the server's status until good
        while load_balancer_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            load_balancer_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}

class PrivateNetwork(object):

    # Init Function
    def __init__(self, name=None, description=None, network_address=None,
            subnet_mask=None, datacenter_id=None):

        self.name = name
        self.description = description
        self.network_address = network_address
        self.subnet_mask = subnet_mask
        self.datacenter_id = datacenter_id

        self.specs = {}

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('Private Network: name=%s, description=%s, network_address=%s, '
                'subnet_mask=%s' % (self.name, self.description,
                    self.network_address, self.subnet_mask))

    def get(self):

        # Perform Request
        url = ('%s/private_networks/%s' %
            (self.base_url, self.specs['private_network_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def servers(self):

        # Perform Request
        url = ('%s/private_networks/%s/servers' %
            (self.base_url, self.specs['private_network_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=5):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/private_networks/%s' % (self.base_url,
            self.specs['private_network_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        private_network_state = response['state']

        # Keep polling the server's status until good
        while private_network_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            private_network_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}

class MonitoringPolicy(object):

    # Init Function
    def __init__(self, name=None, description=None, email=None, agent=None):
        self.specs = {
            'name': name,
            'description': description,
            'email': email,
            'agent': agent
        }

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('MonitoringPolicy: name=%s, description=%s, email=%s, '
                'agent=%s' %
                (self.specs['name'], self.specs['description'],
                    self.specs['email'], self.specs['agent']))

    def get(self):

        # Perform Request
        url = ('%s/monitoring_policies/%s' %
            (self.base_url, self.specs['monitoring_policy_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def ports(self):

        # Perform Request
        url = ('%s/monitoring_policies/%s/ports' %
            (self.base_url, self.specs['monitoring_policy_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def processes(self):

        # Perform Request
        url = ('%s/monitoring_policies/%s/processes' %
            (self.base_url, self.specs['monitoring_policy_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def servers(self):

        # Perform Request
        url = ('%s/monitoring_policies/%s/servers' %
            (self.base_url, self.specs['monitoring_policy_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=5):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/monitoring_policies/%s' % (self.base_url,
            self.specs['monitoring_policy_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        mp_state = response['state']

        # Keep polling the server's status until good
        while mp_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            mp_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}

class Threshold(object):

    # Init Function
    def __init__(self, entity=None, warning_value=None, warning_alert=None,
            critical_value=None, critical_alert=None):

        self.entity = entity
        self.warning_value = warning_value
        self.warning_alert = warning_alert
        self.critical_value = critical_value
        self.critical_alert = critical_alert

    def __repr__(self):
        return ('Threshold: entity=%s, warning_value=%s, warning_alert=%s, '
                'critical_value=%s, critical_alert=%s' % (self.entity,
                    self.warning_value, self.warning_alert, self.critical_value,
                    self.critical_alert))

class Port(object):

    # Init Function
    def __init__(self, protocol=None, port=None, alert_if=None,
            email_notification=None):

        self.specs = {
            'protocol': protocol,
            'port': port,
            'alert_if': alert_if,
            'email_notification': email_notification
        }

    def __repr__(self):
        return ('Port: protocol=%s, port=%s, alert_if=%s, '
                'email_notification=%s' % (self.specs['protocol'],
                    self.specs['port'], self.specs['alert_if'],
                    self.specs['email_notification']))

class Process(object):

    # Init Function
    def __init__(self, process=None, alert_if=None, email_notification=None):
        self.process_set = {
            'process': process,
            'alert_if': alert_if,
            'email_notification': email_notification
        }

    def __repr__(self):
        return ('Process: process=%s, alert_if=%s, email_notification=%s' %
                (self.process_set['process'], self.process_set['alert_if'],
                    self.process_set['email_notification']))

class Vpn(object):

    # Init Function
    def __init__(self, name=None, description=None, datacenter_id=None):

        self.name = name
        self.description = description
        self.datacenter_id = datacenter_id

        self.specs = {}

        self.base_url = 'https://cloudpanel-api.1and1.com/v1'
        self.success_codes = (200, 201, 202)
        self.good_states = ('ACTIVE', 'ENABLED', 'POWERED_ON', 'POWERED_OFF')

    def __repr__(self):
        return ('Vpn: name=%s, description=%s, datacenter_id=%s' % (self.name,
            self.description, self.datacenter_id))

    def get(self):

        # Perform Request
        url = ('%s/vpns/%s' %
            (self.base_url, self.specs['vpn_id']))

        r = requests.get(url, headers=self.specs['api_token'])

        # Handle Potential Response Errors
        if r.status_code not in self.success_codes:
            error_message = ('Error Code: %s. Error Message: %s.' %
                (r.status_code, r.text))
            raise Exception(error_message)

        return r.json()

    def wait_for(self, timeout=25, interval=15):

        # Capture start time
        start = time.time()
        duration = 0

        # Check initial image status
        url = '%s/vpns/%s' % (self.base_url, self.specs['vpn_id'])

        r = requests.get(url, headers=self.specs['api_token'])
        response = r.json()

        # Store initial server state and percent values
        vpn_state = response['state']

        # Keep polling the server's status until good
        while vpn_state not in self.good_states:

            # Wait 15 seconds before polling again
            time.sleep(interval)

            # Check server status again
            r = requests.get(url, headers=self.specs['api_token'])
            response = r.json()

            # Update server state and percent values
            vpn_state = response['state']

            # Check for timeout
            seconds = (time.time() - start)
            duration = seconds / 60
            if duration > timeout:
                print 'The operation timed out after %s minutes.' % timeout
                return

        return {'duration': duration}
