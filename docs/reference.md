# 1&amp;1 Python SDK


# Table of Contents

- [The 'wait_for' Method](#the-'wait_for'-method)
- [Class Helper Methods](#class-helper-methods)
- [Servers](#servers)
- [Images](#images)
- [Shared Storages](#shared-storages)
- [Firewall Policies](#firewall-policies)
- [Load Balancers](#load-balancers)
- [Public IPs](#public-ips)
- [Private Networks](#private-networks)
- [Monitoring Center](#monitoring-center)
- [Monitoring Policies](#monitoring-policies)
- [Logs](#logs)
- [Users](#users)
- [Usages](#usages)
- [Server Appliances](#server-appliances)
- [DVD ISO](#dvd-iso)
- [Data Centers](#datacenters)
- [Pricing](#pricing)
- [Ping](#ping)
- [Ping Auth](#ping-auth)
- [VPN's](#vpn)
- [Roles](#roles)
- [Block Storages](#block-storages)
- [SSH Keys](#ssh-keys)


## The 'wait_for' Method


Use the `wait_for()` method on any major class object to poll its resource until an `"ACTIVE"`, `"ENABLED"`, `"POWERED_ON"`, or `"POWERED_OFF"` state is returned.  This is necessary when chaining together multiple actions that take some time to deploy.  The `wait_for()` method is available on the `Server`, `Image`, `SharedStorage`, `Vpn`, `FirewallPolicy`, `LoadBalancer`, `PrivateNetwork`, and `MonitoringPolicy` classes.  It returns a dictionary containing the execution duration.  See the example below:
```
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd, LoadBalancer, LoadBalancerRule

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



# Add Load Balancer to New Server IP
lb_response = client.add_load_balancer(server_id=new_server['id'],
                                       ip_id=server1.first_ip['id'],
                                       load_balancer_id=new_load_balancer['id']
                                       )

## Wait for Load Balancer to be added
print 'Adding load balancer to Server...'
server1.wait_for()
```


## Class Helper Methods

In addition to the `wait_for()` method, all of the classes mentioned above are also equipped with helper methods that retrieve resources without the need to pass in an ID. For example:

```
from oneandone.client import OneAndOneService
from oneandone.client import Server, Hdd

client = OneAndOneService('<API-TOKEN>')


# Create another server, as we did in the above example

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


# After creating a server, you can then call a helper method from the Server object you instantiated

server1_info = server1.get()

# This will return the same JSON as:

server1_info = client.get_server(server_id=new_server['id'])
```

The helper methods for each class are as follows:

**Server**

`get()` - retrieves the current server specs.

`hardware()` - retrieves the current server hardware configurations.

`hdds()` - retrieves a list of the HDDs currently attached to the server.

`image()` - retrieves information about a server's image.

`ips()` - retrieves a list of the server's IPs.

`status()` - retrieves the server's current status.

`dvd()` - retrieves information about the DVD loaded into the virtual DVD unit of a server.

`private_networks()` - retrieves a list of the server's private networks.

`snapshots()` - retrieves a list of the server's snapshots.

**Image**

`get()` - retrieves the current image specs.

**SharedStorage**

`get()` - retrieves the current shared storage specs.

`servers()` - retrieves a list of the servers currently attached to the shared storage.

**FirewallPolicy**

`get()` - retrieves the current firewall policy specs.

`ips()` - retrieves a list of the servers/IPs attached to the firewall policy.

`rules()` - retrieves a list of the rules for the firewall policy.

**LoadBalancer**

`get()` - retrieves the current load balancer specs.

`ips()` - retrieves a list of the servers/IPs attached to the load balancer.

`rules()` - retrieves a list of the rules for the load balancer.

**PrivateNetwork**

`get()` - retrieves the current private network specs.

`servers()` - retrieves a list of the servers currently attached to the private network.

**MonitoringPolicy**

`get()` - retrieves the current monitoring policy specs.

`ports()` - retrieves a list of the ports of the monitoring policy.

`processes()` - retrieves a list of the processes of the monitoring policy.

`servers()` - retrieves a list of the servers currently attached to the monitoring policy.


## Servers


**List all servers:**

`servers = client.list_servers()`


**Retrieve a single server:**

`server = client.get_server(server_id='')`


**List fixed server flavors:**

`fixed_servers = client.fixed_server_flavors()`


**Retrieve information about a fixed server flavor:**

`fixed_server = client.get_fixed_server(fixed_server_id='')`


**Retrieve information about a server's hardware:**

`hardware = client.get_server_hardware(server_id='')`


**List a server's HDDs:**

`hdds = client.list_server_hdds(server_id='')`


**Retrieve a single server HDD:**

`hdd = client.get_server_hdd(server_id='', hdd_id='')`


**Retrieve information about a server's image:**

`image = client.get_server_image(server_id='')`


**List a server's IPs:**

`ips = client.list_server_ips(server_id='')`


**Retrieve information about a single server IP:**

`ip = client.get_server_ip(server_id='', ip_id='')`


**List all firewall policies assigned to a server IP:**

`firewalls = client.list_ip_firewall_policy(server_id='', ip_id='')`


**List all load balancers assigned to a server IP:**

`load_balancers = client.list_ip_load_balancers(server_id='', ip_id='')`


**Retrieve information about a server's status:**

`status = client.get_server_status(server_id='')`


**Retrieve information about the DVD loaded into the virtual DVD unit of a server:**

`dvd_info = client.get_server_dvd(server_id='')`


**List a server's private networks:**

`private_networks = client.list_server_private_networks(server_id='')`


**Retrieve information about a server's private network:**

`private_network = client.private_network_info(server_id='', private_network_id='')`


**List all server snapshots:**

`snapshots = client.list_server_snapshots(server_id='')`


**Create a fixed server:**

*Note:* `appliance_id` takes an `image_id` string
```
server1 = Server(name='Example Server',
                 fixed_instance_id='<FIXED-ID>',
                 appliance_id='<IMAGE-ID>')


response = client.create_server(server=server1)
```


**Create a custom server:**

*Note:* `hdds` must receive an array with at least one object

*Note:* A Hdd's `size` must be a multiple of `20`

*Note:* `appliance_id` takes an `image_id` string
```
server1 = Server(name='Example Server',
                 vcore=1,
                 cores_per_processor=1,
                 ram=1,
                 appliance_id='<IMAGE-ID>')

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]

response = client.create_server(server=server1, hdds=hdds)
```


**Create a server with SSH Key access:**

*Note:* `hdds` must receive an array with at least one object

*Note:* A Hdd's `size` must be a multiple of `20`

*Note:* `appliance_id` takes an `image_id` string
```
pub_key = '<PUB-KEY>'

server1 = Server(name='Example Server',
                 vcore=1,
                 cores_per_processor=1,
                 ram=1,
                 appliance_id='<IMAGE-ID>',
                 rsa_key=pub_key)

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]

response = client.create_server(server=server1, hdds=hdds)
```


**Create a server with SSH Key access and explicitly declare your datacenter:**

*Note:* `hdds` must receive an array with at least one object

*Note:* A Hdd's `size` must be a multiple of `20`

*Note:* `appliance_id` takes an `image_id` string

*Note:* `appliance_id` location must match datacenter location (ex. DE and DE)
```
pub_key = '<PUB-KEY>'
datacenter = '<DATACENTER-ID>'

server1 = Server(name='Example Server',
                 vcore=1,
                 cores_per_processor=1,
                 ram=1,
                 appliance_id='<IMAGE-ID>',
                 rsa_key=pub_key,
                 datacenter_id=datacenter)

hdd1 = Hdd(size=120, is_main=True)
hdds = [hdd1]

response = client.create_server(server=server1, hdds=hdds)
```


**Add a new IP to the server:**

`response = client.add_new_ip(server_id='')`


**Add a new load balancer to the IP:**

`response = client.add_load_balancer(server_id='', ip_id='', load_balancer_id='')`


**Assign a private network to the server:**

`response = client.assign_private_network(server_id='', private_network_id='')`


**Create a snapshot:**

`new_snapshot = client.create_snapshot(server_id='')`


**Clone a server:**

`cloned_server = client.clone_server(server_id='', name='Clone Server')`


**Modify a server:**

`response = client.modify_server(server_id='', name='New Name', description='New Description')`


**Modify server hardware:**

*Note:* Cannot perform "hot" decreasing of server hardware values.  "Cold" decreasing is allowed.

`response = client.modify_server_hardware(server_id='', vcore=2, ram=6)`


**Modify a HDD:**

*Note:* `size` must be a multiple of `20`

`response = client.modify_hdd(server_id='', hdd_id='', size=80)`


**Add a firewall policy to the IP:**

`response = client.add_firewall_policy(server_id='', ip_id='', firewall_id='')`


**Modify a server's status:**

*Note:* `action` can be set to `POWER_OFF`, `POWER_ON`, `REBOOT`

*Note:* `method` can be set to `SOFTWARE` or `HARDWARE`

`response = client.modify_server_status(server_id='', action='REBOOT', method='SOFTWARE')`


**Stop a server:**

`response = client.stop_server(server_id='')`


**Start a server:**

`response = client.start_server(server_id='')`


**Load a DVD into the virtual DVD unit of a server:**

`response = client.load_dvd(server_id='', dvd_id='')`


**Restore a snapshot into the server:**

`response = client.restore_snapshot(server_id='', snapshot_id='')`


**Reinstall an image into a server:**

`response = client.reinstall_image(server_id='', image_id='')`


**Delete a server:**

*Note:* Set `keep_ips` to `True` to keep server IPs after deleting a server. (`False` by default)

`response = client.delete_server(server_id='')`


**Remove a server HDD:**

`response = client.remove_hdd(server_id='', hdd_id='')`


**Release an IP and optionally remove it:**

*Note:* Set `keep_ip` to `True` for releasing the IP without deleting it permanently. (`False` by default)

`response = client.remove_ip(server_id='', ip_id='')`

**Remove a load balancer from the IP:**

`response = client.remove_load_balancer(server_id='', ip_id='', load_balancer_id='')`


**Remove a private network from the server:**

`response = client.remove_private_network(server_id='', private_network_id='')`


**Unload a DVD from the virtual DVD unit of a server:**

`response = client.eject_dvd(server_id='')`


**Remove a snapshot:**

`response = client.delete_snapshot(server_id='', snapshot_id='')`



## Images


**List all images:**

`images = client.list_images()`


**Retrieve a single image:**

`image = client.get_image(image_id='')`


**Create an image:**

*Note:* `image` must receive an `Image` object

*Note:* `frequency` can be set to `'ONCE', 'DAILY'`, or `'WEEKLY'`

*Note:* `num_images` must be an integer between `1` and `50`
```
image1 = Image(server_id='',
               name='Test Image',
               description='Test Description',
               frequency='WEEKLY',
               num_images=1
               )

new_image = client.create_image(image=image1)
```


**Modify an image:**

*Note:* `frequency` can only be changed to `'ONCE'`
```
modified_image = client.modify_image(image_id='',
                                     name='New Image Name',
                                     description='New Description',
                                     frequency='ONCE'
                                     )
```


**Delete an image:**

`response = client.delete_image(image_id='')`




## Shared Storages


**List all shared storages:**

`storages = client.list_shared_storages()`


**Retrieve a single shared storage:**

`storage = client.get_shared_storage(shared_storage_id='')`


**List all servers attached to a shared storage:**

`servers = client.list_servers_attached_storage(shared_storage_id='')`


**Retrieve a server attached to a shared storage:**

`server = client.get_shared_storage_server(shared_storage_id='', server_id=''`


**Retrieve shared storage credentials:**

`credentials = client.get_credentials()`


**Create a shared storage:**

*Note:* `shared_storage` must receive a `SharedStorage` object

*Note:* `size` must be a multiple of `50`

```
storage1 = SharedStorage(name='Test Storage',
                         description='Test Description',
                         size=50
                         )

new_storage = client.create_shared_storage(shared_storage=storage1)
```


**Attach servers to a shared storage:**

*Note:* `server_ids` must receive a list with at least one `AttachServer` object

*Note:* `rights` can be set to either `'R'` or `'RW'`. (Read or Read/Write)
```
server1 = AttachServer(server_id='', rights='R')
server2 = AttachServer(server_id='', rights='RW')

servers = [server1, server2]

response = client.attach_server_shared_storage(shared_storage_id='', server_ids=servers)
```


**Modify a shared storage:**

*Note:* `size` must be a multiple of `50`

```
modified_storage = client.modify_shared_storage(shared_storage_id='',
                                                name='New Name',
                                                description='New Description',
                                                size=100
                                                )
```


**Change the password for accessing a shared storage:**

`response = client.change_password(password='')`


**Delete a shared storage:**

`response = client.delete_shared_storage(shared_storage_id='')`


**Detach a server from a shared storage:**

`response = client.detach_server_shared_storage(shared_storage_id='', server_id='')`




## Firewall Policies


**List all firewall policies:**

`firewall_policies = client.list_firewall_policies()`


**Retrieve a single firewall policy:**

`firewall_policy = client.get_firewall(firewall_id='')`


**List all servers attached to a firewall_policy:**

`servers = client.list_firewall_servers(firewall_id='')`


**Retrieve a server attached to a firewall policy:**

`server = client.get_firewall_server(firewall_id='', server_ip_id='')`


**List the rules for a firewall policy:**

`rules = client.list_firewall_policy_rules(firewall_id='')`


**Retrieve a single firewall policy rule:**

`rule = client.get_firewall_policy_rule(firewall_id='', rule_id='')`


**Create a firewall policy:**

*Note:* `firewall_policy` must receive a `FirewallPolicy` object

*Note:* `firewall_policy_rules` must receive a list with at least one `FirewallPolicyRule` object
```
fp1 = FirewallPolicy(name='Test Firewall Policy', description='Test Description')


rule1 = FirewallPolicyRule(protocol='TCP', port=80, source='0.0.0.0', action='allow')

rule2 = FirewallPolicyRule(protocol='UDP', port=443, source='0.0.0.0', action='allow')

rules = [rule1, rule2]


new_firewall = client.create_firewall_policy(firewall_policy=fp1, firewall_policy_rules=rules)
```


**Add new rules to a firewall policy:**

*Note:* `firewall_policy_rules` must receive a list with at least one `FirewallPolicyRule` object
```
new_rule1 = FirewallPolicyRule(protocol='TCP', port=90, source='0.0.0.0', action='allow')

new_rule2 = FirewallPolicyRule(protocol='TCP', port=333, source='0.0.0.0', action='allow')

new_rules = [new_rule1, new_rule2]


response = client.add_firewall_policy_rule(firewall_id='', firewall_policy_rules=new_rules)
```


**Attach servers to a firewall policy:**

*Note:* `server_ips` must receive a list with at least one `AttachServer` object

*Note:* `server_ip_id` is different from `server_id`.  Use `list_server_ips()` or `get_server_ip()`
to retreive the ID for a server IP
```
server1 = AttachServer(server_ip_id='')

server2 = AttachServer(server_ip_id='')

servers = [server1, server2]


response = client.attach_server_firewall_policy(firewall_id='', server_ips=servers)
```


**Modify a firewall policy:**

`modified_firewall = client.modify_firewall(name='New Name', description='New Description')`


**Delete a firewall policy:**

`response = client.delete_firewall(firewall_id='')`


**Remove a rule from a firewall policy:**

`response = client.remove_firewall_rule(firewall_id='', rule_id='')`


## Load Balancers


**List all load balancers:**

`load_balancers = client.list_load_balancers()`


**Retrieve a single load balancer:**

`load_balancer = client.get_load_balancer(load_balancer_id='')`


**List all servers attached to a load balancer:**

`servers = client.list_load_balancer_servers(load_balancer_id='')`


**Retrieve a server attached to a load balancer:**

*Note:* `server_ip_id` is different from `server_id`.  Use `list_server_ips()` or `get_server_ip()`
to retreive the ID for a server IP

`server = client.get_load_balancer_server(load_balancer_id='', server_ip_id='')`


**List all load balancer rules:**

`rules = client.load_balancer_rules(load_balancer_id='')`


**Retrieve a load balancer rule:**

`rule = client.get_load_balancer_rule(load_balancer_id='', rule_id='')`


**Create a load balancer:**

*Note:* `load_balancer` must receive a `LoadBalancer` object

*Note:* `load_balancer_rules` must receive a list with at least one `LoadBalancerRule` object

*Note:* `health_check_test` can only be set to `'TCP'` at the moment

*Note:* `health_check_interval` can range from `5` to `300` seconds

*Note:* `persistence_time` is required if `persistence` is enabled, and can range from `30` to `1200` seconds

*Note:* `method` can be set to `'ROUND_ROBIN'` or `'LEAST_CONNECTIONS'`
```
lb1 = LoadBalancer(name='Test Load Balancer',
                   description='Test Description',
                   health_check_test='TCP',
                   health_check_interval=40,
                   persistence=True,
                   persistence_time=1200,
                   method='ROUND_ROBIN'
                  )

rule1 = LoadBalancerRule(protocol='TCP', port_balancer=80, port_server=80, source='0.0.0.0')
rule2 = LoadBalancerRule(protocol='TCP', port_balancer=9999, port_server=8888, source='0.0.0.0')

rules = [rule1, rule2]

new_load_balancer = client.create_load_balancer(load_balancer=lb1, load_balancer_rules=rules)
```


**Attach servers to a load balancer:**

*Note:* `server_ips` must receive a list with at least one `AttachServer` object

*Note:* `server_ip_id` is different from `server_id`.  Use `list_server_ips()` or `get_server_ip()`
to retreive the ID for a server IP
```
server1 = AttachServer(server_ip_id='')
server2 = AttachServer(server_ip_id='')
servers = [server1, server2]


response = client.attach_load_balancer_server(load_balancer_id='', server_ips=servers)
```


**Add rules to a load balancer:**

*Note:* `load_balancer_rules` must receive a list with at least one `LoadBalancerRule` object
```
rule1 = LoadBalancerRule(protocol='TCP', port_balancer=99, port_server=99, source='0.0.0.0')
rule2 = LoadBalancerRule(protocol='TCP', port_balancer=125, port_server=521, source='0.0.0.0')
rules = [rule1, rule2]


response = client.add_load_balancer_rule(load_balancer_id='', load_balancer_rules=rules)
```


**Modify a load balancer:**

```
modified_load_balancer = client.modify_load_balancer(name='New Name',
                                                     description='New Description',
                                                     health_check_test='NONE',
                                                     persistence=False,
                                                     method='LEAST_CONNECTIONS'
                                                    )
```


**Delete a load balancer:**

`response = client.delete_load_balancer(load_balancer_id='')`


**Remove a server from a load balancer:**

*Note:* `server_ip_id` is different from `server_id`.  Use `list_server_ips()` or `get_server_ip()`
to retreive the ID for a server IP

`response = client.remove_load_balancer_server(load_balancer_id='', server_ip_id='')`


**Remove a rule from a load balancer:**

`response = client.remove_load_balancer_rule(load_balancer_id='', rule_id='')`



## Public IPs


**List all of your public IPs:**

`public_ips = client.list_public_ips()`


**Retrieve a single public IP:**

`public_ip = client.get_public_ip(ip_id='')`


**Create a public IP:**

*Note:* `reverse_dns` is an optional parameter

`new_public_ip = client.create_public_ip(reverse_dns='example.com')`


**Modify a public IP:**

*Note:* If you call this method without a `reverse_dns` argument, it will remove the previous `reverse_dns` value

`modified_ip = client.modify_public_ip(ip_id='', reverse_dns='newexample.com')`


**Delete a public IP:**

`response = client.delete_public_ip(ip_id='')`



## Private Networks


**List all private networks:**

`private_networks = client.list_private_networks()`


**Retrieve a single private network:**

`private_network = client.get_private_network(private_network_id='')`


**List all servers attached to a private network:**

`servers = client.list_private_network_servers(private_network_id='')`


**Retrieve a server attached to a private network:**

`server = client.get_private_network_server(private_network_id='', server_id='')`


**Create a private network:**

*Note:* `private_network` must receive a `PrivateNetwork` object

*Note:* `name` is the only required parameter
```
pn1 = PrivateNetwork(name='Test Name',
                     description='Test Description',
                     network_address='192.168.1.0',
                     subnet_mask='255.255.255.0'
                     )

new_private_network = client.create_private_network(private_network=pn1)
```


**Attach servers to a private network:**

*Note:* `server_ids` must receive a list with at least one `AttachServer` object

*Note:* Servers cannot be attached or removed from a private network if they currently have a snapshot. Use
`delete_snapshot()` to remove a server's snapshot first
```
server1 = AttachServer(server_id='')
server2 = AttachServer(server_id='')
servers = [server1, server2]

response = client.attach_private_network_servers(private_network_id='', server_ids=servers)
```


**Modify a private network:**

`modified_private_network = client.modify_private_network(private_network_id='', name='New Name')`


**Delete a private network:**

`response = client.delete_private_network(private_network_id='')`


**Remove a server from a private network:**

*Note:* Servers cannot be attached or removed from a private network if they currently have a snapshot. Use
`delete_snapshot()` to remove a server's snapshot first

*Note:* Servers cannot be removed from a private network when they are 'online'.  Use `modify_server_status()`
to power down the server first

`response = client.remove_private_network_server(private_network_id='', server_id='')`


## Monitoring Center


**List all usages and alerts of monitoring servers:**

`usages = client.list_server_usages()`


**Retrieve the usages and alerts for a monitoring server:**

*Note:* `period` can be set to `'LAST_HOUR'`, `'LAST_24H'`, `'LAST_7D'`, `'LAST_30D'`, `'LAST_365D'`, or `'CUSTOM'`

*Note:* If `period` is set to `'CUSTOM'`, the `start_date` and `end_date` parameters are required.  They should be
set using the following date/time format: `2015-19-05T00:05:00Z`

`usage = client.get_usage(server_id='', period='LAST_24H')`



## Monitoring Policies


**List all monitoring policies:**

`monitoring_policies = client.list_monitoring_policies()`


**Retrieve a single monitoring policy:**

`monitoring_policy = client.get_monitoring_policy(monitoring_policy_id='')`


**List all ports of a monitoring policy:**

`ports = client.list_monitoring_policy_ports(monitoring_policy_id='')`


**Retrieve a port of a monitoring policy:**

`port = client.get_monitoring_policy_port(monitoring_policy_id='', port_id='')`


**List all processes of a monitoring policy:**

`processes = client.list_monitoring_policy_processes(monitoring_policy_id='')`


**Retrieve a process of a monitoring policy:**

`process = client.get_monitoring_policy_process(monitoring_policy_id='', process_id='')`


**List all servers attached to a monitoring policy:**

`servers = client.list_monitoring_policy_servers(monitoring_policy_id='')`


**Retrieve a server attached to a monitoring policy:**

`server = client.get_monitoring_policy_server(monitoring_policy_id='', server_id='')`


**Create a monitoring policy:**

*Note:* `monitoring_policy` must receive a `MonitoringPolicy` object

*Note:* `thresholds` must receive a list with the following `Threshold` objects: `cpu`, `ram`, `disk`, `transfer`, `internal_ping`

*Note:* `ports` must receive a list with at least one `Port` object

*Note:* `processes` must receive a list with at least one `Process` object
```
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


**Add new ports to a monitoring policy:**

*Note:* `ports` must receive a list with at least one `Port` object
```
port3 = Port(protocol='TCP',
             port=66,
             alert_if='RESPONDING',
             email_notification=False
             )

ports = [port3]

response = client.add_port(monitoring_policy_id='', ports=ports)
```


**Add new processes to a monitoring policy:**

*Note:* `processes` must receive a list with at least one `Process` object
```
process3 = Process(process='Third Test',
                   alert_if='RUNNING',
                   email_notification=True
                   )

processes = [process3]


response = client.add_process=(monitoring_policy_id='', processes=processes)
```


**Attach servers to a monitoring policy:**

*Note:* `servers` must receive a list with at least one `AttachServer` object
```
server1 = AttachServer(server_id='')
server2 = AttachServer(server_id='')

servers = [server1, server2]

response = client.attach_monitoring_policy_server(monitoring_policy_id='', servers=servers)
```

**Modify a monitoring policy:**

*Note:* `monitoring_policy` is not a required parameter, but it must receive a `MonitoringPolicy` object if you do choose to update.

*Note:* `thresholds` is not a required parameter, but it must receive a list with at least one `Threshold` object if you do choose to update.
```
modified_mp = MonitoringPolicy(name='New Name',
                               description='New Description',
                               email='new_email@example.com'
                               )

modified_cpu = Threshold(entity='cpu',
                         warning_value=80,
                         warning_alert=True,
                         critical_value=90,
                         critical_alert=True
                         )

modified_ram = Threshold(entity='ram',
                         warning_value=80,
                         warning_alert=True,
                         critical_value=90,
                         critical_alert=True
                         )

modified_disk = Threshold(entity='disk',
                          warning_value=70,
                          warning_alert=True,
                          critical_value=80,
                          critical_alert=True
                          )


thresholds = [modified_cpu, modified_ram, modified_disk]


modified_monitoring_policy = client.modify_monitoring_policy(monitoring_policy_id='',
                                                             monitoring_policy=modified_mp,
                                                             thresholds=thresholds
                                                             )
```


**Modify a port from a monitoring policy:**

*Note:* Only `alert_if` and `email_notification` can be updated.  `protocol` and `port` are immutable.
```
modified_port = Port(alert_if='NOT_RESPONDING', email_notification=True)


response = client.modify_port(monitoring_policy_id='', port_id='', port=modified_port)
```


**Modify a process from a monitoring policy:**

*Note:* Only `alert_if` and `email_notification` can be updated.  `process` is immutable.
```
modified_process = Process(alert_if='NOT_RUNNING', email_notification=True)


response = client.modify_process(monitoring_policy_id='', process_id='', process=modified_process)
```


**Delete a monitoring policy:**

`response = client.delete_monitoring_policy(monitoring_policy_id='')`


**Remove a port from a monitoring policy:**

`response = client.delete_monitoring_policy_port(monitoring_policy_id='', port_id='')`


**Remove a process from a monitoring policy:**

`response = client.delete_monitoring_policy_process(monitoring_policy_id='', process_id='')`


**Detach a server from a monitoring policy:**

`response = client.detach_monitoring_policy_server(monitoring_policy_id='', server_id='')`



## Logs


**List all logs:**

*Note:* `period` can be set to `'LAST_HOUR'`, `'LAST_24H'`, `'LAST_7D'`, `'LAST_30D'`, `'LAST_365D'`, or `'CUSTOM'`

*Note:* If `period` is set to `'CUSTOM'`, the `start_date` and `end_date` parameters are required.  They should be
set using the following date/time format: `2015-19-05T00:05:00Z`

`logs = client.list_logs(period='LAST_24H')`


**Retrieve a single log:**

`log = client.get_log(log_id='')`



## Users


**List all users:**

`users = client.list_users()`


**Retrieve information about a user:**

`user = client.get_user(user_id='')`


**Retrieve information about a user's API privileges:**

`api_info = client.api_info(user_id='')`


**Retrieve a user's API key:**

`api_key = client.show_api_key(user_id='')`


**List IPs from which API access is allowed for a user:**

`ips_allowed = client.ips_api_access_allowed(user_id='')`


**Create a user:**

```
new_user = client.create_user(name='Test User',
                              password='testing123',
                              email='test@example.com',
                              description='Test Description'
                              )
```


**Add new IPs to a user:**

*Note:* `user_ips` must receive a list with at least one IP string
```
ip1 = '12.54.127.11'
ip2 = '14.97.4.171'

ips = [ip1, ip2]

response = client.add_user_ip(user_id='', user_ips=ips)
```


**Modify user information:**

*Note:* `state` can be set to `ACTIVE` or `DISABLE`

`response = client.modify_user(user_id='', description='', email='', password='', state='ACTIVE')`


**Modify a user's API privileges:**

`response = client.modify_user_api(user_id='', active=True)`


**Change a user's API key:**

`response = client.change_api_key(user_id='')`


**Delete a user:**

`response = client.delete_user(user_id='')`


**Remove an IP and forbid API access from it:**

`response = client.remove_user_ip(user_id='', ip='14.97.4.171')`



## Usages


**List all usages:**

*Note:* `period` can be set to `'LAST_HOUR'`, `'LAST_24H'`, `'LAST_7D'`, `'LAST_30D'`, `'LAST_365D'`, or `'CUSTOM'`

*Note:* If `period` is set to `'CUSTOM'`, the `start_date` and `end_date` parameters are required.  They should be
set using the following date/time format: `2015-19-05T00:05:00Z`

`usages = client.list_usages(period='LAST_24H')`



## Server Appliances


**List all of the appliances that you can use for creating a server:**

`server_appliances = client.list_appliances()`


**Retrieve a specific appliance:**

`server_appliance = client.get_appliance(appliance_id='')`



## DVD ISO


**List all operating systems and tools that you can load into your virtual DVD unit:**

`dvds = client.list_dvds()`


**Retrieve a specific ISO image:**

`dvd = client.get_dvd(iso_id='')`



# <a name="datacenters"></a>Data Centers


**List all available data centers:**

```
response = client.list_datacenters()
```


**Returns information about a data center:**

```
response = client.get_datacenter(datacenter_id='<DATACENTER-ID>')
```



# <a name="pricing"></a>Pricing


**List pricing for all available resources in Cloud Panel:**

```
response = client.pricing()
```



# <a name="ping"></a>Ping


**Returns `"PONG"` if the API is running:**

```
response = client.ping()
```



# <a name="ping-auth"></a>Ping Auth


**Returns `"PONG"` if the API is running and your token is valid:**

```
response = client.ping_auth()
```



# <a name="vpn"></a>VPN's


**List all VPN's:**

```
response = client.list_vpns()
```


**Retrieve a single VPN:**

```
response = client.get_vpn(vpn_id='<VPN-ID>')
```


**Create a VPN:**

```
my_vpn = Vpn(name='Example VPN', datacenter_id='<DC-ID>')

response = client.create_vpn(vpn=my_vpn)
```


**Modify a VPN:**

```
response = client.modify_vpn(vpn_id='<VPN-ID>', name='New Name')
```


**Delete a VPN:**

```
response = client.delete_vpn(vpn_id='<VPN-ID>')
```


**Download a VPN's config file:**

```
response = client.download_config(vpn_id='<VPN-ID>')
```



# <a name="roles"></a>Roles


**List all available roles on your account:**

```
response = client.list_roles()
```


**Retrieve a single role:**

```
response = client.get_role(role_id='<ROLE-ID>')
```


**Create a role:**

```
response = client.create_role(name='Example Role')
```


**Modify a role:**

```
response = client.modify_role(role_id='<ROLE-ID>', name='New Name',
                              state='ACTIVE')
```


**Delete a role:**

```
response = client.delete_role(role_id='<ROLE-ID>')
```



**List a role's permissions:**

```
response = client.permissions(role_id='<ROLE-ID>')
```



**Modify a role's permissions:**

```
server_perms = {
  'show': True,
  'create': True,
  'delete': False
}

response = client.modify_permissions(role_id='<ROLE-ID>', servers=server_perms)
```



**List the users assigned to a role:**

```
response = client.role_users(role_id='<ROLE-ID>')
```



**Assign new users to a role:**

```
users = ['<USER1-ID>', '<USER2-ID>']

response = client.add_users(role_id='<ROLE-ID>', users=users)
```



**Returns information about a user assigned to a role:**

```
response = client.get_role_user(role_id='<ROLE-ID>', user_id='<USER-ID>')
```



**Unassign a user from a role:**

```
response = client.remove_user(role_id='<ROLE-ID>', user_id='<USER-ID>')
```



**Clone a role:**

```
response = client.clone_role(role_id='<ROLE-ID>', name='Role Clone')
```



# <a name="block-storages"></a>Block Storages


**List all available block storages on your account:**

```
response = client.list_block_storages()
```


**Retrieve a single block storage:**

```
response = client.get_block_storage(block_storage_id='<BLOCK-STORAGE-ID>')
```


**Create a block storage:**

```
block_storage = BlockStorage(name='My new block storage',
                             description='My block storage description',
                             size=20,
                             datacenter_id='<DATACENTER-ID>')

response = client.create_block_storage(block_storage)
```


**Modify a block storage:**

```
response = client.modify_block_storage(block_storage_id='<BLOCK-STORAGE-ID>', name='New name', description='New Description')
```


**Delete a block storage:**

```
response = client.delete_block_storage(block_storage_id='<BLOCK-STORAGE-ID>')
```


**Attach a block storage to a server:**

```
response = client.attach_block_storage(block_storage_id='<BLOCK-STORAGE-ID>', server_id='<SERVER-ID>')
```


**Detach a block storage from a server:**

```
response = client.detach_block_storage(block_storage_id='<BLOCK-STORAGE-ID>')
```



# <a name="ssh-keys"></a>SSH Keys


**List all available ssh keys on your account:**

```
response = client.list_ssh_keys()
```


**Retrieve a single ssh key:**

```
response = client.get_ssh_key(role_id='<SSH-KEY-ID>')
```


**Create an ssh key:**

```
ssh_key = SshKey(name='Test SSH Key', description='Test Description', public_key='<PUBLIC-KEY>')

response = client.create_ssh_key(ssh_key)
```


**Modify an ssh key:**

```
response = client.modify_ssh_key(ssh_key_id='<SSH-KEY-ID>',
                                 name='New Name',
                                 description='New Description')
```


**Delete an ssh key:**

```
response = client.delete_ssh_key(ssh_key_id='<SSH-KEY-ID>')
```
