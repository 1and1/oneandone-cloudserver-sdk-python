# 1&1 Python SDK

The 1&1 Python SDK is a Python library used for interacting with the 1&1 platform over the REST API.

This guide will show you how to programmatically use the 1&1 library to perform common management tasks also available through the 1&1 Control Panel. For more information on the 1&1 Python SDK see the [1&1 Community Portal](https://www.1and1.com/cloud-community/).

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Authentication](#authentication)
- [Operations](#operations)
  - [Resources and Using the Module](#resources-and-using-the-module)
  - [Creating a Server](#creating-a-server)
  - [Creating a Server with SSH Key Access](#creating-a-server-with-ssh-key-access)
  - [Creating a Firewall Policy](#creating-a-firewall-policy)
  - [Creating a Load Balancer](#creating-a-load-balancer)
  - [Creating a Monitoring Policy](#creating-a-monitoring-policy)
  - [Updating Server Cores, Memory, and Disk](#updating-server-cores,-memory,-and-disk)
  - [Listing Servers, Images, Shared Storages, etc.](#listing-servers,-images,-shared-storages,-etc.)
    * [Available Parameters](#available-parameters)
    * [Examples of Listing Resources](#examples-of-listing-resources)
- [Example App](#example-app)


## Overview

The Python Client Library wraps the latest version of the 1&1 REST API. All API operations are performed over SSL and authenticated using your 1&1 API Token. The API can be accessed within an instance running in 1&1 or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.

For more information on the 1&1 Cloud Server SDK for Python, visit the [Community Portal](https://www.1and1.com/cloud-community/).


## Getting Started

Before you begin you will need to have signed up for a 1&1 account. The credentials you create during sign-up will be used to authenticate against the API. 


### Installation

The Python Client Library is available on <a href='https://pypi.python.org/pypi/1and1'>PyPi</a>. You can install the latest stable version using pip:

```bash
$ pip install 1and1
```

Done!


### Authentication

Connecting to 1&1 is handled by first setting up your authentication.

```python
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')
```

You can now use `client` for any future requests.

## Operations

### Resources and Using the Module

**Resources**

Official 1&amp;1 REST API Documentation: <a href='https://cloudpanel-api.1and1.com/documentation/1and1/v1/en/documentation.html' target='_blank'>https://cloudpanel-api.1and1.com/documentation/1and1/v1/en/documentation.html</a>

1&amp;1 Python SDK Method Reference Sheet: <a href='docs/reference.md'>reference.md</a>

**Using the Module**

The following "**How To's**" are meant to give you a general overview of some of the things you can do with the 1&amp;1 Python SDK.  For a detailed list of all methods and functionality, please visit the <a href='docs/reference.md'>reference.md</a> file.


### Creating a Server

```python
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd

client = OneAndOneService('<API-TOKEN>')


server1 = Server(name='Test Server',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1, 
                 ram=2, 
                 appliance_id='<IMAGE ID>'
                 )

hdd1 = Hdd(size=120, is_main=True)
hdd2 = Hdd(size=60, is_main=False)

hdds = [hdd1, hdd2]

new_server = client.create_server(server=server1, hdds=hdds)
```

### Creating a Server with SSH Key Access

```python
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd

client = OneAndOneService('<API-TOKEN>')


# Assign your public key to a variable
pub_key = '<PUB-KEY>'

server1 = Server(name='Test Server',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1, 
                 ram=2, 
                 appliance_id='<IMAGE ID>',
                 rsa_key=pub_key
                 )

hdd1 = Hdd(size=120, is_main=True)
hdd2 = Hdd(size=60, is_main=False)

hdds = [hdd1, hdd2]

new_server = client.create_server(server=server1, hdds=hdds)
```
**Note:** You may then SSH into your server by executing the following command in terminal 

`ssh –i <path_to_private_key_file> root@SERVER_IP`


### Creating a Firewall Policy

```python
from oneandone.client import OneAndOneService
from oneandone.client import FirewallPolicy, FirewallPolicyRule

client = OneAndOneService('<API-TOKEN>')


fp1 = FirewallPolicy(name='Test Firewall Policy',
                     description='Test Description'
                     )


rule1 = FirewallPolicyRule(protocol='TCP',
                           port_from=80,
                           port_to=80,
                           source='0.0.0.0'
                           )

rule2 = FirewallPolicyRule(protocol='UDP',
                           port_from=443,
                           port_to=443,
                           source='0.0.0.0'
                           )

rules = [rule1, rule2]


new_firewall = client.create_firewall_policy(firewall_policy=fp1, firewall_policy_rules=rules)
```


### Creating a Load Balancer

```python
from oneandone.client import OneAndOneService
from oneandone.client import LoadBalancer, LoadBalancerRule

client = OneAndOneService('<API-TOKEN>')


lb1 = LoadBalancer(name='Test Load Balancer',
                   description='Test Description',
                   health_check_test='TCP',
                   health_check_interval=40,
                   persistence=True,
                   persistence_time=1200,
                   method='ROUND_ROBIN'
                   )

rule1 = LoadBalancerRule(protocol='TCP',
                         port_balancer=80,
                         port_server=80,
                         source='0.0.0.0'
                         )
rule2 = LoadBalancerRule(protocol='TCP',
                         port_balancer=9999,
                         port_server=8888,
                         source='0.0.0.0'
                         )

rules = [rule1, rule2]

new_load_balancer = client.create_load_balancer(load_balancer=lb1, load_balancer_rules=rules)
```


### Creating a Monitoring Policy


First, create the monitoring policy:
```python
from oneandone.client import OneAndOneService
from oneandone.client import MonitoringPolicy, Threshold, Port, Process

client = OneAndOneService('<API-TOKEN>')


mp1 = MonitoringPolicy(name='Test MP',
                       description='Test Description',
                       email='test@example.com',
                       agent=True
                       )


cpu = Threshold(entity='cpu',
                warning_value=90,
                warning_alert=False,
                critical_value=95,
                critical_alert=False
                )

ram = Threshold(entity='ram',
                warning_value=90,
                warning_alert=False,
                critical_value=95,
                critical_alert=False
                )

disk = Threshold(entity='disk',
                 warning_value=80,
                 warning_alert=False,
                 critical_value=90,
                 critical_alert=False
                 )

transfer = Threshold(entity='transfer',
                     warning_value=1000,
                     warning_alert=False,
                     critical_value=2000,
                     critical_alert=False
                     )

internal_ping = Threshold(entity='internal_ping',
                          warning_value=50,
                          warning_alert=False,
                          critical_value=100,
                          critical_alert=False
                          )

thresholds = [cpu, ram, disk, transfer, internal_ping]


port1 = Port(protocol='TCP',
             port=22,
             alert_if='RESPONDING',
             email_notification=False
             )

port2 = Port(protocol='TCP',
             port=44,
             alert_if='NOT_RESPONDING',
             email_notification=True
             )

ports = [port1, port2]


process1 = Process(process='TaskMgr',
                   alert_if='NOT_RUNNING',
                   email_notification=True
                   )

process2 = Process(process='Logger',
                   alert_if='NOT_RUNNING',
                   email_notification=True
                   )

processes = [process1, process2]


new_monitoring_policy = client.create_monitoring_policy(monitoring_policy=mp1,
                                                        thresholds=thresholds,
                                                        ports=ports,
                                                        processes=processes
                                                        )
```

Then, add a server or two:
```python
from oneandone.client import OneAndOneService
from oneandone.client import AttachServer

client = OneAndOneService('<API-TOKEN>')


server1 = AttachServer(server_id='<SERVER1 ID>')
server2 = AttachServer(server_id='<SERVER2 ID>')

servers = [server1, server2]

response = client.attach_monitoring_policy_server(monitoring_policy_id='<MONITORING POLICY ID>',
                                                  servers=servers
                                                  )
```


### Updating Server Cores, Memory, and Disk

1&amp;1 allows users to dynamically update cores, memory, and disk independently of each other. This means you will no longer have to upgrade your server to receive an increase in memory. You can now simply increase the instance's memory, which keeps your costs in-line with your resource needs.

The following code illustrates how you can update cores and memory:
```python
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')


response = modify_server_hardware(server_id='<SERVER ID>',
                                  vcore=2,
                                  ram=6
                                  )
```

This is how you would update a server disk's size:
```python
response = client.modify_hdd(server_id='<SERVER_ID>',
                             hdd_id='<HDD ID>',
                             size=80
                             )
```


### Listing Servers, Images, Shared Storages, etc.

Generating a list of resources is fairly straight forward.  Each "list" method follows this general format: `list_*()` where the `*` is `servers`, `images`, `load_balancers`, etc.  You may also pass optional query parameters to help filter your results.  By default, these parameters are all set to `None`.

#### Available Parameters

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`page` (integer): Allows to the use of pagination. Indicate which page to start on.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`per_page` (integer): Number of items per page.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`sort` (string): `sort='name'` retrieves a list of elements sorted alphabetically. `sort='creation_date'` retrieves a list of elements sorted by their creation date in descending order.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`q` (string): `q` is for query.  Use this parameter to return only the items that match your search query.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`fields` (string): Returns only the parameters requested. (i.e. fields='id, name, description, hardware.ram')


#### Examples of Listing Resources
```python
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')


servers = client.list_servers()

images = client.list_images()

shared_storages = client.list_shared_storages()

firewall_policies = client.list_firewall_policies()

load_balancers = client.list_load_balancers()

private_networks = client.list_private_networks()

monitoring_policies = client.list_monitoring_policies()
```


## Example App

This simple app creates a load balancer, firewall policy, and server.  It then adds the load balancer and firewall policy to the server's initial IP address.  You can access a server's initial IP by using the `first_ip` attribute on the Server class object, as seen in the example below.

The source code for the Example App can be found <a href='examples/example_app.py'>here</a>.
```python
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd, LoadBalancer, LoadBalancerRule
from oneandone.client import FirewallPolicy, FirewallPolicyRule

client = OneAndOneService('<API-Token>')


# Create Load Balancer
lb1 = LoadBalancer(name='Example App LB', description='Example Description',
  health_check_test='TCP', health_check_interval=40, persistence=True,
  persistence_time=1200, method='ROUND_ROBIN')

rule1 = LoadBalancerRule(protocol='TCP', port_balancer=80, port_server=80,
  source='0.0.0.0')

rules = [rule1]

new_load_balancer = client.create_load_balancer(load_balancer=lb1,
  load_balancer_rules=rules)

## Wait for Load Balancer to go live
print 'Creating load balancer...'
print lb1.wait_for()


# Create Firewall Policy
fp1 = FirewallPolicy(name='Example App FP', description='Test Description')

rule1 = FirewallPolicyRule(protocol='TCP', port_from=80, port_to=80,
  source='0.0.0.0')

rules = [rule1]

new_firewall = client.create_firewall_policy(firewall_policy=fp1,
  firewall_policy_rules=rules)

## Wait for Firewall Policy to go live
print 'Creating firewall policy...'
print fp1.wait_for()


# Create Server
server1 = Server(name='Example App Server',
  fixed_instance_size_id='65929629F35BBFBA63022008F773F3EB',
  appliance_id='6C902E5899CC6F7ED18595EBEB542EE1',
  datacenter_id='5091F6D8CBFEF9C26ACE957C652D5D49')

new_server = client.create_server(server=server1)

## Wait for the Server to go live
print 'Creating new server...'
print server1.wait_for()


# Add Load Balancer to New Server
lb_response = client.add_load_balancer(server_id=new_server['id'],
  ip_id=server1.first_ip['id'], load_balancer_id=new_load_balancer['id'])

## Wait for Load Balancer to be added
print 'Adding load balancer to Server...'
print server1.wait_for()


# Add Firewall Policy to New Server
fw_response = client.add_firewall_policy(server_id=new_server['id'],
  ip_id=server1.first_ip['id'], firewall_id=new_firewall['id'])

## Wait for Firewall Policy to be added
print 'Adding firewall policy to Server...'
print server1.wait_for()
print 'Everything looks good!'


# Cleanup the rubbish
print 'Cleaning up the mess we just made...\n'

print 'Deleting server...'
client.delete_server(server_id=new_server['id'])

print 'Deleting load balancer...'
client.delete_load_balancer(load_balancer_id=new_load_balancer['id'])

print 'Deleting firewall...'
client.delete_firewall(firewall_id=new_firewall['id'])

print '\nAll done!'
```

