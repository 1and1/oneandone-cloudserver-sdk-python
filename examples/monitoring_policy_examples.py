# List all monitoring policies
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

monitoring_policies = client.list_monitoring_policies()

# Retrieve a monitoring policy
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

monitoring_policy = client.get_monitoring_policy(monitoring_policy_id='')

# List all ports of a monitoring policy
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

ports = client.list_monitoring_policy_ports(monitoring_policy_id='')

# Retrieve a monitoring policy port
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

port = client.get_monitoring_policy_port(monitoring_policy_id='', port_id='')

# List all processes of a monitoring policy
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

processes = client.list_monitoring_policy_processes(monitoring_policy_id='')

# Retrieve a monitoring policy process
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

process = client.get_monitoring_policy_process(monitoring_policy_id='',
		process_id='')


# List all monitoring policy servers
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

servers = client.list_monitoring_policy_servers(monitoring_policy_id='')

# Retrieve a monitoring policy server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server = client.get_monitoring_policy_server(monitoring_policy_id='',
		server_id='')

# Create a monitoring policy
from oneandone.client import OneAndOneService
from oneandone.client import MonitoringPolicy, Threshold, Port, Process

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

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


process1 = Process(process='Test',
                   alert_if='NOT_RUNNING',
                   email_notification=True
                   )

process2 = Process(process='Another Test',
                   alert_if='NOT_RUNNING',
                   email_notification=True
                   )

processes = [process1, process2]


new_monitoring_policy = client.create_monitoring_policy(monitoring_policy=mp1,
                                                        thresholds=thresholds,
                                                        ports=ports,
                                                        processes=processes
                                                        )

# Add new ports to a monitoring policy
from oneandone.client import OneAndOneService
from oneandone.client import Port

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

port3 = Port(protocol='TCP',
             port=66,
             alert_if='RESPONDING',
             email_notification=False
             )

ports = [port3]

response = client.add_port(monitoring_policy_id='', ports=ports)

# Add new processes to a monitoring policy
from oneandone.client import OneAndOneService
from oneandone.client import Process

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

process3 = Process(process='Third Test',
                   alert_if='RUNNING',
                   email_notification=True
                   )

processes = [process3]


response = client.add_process=(monitoring_policy_id='', processes=processes)

# Attach servers to a monitoring policy
from oneandone.client import OneAndOneService
from oneandone.client import AttachServer

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

server1 = AttachServer(server_id='')
server2 = AttachServer(server_id='')

servers = [server1, server2]

response = client.attach_monitoring_policy_server(monitoring_policy_id='',
		servers=servers)

# Modify a monitoring policy
from oneandone.client import OneAndOneService
from oneandone.client import MonitoringPolicy, Threshold

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

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
		monitoring_policy=modified_mp, thresholds=thresholds)

# Modify a monitoring policy port
from oneandone.client import OneAndOneService
from oneandone.client import Port

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_port = Port(alert_if='NOT_RESPONDING', email_notification=True)

response = client.modify_port(monitoring_policy_id='', port_id='',
		port=modified_port)

# Modify a monitoring policy process
from oneandone.client import OneAndOneService
from oneandone.client import Process

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

modified_process = Process(alert_if='NOT_RUNNING', email_notification=True)

response = client.modify_process(monitoring_policy_id='', process_id='',
		process=modified_process)

# Delete a monitoring policy
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_monitoring_policy(monitoring_policy_id='')

# Remove a port
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_monitoring_policy_port(monitoring_policy_id='',
		port_id='')

# Remove a process
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.delete_monitoring_policy_process(monitoring_policy_id='',
		process_id='')

# Detach a server
from oneandone.client import OneAndOneService

client = OneAndOneService('675fbe491b27896b57e76867604f8255')

response = client.detach_monitoring_policy_server(monitoring_policy_id='',
		server_id='')

