Private Networks
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_private_networks(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all private networks.

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


.. function:: get_private_network(private_network_id=None)

   Retrieve information about a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :rtype: JSON


.. function:: list_private_network_servers(private_network_id=None)

   Returns a list of the servers attached to a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :rtype: JSON


.. function:: get_private_network_server(private_network_id=None, server_id=None)

   Retrieve a information about a server attached to a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: create_private_network(private_network=None)

   Create a private network.

   :param private_network: an instantiation of the :class:`PrivateNetwork` class.
   :type private_network: ``obj``

   :rtype: JSON


.. function:: attach_private_network_servers(private_network_id=None, server_ids=None)

   Attach servers to a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :param server_ids: a list of :class:`AttachServer` instances.
   :type server_ids: ``list``

   :rtype: JSON


.. function:: modify_private_network(private_network_id=None, name=None, description=None, network_address=None, subnet_mask=None)

   Modify a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :param name: private network name.
   :type name: ``str``

   :param description: private network description.
   :type description: ``str``

   :param network_address: private network address. (valid IP)
   :type network_address: ``str``

   :param subnet_mask: Subnet mask (valid subnet for the given IP).
   :type subnet_mask: ``str``

   :rtype: JSON


.. function:: delete_private_network(private_network_id=None)

   Delete a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :rtype: JSON


.. function:: remove_private_network_server(private_network_id=None, server_id=None)

   Detach a server from a private network.

   :param private_network_id: the unique identifier for the private network.
   :type private_network_id: ``str``

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


The "PrivateNetwork" Class
==========================

.. class:: PrivateNetwork(name=None, description=None, network_address=None, subnet_mask=None)
   
   
   Pass a :class:`PrivateNetwork` instance into the :func:`create_private_network` 
   method to create a private network.  There are also a few helper methods available to perform simple requests after creating your private network.

   :param name: private network name.
   :type name: ``str``

   :param description: private network description.
   :type description: ``str``

   :param network_address: Private network address. (valid IP)
   :type network_address: ``str``

   :param subnet_mask: Subnet mask (valid subnet for the given IP).
   :type subnet_mask: ``str``

   **Methods:**

   .. method:: get()
      
      Retrieves the private network's current specs.

   .. method:: servers()
      
      Returns a list of the servers attached to the private network.

   .. method:: wait_for()
      
      Polls the :class:`PrivateNetwork` resource until an ``ACTIVE``, ``POWERED_ON``, or ``POWERED_OFF`` state is returned.


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