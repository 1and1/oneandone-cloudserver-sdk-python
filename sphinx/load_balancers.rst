Load Balancers
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_load_balancers(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of your load balancers.

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


.. function:: get_load_balancer(load_balancer_id=None)

   Retrieve information about a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :rtype: JSON


.. function:: list_load_balancer_servers(load_balancer_id=None)

   Returns a list of the servers attached to a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :rtype: JSON


.. function:: get_load_balancer_server(load_balancer_id=None, server_ip_id=None)

   Retrieve a information about a server attached to a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param server_ip_id: the unique identifier for a server's IP.  This is different from ``server_id``.
   :type server_ip_id: ``str``

   :rtype: JSON


.. function:: load_balancer_rules(load_balancer_id=None)

   Returns a list of the rules of a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :rtype: JSON


.. function:: get_load_balancer_rule(load_balancer_id=None, rule_id=None)

   Retrieve information about a load balancer rule.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param rule_id: the unique identifier for the load balancer rule.
   :type rule_id: ``str``

   :rtype: JSON


.. function:: modify_load_balancer(load_balancer_id=None, name=None, description=None, health_check_test=None, health_check_interval=None, health_check_path=None, health_check_parse=None, persistence=None, persistence_time=None, method=None)

   Modify a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param name: load balancer name.
   :type name: ``str``

   :param description: load balancer description.
   :type description: ``str``

   :param health_check_test: possible values are ``"NONE"``,``"TCP"``, or ``"HTTP"``.
   :type health_check_test: ``str``

   :param health_check_interval: Health check period in seconds.
   :type health_check_interval: ``int``

   :param health_check_path: Url to call for checking. Required for HTTP health check.
   :type health_check_path: ``str``

   :param health_check_parse: Regular expression to check. Required for HTTP health check.
   :type health_check_parse: ``str``

   :param persistence: enable or disable persistnece.
   :type persistence: ``bool``

   :param persistence_time: Persistence time in seconds. Required if persistence is enabled.
   :type persistence_time: ``int``

   :param method: balancing procedure.  possible values are ``"ROUND_ROBIN"`` or ``"LEAST_CONNECTIONS"``.
   :type method: ``str``

   :rtype: JSON


.. function:: create_load_balancer(load_balancer=None, load_balancer_rules=None)

   Create a load balancer.

   :param load_balancer: an instantiation of the :class:`LoadBalancer` class.
   :type load_balancer: ``obj``

   :param load_balancer_rules: a list of :class:`LoadBalancerRule` instances.
   :type load_balancer_rules: ``list``

   :rtype: JSON


.. function:: attach_load_balancer_server(load_balancer_id=None, server_ips=None)

   Attach servers to a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param server_ips: a list of :class:`AttachServer` instances.
   :type server_ips: ``list``

   :rtype: JSON


.. function:: add_load_balancer_rule(load_balancer_id=None, load_balancer_rules=None)

   Attach rules to a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param load_balancer_rules: a list of :class:`LoadBalancerRule` instances.
   :type load_balancer_rules: ``list``

   :rtype: JSON


.. function:: delete_load_balancer(load_balancer_id=None)

   Delete a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :rtype: JSON


.. function:: remove_load_balancer_server(load_balancer_id=None, server_ip_id=None)

   Remove a server from a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param server_ip_id: the unique identifier for the server's IP.  This is different from ``server_id``.
   :type server_ip_id: ``str``

   :rtype: JSON


.. function:: remove_load_balancer_rule(load_balancer_id=None, rule_id=None)

   Remove a rule from a load balancer.

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :param rule_id: the unique identifier for the load balancer rule.
   :type rule_id: ``str``

   :rtype: JSON


The "LoadBalancer" Class
==========================

.. class:: LoadBalancer(health_check_path=None, health_check_parse=None, name=None, description=None, health_check_test=None, health_check_interval=None, persistence=None, persistence_time=None, method=None)
   
   
   Pass a :class:`LoadBalancer` instance into the :func:`create_load_balancer` 
   method to create a load balancer.  There are also a few helper methods available to perform simple requests after creating your load balancer.

   :param name: load balancer name.
   :type name: ``str``

   :param description: load balancer description.
   :type description: ``str``

   :param health_check_test: possible values are ``"NONE"`` or ``"TCP"``.
   :type health_check_test: ``str``

   :param health_check_interval: Health check period in seconds.  Can range between ``5`` and ``300`` seconds.
   :type health_check_interval: ``int``

   :param health_check_path: Url to call for checking. Required for HTTP health check.
   :type health_check_path: ``str``

   :param health_check_parse: Regular expression to check. Required for HTTP health check.
   :type health_check_parse: ``str``

   :param persistence: enable or disable persistence.
   :type persistence: ``bool``

   :param persistence_time: Persistence time in seconds. Required if persistence is enabled.  Can range from ``30`` to ``1200`` seconds
   :type persistence_time: ``int``

   :param method: balancing procedure.  Possible values are ``"ROUND_ROBIN"`` or ``"LEAST_CONNECTIONS"``.
   :type method: ``str``   


   **Methods:**

   .. method:: get()
      
      Retrieves the load balancer's current specs.

   .. method:: ips()
      
      Returns a list of the server IPs attached to the load balancer.

   .. method:: rules()
      
      Returns a list of the rules attached to the load balancer.

   .. method:: wait_for()
      
      Polls the :class:`LoadBalancer` resource until an ``ACTIVE``, ``POWERED_ON``, or ``POWERED_OFF`` state is returned.


The "LoadBalancerRule" Class
================================

.. class:: LoadBalancerRule(protocol=None, port_balancer=None, port_server=None, source=None)
   
   
   Use the :class:`LoadBalancerRule` class to create or modify load balancer rules.

   :param protocol: internet protocol.  Possible values are ``'TCP'`` and ``'UDP'``.
   :type protocol: ``str``

   :param port_balancer: port in balancer.
   :type port_balancer: ``int``

   :param port_server: port in server.
   :type port_server: ``int``

   :param source: IPs from which access is available. Setting ``0.0.0.0`` means all IPs are allowed.
   :type source: ``str``


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