Servers
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_servers(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all servers.

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


.. function:: get_server(server_id=None)

   Retrieve information about a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: fixed_server_flavors()

   Returns a list of all fixed server flavors.

   :rtype: JSON


.. function:: get_fixed_server(fixed_server_id=None)

   Retrieve information about a fixed server flavor.

   :param fixed_server_id: the unique identifier for the fixed server flavor.
   :type fixed_server_id: ``str``

   :rtype: JSON


.. function:: get_server_hardware(server_id=None)

   Retrieve information about a server's hardware configurations.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: list_server_hdds(server_id=None)

   Returns a list of a server's HDDs.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: get_server_hdd(server_id=None, hdd_id=None)

   Retrieve a single server HDD.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param hdd_id: the unique identifier for the HDD.
   :type hdd_id: ``str``

   :rtype: JSON


.. function:: get_server_image(server_id=None)

   Retrieve information about a server's image.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: list_server_ips(server_id=None)

   Returns a list of a server's IPs.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: get_server_ip(server_id=None, ip_id=None)

   Retrieve information about a single server IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the IP.
   :type ip_id: ``str``

   :rtype: JSON


.. function:: list_ip_firewall_policy(server_id=None, ip_id=None)

   Returns a list of all firewall policies assigned to a server IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the IP.
   :type ip_id: ``str``

   :rtype: JSON


.. function:: list_ip_load_balancers(server_id=None, ip_id=None)

   Returns a list of all load balancers assigned to a server IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the IP.
   :type ip_id: ``str``

   :rtype: JSON


.. function:: get_server_status(server_id=None)

   Retrieve information about a server's status.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: get_server_dvd(server_id=None)

   Retrieve information about the DVD loaded into the virtual DVD unit of a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: list_server_private_networks(server_id=None)

   Returns a list of a server's private networks.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: private_network_info(server_id=None, private_network_id=None)

   Retrieve information about a server's private network.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :rtype: JSON


.. function:: list_server_snapshots(server_id=None)

   Returns a list of all server snapshots.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: create_server(server=None, hdds=None)

   Create a server.

   :param server: An instantiation of the :class:`Server` class.
   :type server: ``obj``

   :param hdds: a list of :class:`Hdd` instances.
   :type hdds: ``list``

   :rtype: JSON


.. function:: add_hdd(server_id=None, hdds=None)

   Add a new HDD to a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param hdds: a list of :class:`Hdd` instances.
   :type hdds: ``list``

   :rtype: JSON


.. function:: add_new_ip(server_id=None, ip_type=None)

   Add a new IP to the server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_type: at the moment, only ```IPV4``` is currently supported.
   :type ip_type: ``str``

   :rtype: JSON


.. function:: add_load_balancer(server_id=None, ip_id=None, load_balancer_id=None)

   Add a new load balancer to the server IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the server's IP.
   :type ip_id: ``str``

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :rtype: JSON


.. function:: assign_private_network(server_id=None, private_network_id=None)

   Assign a private network to a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :rtype: JSON


.. function:: create_snapshot(server_id=None)

   Create a server snapshot.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: clone_server(server_id=None, name=None)

   Clone a server.

   :param server_id: the unique identifier for the server to be cloned.
   :type server_id: ``str``

   :param name: the new server's name.
   :type name: ``str``

   :rtype: JSON



.. function:: modify_server(server_id=None, name=None, description=None)

   Modify a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param name: server name.
   :type name: ``str``

   :param description: server description.
   :type description: ``str``

   :rtype: JSON


.. function:: modify_server_hardware(server_id=None, fixed_instance_size_id=None, vcore=None, cores_per_processor=None, ram=None)

   Modify a server's hardware configurations.

   .. note:: Cannot perform "hot" decreasing of server hardware values. "Cold" decreasing is allowed.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param fixed_instance_size_id: ID of the instance size for the server. It 
         is not possible to resize to a fixed instance with a HDD smaller than the current one.
   :type fixed_instance_size_id: ``str``

   :param vcore: Total amount of virtual cores.
   :type vcore: ``int``

   :param cores_per_processor: Number of cores per processor.
   :type cores_per_processor: ``int``

   :param ram: Memory size.
   :type ram: ``int``

   :rtype: JSON


.. function:: modify_hdd(server_id=None, hdd_id=None, size=None)

   Modify a server's HDD.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param hdd_id: the unique identifier for the server's HDD.
   :type hdd_id: ``str``

   :param size: the new size of the HDD.  Must be a multiple of ``20``.
   :type size: ``int``

   :rtype: JSON


.. function:: add_firewall_policy(server_id=None, ip_id=None, firewall_id=None)

   Add a firewall policy to the server's IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the server's IP.
   :type ip_id: ``str``

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :rtype: JSON


.. function:: modify_server_status(server_id=None, action=None, method=None)

   Modify a server's status.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param action: the action to perform on the server.  Possible values are ``'POWER_OFF'``, ``'POWER_ON'``,  and ``'REBOOT'``.
   :type action: ``str``

   :param method: the action's method.  Possible values are ``'SOFTWARE'`` or ``'HARDWARE'``.
   :type method: ``str``

   :rtype: JSON


.. function:: load_dvd(server_id=None, dvd_id=None)

   Load a DVD into the virtual DVD unit of a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param dvd_id: the unique identifier for the DVD.
   :type dvd_id: ``str``

   :rtype: JSON


.. function:: restore_snapshot(server_id=None, snapshot_id=None)

   Restore a snapshot into the server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param snapshot_id: the unique identifier for the server snapshot.
   :type snapshot_id: ``str``

   :rtype: JSON


.. function:: reinstall_image(server_id=None, image_id=None, password=None, firewall_id=None)

   Reinstall an image into a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param image_id: the unique identifier for the server image.
   :type image_id: ``str``

   :param password: server password.
   :type password: ``str``

   :param firewall_id: the unique identifier for the firewall policy to be assigned.
   :type firewall_id: ``str``

   :rtype: JSON


.. function:: delete_server(server_id=None, keep_ips=None)

   Delete a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param keep_ips: Set ``keep_ips`` to ``True`` to keep server IPs after deleting a server. (``False`` by default).
   :type keep_ips: ``bool``

   :rtype: JSON


.. function:: remove_hdd(server_id=None, hdd_id=None)

   Remove a server's HDD.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param hdd_id: the unique identifier for the server's HDD.
   :type hdd_id: ``str``

   :rtype: JSON


.. function:: remove_ip(server_id=None, ip_id=None, keep_ip=None)

   Release an server's IP and optionally remove it.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the server's IP.
   :type ip_id: ``str``

   :param keep_ip: Set ``keep_ip`` to ``True`` for releasing the IP without deleting it permanently. (``False`` by default)
   :type keep_ip: ``bool``

   :rtype: JSON


.. function:: remove_firewall_policy(server_id=None, ip_id=None)

   Remove a firewall policy from the server's IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the server's IP.
   :type ip_id: ``str``

   :rtype: JSON


.. function:: remove_load_balancer(server_id=None, ip_id=None, load_balancer_id=None)

   Remove a load balancer from the server's IP.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param ip_id: the unique identifier for the server's IP.
   :type ip_id: ``str``

   :param load_balancer_id: the unique identifier for the load balancer.
   :type load_balancer_id: ``str``

   :rtype: JSON


.. function:: remove_private_network(server_id=None, private_network_id=None)

   Remove a private network from a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :rtype: JSON


.. function:: eject_dvd(server_id=None)

   Unload a DVD from the virtual DVD unit of a server.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: delete_snapshot(server_id=None, snapshot_id=None)

   Remove a snapshot.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param snapshot_id: the unique identifier for the server snapshot.
   :type snapshot_id: ``str``

   :rtype: JSON


The "Server" Class
==========================

.. class:: Server(name=None, description=None, fixed_instance_size_id=None, vcore=None, cores_per_processor=None, ram=None, appliance_id=None, password=None, power_on=None, firewall_policy_id=None, ip_id=None, load_balancer_id=None, monitoring_policy_id=None)
   
   |
   Pass a :class:`Server` instance into the :func:`create_server` 
   method to create a server.  There are also a few helper methods available to perform simple requests after creating your server.

   .. note:: Only the following parameters are **required** to create a server:
         
      * ``name``
      * ``description``
      * ``vcore``
      * ``cores_per_processor``
      * ``ram``
      * ``appliance_id``

   :param name: server name.
   :type name: ``str``

   :param description: server description.
   :type description: ``str``

   :param fixed_instance_size_id: the unique identifier for your desired fixed server flavor.
   :type fixed_instance_size_id: ``str``

   :param vcore: Total amount of virtual cores.
   :type vcore: ``int``

   :param cores_per_processor: Number of cores per processor.
   :type cores_per_processor: ``int``

   :param ram: Memory size.
   :type ram: ``int``

   :param appliance_id: image to be installed on the server.
   :type appliance_id: ``str``

   :param password: server password.
   :type password: ``str``

   :param power_on: choose whether or not you want the server to 'POWER_ON' after creation.  (True by default)
   :type power_on: ``bool``

   :param firewall_policy_id: the unique identifier for the firewall policy to be assigned.
   :type firewall_policy_id: ``str``

   :param ip_id: the unique identifier for the IP to be assigned.
   :type ip_id: ``str``

   :param load_balancer_id: the unique identifier for the load balancer to be assigned.
   :type load_balancer_id: ``str``

   :param monitoring_policy_id: the unique identifier for the monitoring policy to be assigned.
   :type monitoring_policy_id: ``str``

   **Methods:**

   .. method:: get()
      
      Retrieves the server's current specs.

   .. method:: hardware()
      
      Retrieves the server's current hardware configurations.

   .. method:: hdds()
      
      Retrieves a list of the server's HDDs.

   .. method:: image()
      
      Retrieves information about the image currently installed on the server.

   .. method:: ips()
      
      Retrieves a list of the server's IPs.

   .. method:: status()
      
      Retrieves the server's current status.

   .. method:: dvd()
      
      Retrieves information about the DVD currently loaded into the server.

   .. method:: private_networks()
      
      Retrieves a list of the server's private networks.

   .. method:: snapshots()
      
      Retrieves a list of the server's snapshots.

   .. method:: wait_for()
      
      Polls the :class:`Server` resource until an ``ACTIVE``, ``POWERED_ON``, or ``POWERED_OFF`` state is returned.


The "Hdd" Class
================================

.. class:: Hdd(size=None, is_main=None)
   
   
   Use the :class:`Hdd` class to create HDDs which can then be added to a server.

   :param size: HDD size.  Must be a multiple of ``20``.
   :type size: ``int``

   :param is_main: set to ``True`` if the HDD is to be the primary HDD.
   :type is_main: ``bool``
   