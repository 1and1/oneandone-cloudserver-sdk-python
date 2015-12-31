Monitoring Policies
********************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_monitoring_policies(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of your monitoring policies.

   :param page: Allows the use of pagination. Indicate which page to start on.
   :type page: ``int``

   :param per_page: Number of items per page.
   :type per_page: ``int``

   :param sort: ``sort='name'`` retrieves a list of elements sorted 
   		alphabetically. ``sort='creation_date'`` retrieves a list of elements 
   		sorted by their creation date in descending order.
   :type sort: ``str``

   :param q: ``q`` is for query. Use this parameter to return only the items 
   		that match your search query.
   :type q: ``str``

   :param fields: Returns only the parameters requested. 
   		(i.e. fields='id, name, description, hardware.ram')
   :type fields: ``str``

   :rtype: JSON


.. function:: get_monitoring_policy(monitoring_policy_id=None)

   Retrieve information about a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :rtype: JSON


.. function:: list_monitoring_policy_servers(monitoring_policy_id=None)

   Returns a list of the servers attached to a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :rtype: JSON


.. function:: get_monitoring_policy_server(monitoring_policy_id=None, server_id=None)

   Retrieve information about a server attached to a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param server_id: the unique identifier for a server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: list_monitoring_policy_ports(monitoring_policy_id=None)

   List all ports of a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :rtype: JSON


.. function:: get_monitoring_policy_port(monitoring_policy_id=None, port_id=None)

   Retrieve a port of a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param port_id: the unique identifier for the port.
   :type port_id: ``str``

   :rtype: JSON


.. function:: list_monitoring_policy_processes(monitoring_policy_id=None)

   List all processes of a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :rtype: JSON


.. function:: get_monitoring_policy_process(monitoring_policy_id=None, process_id=None)

   Retrieve a process of a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param process_id: the unique identifier for the process.
   :type process_id: ``str``

   :rtype: JSON


.. function:: create_monitoring_policy(monitoring_policy=None, thresholds=None, ports=None, processes=None)

   Create a monitoring policy.

   :param monitoring_policy: an instantiation of the :class:`MonitoringPolicy` class.
   :type monitoring_policy: ``obj``

   :param thresholds: a list of :class:`Threshold` instances.  Must contain a threshold for ``'cpu'``, ``'ram'``, ``'disk'``, ``'transfer'``, ``'internal_ping'``
   :type thresholds: ``list``

   :param ports: a list of :class:`Port` instances.
   :type ports: ``list``

   :param processes: a list of :class:`Process` instances.
   :type processes: ``list``

   :rtype: JSON


.. function:: add_port(monitoring_policy_id=None, ports=None)

   Add new ports to a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param ports: a list of :class:`Port` instances.
   :type ports: ``list``

   :rtype: JSON


.. function:: add_process(monitoring_policy_id=None, processes=None)

   Add new processes to a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param processes: a list of :class:`Process` instances.
   :type processes: ``list``

   :rtype: JSON


.. function:: attach_monitoring_policy_server(monitoring_policy_id=None, servers=None)

   Attach servers to a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param servers: a list of :class:`AttachServer` instances.
   :type servers: ``list``

   :rtype: JSON


.. function:: modify_monitoring_policy(monitoring_policy_id=None, monitoring_policy=None, thresholds=None)

   Modify a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param monitoring_policy: an instantiation of the :class:`MonitoringPolicy` class.
   :type monitoring_policy: ``obj``

   :param thresholds: a list of :class:`Threshold` instances.
   :type thresholds: ``list``

   :rtype: JSON


.. function:: modify_port(monitoring_policy_id=None, port_id=None, port=None)

   Modify a port from a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param port_id: the unique identifier for the port.
   :type port_id: ``str``

   :param port: an instantiation of the :class:`Port` class.
   :type port: ``obj``

   :rtype: JSON


.. function:: modify_process(monitoring_policy_id=None, process_id=None, process=None)

   Modify a process from a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param process_id: the unique identifier for the port.
   :type process_id: ``str``

   :param process: an instantiation of the :class:`Process` class.
   :type process: ``obj``

   :rtype: JSON


.. function:: delete_monitoring_policy(monitoring_policy_id=None)

   Delete a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :rtype: JSON


.. function:: delete_monitoring_policy_port(monitoring_policy_id=None, port_id=None)

   Remove a port from a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param port_id: the unique identifier for the port.
   :type port_id: ``str``

   :rtype: JSON


.. function:: delete_monitoring_policy_process(monitoring_policy_id=None, process_id=None)

   Remove a process from a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param process_id: the unique identifier for the process.
   :type process_id: ``str``

   :rtype: JSON


.. function:: detach_monitoring_policy_server(monitoring_policy_id=None, server_id=None)

   Detach a server from a monitoring policy.

   :param monitoring_policy_id: the unique identifier for the monitoring policy.
   :type monitoring_policy_id: ``str``

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON



The "MonitoringPolicy" Class
=============================

.. class:: MonitoringPolicy(name=None, description=None, email=None, agent=None)
   
   
   Pass a :class:`MonitoringPolicy` instance into the :func:`create_monitoring_policy` 
   method to create a monitoring policy.  There are also a few helper methods 
   available to perform simple requests after creating your monitoring policy.

   :param name: monitoring policy name.
   :type name: ``str``

   :param description: monitoring policy description.
   :type description: ``str``

   :param email: user's email address.
   :type email: ``str``

   :param agent: Set to ``True`` to use an agent.
   :type agent: ``bool``

   **Methods:**

   .. method:: get()
      
      Retrieves the monitoring policy's current specs.

   .. method:: ports()
      
      Retrieves a list of the ports of the monitoring policy.

   .. method:: processes()
      
      Retrieves a list of the processes of the monitoring policy.

   .. method:: servers()
      
      Retrieves a list of the servers currently attached to the monitoring policy.

   .. method:: wait_for()
      
      Polls the :class:`MonitoringPolicy` resource until an ``ACTIVE``, ``POWERED_ON``, or ``POWERED_OFF`` state is returned.



The "Threshold" Class
==========================

.. class:: Threshold(entity=None, warning_value=None, warning_alert=None, critical_value=None, critical_alert=None)
   
   
   Use the :class:`Threshold` class to add thresholds to a monitoring policy.

   :param entity: threshold name.  Possible values are ``'cpu'``, ``'ram'``, ``'disk'``, ``'transfer'``, ``'internal_ping'``.
   :type entity: ``str``

   :param warning_value: advise when this value is exceeded. (%)
   :type warning_value: ``int``

   :param warning_alert: enable or disable alerts.
   :type warning_alert: ``bool``

   :param critical_value: advise when this value is exceeded. (%)
   :type critical_value: ``int``

   :param critical_alert: enable or disable alerts.
   :type critical_alert: ``bool``


The "Port" Class
==========================

.. class:: Port(protocol=None, port=None, alert_if=None, email_notification=None)
   
   
   Use the :class:`Port` class to add ports to a monitoring policy.

   :param protocol: internet protocol.  Possible values are ``'TCP'`` or ``'UDP'``.
   :type protocol: ``str``

   :param port: port number.
   :type port: ``int``

   :param alert_if: case of alert.  Possible values are ``'RESPONDING'`` or ``'NOT_RESPONDING'``.
   :type alert_if: ``str``

   :param email_notification: elect to receive email notifications in case of alert.
   :type email_notification: ``bool``


The "Process" Class
==========================

.. class:: Process(process=None, alert_if=None, email_notification=None)
   
   
   Use the :class:`Process` class to add processes to a monitoring policy.

   :param process: process name.
   :type process: ``str``

   :param alert_if: case of alert.  Possible values are ``'RUNNING'`` or ``'NOT_RUNNING'``.
   :type alert_if: ``str``

   :param email_notification: elect to receive email notifications in case of alert.
   :type email_notification: ``bool``


The "AttachServer" Class
==========================

.. class:: AttachServer(server_id=None, rights=None, server_ip_id=None)
   
   
   Use the :class:`AttachServer` class to attach servers or server IPs to various containers.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param rights: server rights for accessing a shared storage.  Possible values are ``'R'`` or ``'RW'``.
   :type rights: ``str``

   :param server_ip_id: the unique identifier for the server's IP.
   :type server_ip_id: ``str``