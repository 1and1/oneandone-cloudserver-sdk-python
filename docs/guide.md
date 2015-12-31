# 1&amp;1 Python SDK

The 1&amp;1 Python SDK is a Python library used for interacting with the 1&amp;1 platform over the REST API.

This guide will show you how to programmatically use the 1&amp;1 library to perform common management tasks also available through the 1&amp;1 Control Panel.

## Table of Contents

- [Concepts](#concepts)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Authentication](#authentication)
- [Resources &amp; Using the Module](#using-module)
- [How To: Create a Server](#create-server)
- [How To: Create a Firewall Policy](#create-fp)
- [How To: Create a Load Balancer](#create-lb)
- [How To: Create a Monitoring Policy](#create-mp)
- [How To: Update Server Cores, Memory, and Disk](#update-hardware)
- [How To: List Servers, Images, Shared Storages, etc.](#list-things)
- [Example App](#app)


## <a name="concepts"></a> Concepts

The Python Client Library wraps the latest version of the 1&amp;1 REST API. All API operations are performed over SSL and authenticated using your 1&amp;1 API Token. The API can be accessed within an instance running in 1&amp;1 or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


## <a name="getting-started"></a> Getting Started

Before you begin you will need to have signed-up for a 1&amp;1 account. The credentials you setup during sign-up will be used to authenticate against the API.


## <a name="installation"></a> Installation

The Python Client Library is available on <a href='https://pypi.python.org/pypi/1and1'>PyPi</a>. You can install the latest stable version using pip:

`pip install 1and1`

Done!


## <a name="authentication"></a> Authentication

Connecting to 1&amp;1 is handled by first setting up your authentication.

```
from oneandone.client import OneAndOneService

client = OneAndOneService('API-TOKEN')
```

You can now use `client` for any future requests.



## <a name="using-module"></a> Resources &amp; Using the Module

**Resources**

Official 1&amp;1 REST API Documentation: <a href='https://cloudpanel-api.1and1.com/documentation/v1/#' target='_blank'>https://cloudpanel-api.1and1.com/documentation/v1/#</a>

1&amp;1 Python SDK Method Reference Sheet: <a href='docs/reference.md'>reference.md</a>

**Using the Module**

The following "**How To's**" are meant to give you a general overview of some of the things you can do with the 1&amp;1 Python SDK.  For a detailed list of all methods and functionality, please visit the <a href='docs/reference.md'>reference.md</a> file.


## <a name="create-server"></a> How To: Create a Server

```
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


## <a name="create-fp"></a> How To: Create a Firewall Policy

```
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


## <a name="create-lb"></a> How To: Create a Load Balancer

```
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


## <a name="create-mp"></a> How To: Create a Monitoring Policy


First, create the monitoring policy:
```
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
```
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


## <a name="update-hardware"></a> How To: Update Server Cores, Memory, and Disk

1&amp;1 allows users to dynamically update cores, memory, and disk independently of each other. This removes the restriction of needing to upgrade to the next size up to receive an increase in memory. You can now simply increase the instances memory keeping your costs in-line with your resource needs.

The following code illustrates how you can update cores and memory:
```
from oneandone.client import OneAndOneService

client = OneAndOneService('<API-TOKEN>')


response = modify_server_hardware(server_id='<SERVER ID>',
                                  vcore=2,
                                  ram=6
                                  )
```

This is how you would update a server disk's size:
```
response = client.modify_hdd(server_id='<SERVER_ID>',
                             hdd_id='<HDD ID>',
                             size=80
                             )
```


## <a name="list-things"></a> How To: List Servers, Images, Shared Storages, etc.

Generating a list of resources is fairly straight forward.  Each "list" method follows this general format: `list_*()` where the `*` is `servers`, `images`, `load_balancers`, etc.  You may also pass optional query parameters to help filter your results.  By default, these parameters are all set to `None`.

**Here are the parameters available to you:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`page` (integer): Allows to the use of pagination. Indicate which page to start on.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`per_page` (integer): Number of items per page.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`sort` (string): `sort='name'` retrieves a list of elements sorted alphabetically. `sort='creation_date'` retrieves a list of elements sorted by their creation date in descending order.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`q` (string): `q` is for query.  Use this parameter to return only the items that match your search query.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-`fields` (string): Returns only the parameters requested. (i.e. fields='id, name, description, hardware.ram')


**Here are a few examples of how you would list resources:**
```
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


## <a name="app"></a> Example App

This simple app creates a load balancer, firewall policy, and server.  It then creates a new IP for the server and attaches the load balancer and firewall policy to that IP.

Use the `wait_for()` method to chain together multiple actions that take a while to deploy.  See the <a href='docs/reference.md'>reference.md</a> file for a more detailed description of the `wait_for()` method and other class helper methods.

The original source code for the Example App with some additional markup and cleanup can be found <a href='examples/example_app.py'>HERE</a>
```
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd, LoadBalancer, LoadBalancerRule
from oneandone.client import FirewallPolicy, FirewallPolicyRule

client = OneAndOneService('<API-TOKEN>')


# Create Load Balancer
lb1 = LoadBalancer(name='Example App LB',
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

new_load_balancer = client.create_load_balancer(load_balancer=lb1,
                                                load_balancer_rules=rules
                                                )

## Wait for Load Balancer to go live
print 'Creating load balancer...'
lb1.wait_for()


# Create Firewall Policy
fp1 = FirewallPolicy(name='Example App FP',
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


new_firewall = client.create_firewall_policy(firewall_policy=fp1,
					     	 				 firewall_policy_rules=rules
					     	 				 )

## Wait for Firewall Policy to go live
print 'Creating firewall policy...'
fp1.wait_for()


# Create Server
server1 = Server(name='Example App Server',
                 description='Server Description',
                 vcore=1,
                 cores_per_processor=1, 
                 ram=2, 
                 appliance_id='D9DBA7D7F7E9C8200A493CE9013C4605'
                 )

hdd1 = Hdd(size=120, is_main=True)
hdd2 = Hdd(size=60, is_main=False)

hdds = [hdd1, hdd2]

new_server = client.create_server(server=server1, hdds=hdds)

## Wait for the Server to go live
print 'Creating new server...'
server1.wait_for()


# Add a new IP to the server
new_ip = client.add_new_ip(server_id=new_server['id'])


# Add Load Balancer to New Server IP
lb_response = client.add_load_balancer(server_id=new_server['id'],
                                       ip_id=new_ip['ips'][1]['id'],
                                       load_balancer_id=new_load_balancer['id']
                                       )

## Wait for Load Balancer to be added
print 'Adding load balancer to Server...'
server1.wait_for()


# Add Firewall Policy to New Server IP
fw_response = client.add_firewall_policy(server_id=new_server['id'],
					 					 ip_id=new_ip['ips'][1]['id'],
					 					 firewall_id=new_firewall['id']
					 					 )

## Wait for Firewall Policy to be added
print 'Adding firewall policy to Server...'
server1.wait_for()
```
