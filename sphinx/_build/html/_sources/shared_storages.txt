Shared Storages
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_shared_storages(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all shared storages.

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


.. function:: get_shared_storage(shared_storage_id=None)

   Retrieve information about a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :rtype: JSON


.. function:: list_servers_attached_storage(shared_storage_id=None)

   Returns a list of the servers attached to a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :rtype: JSON


.. function:: get_shared_storage_server(shared_storage_id=None, server_id=None)

   Retrieve information about a server attached to a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


.. function:: get_credentials()

   Returns the credentials for accessing the shared storages.

   :rtype: JSON


.. function:: create_shared_storage(shared_storage=None)

   Create a shared storage.

   :param shared_storage: an instantiation of the :class:`SharedStorage` class.
   :type shared_storage: ``obj``

   :rtype: JSON


.. function:: attach_server_shared_storage(shared_storage_id=None, server_ids=None)

   Attach servers to a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :param server_ids: a list of :class:`AttachServer` instances.
   :type server_ids: ``list``

   :rtype: JSON


.. function:: modify_shared_storage(shared_storage_id=None, name=None, description=None, size=None)

   Modify a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :param name: shared storage name.
   :type name: ``str``

   :param description: shared storage description.
   :type description: ``str``

   :param size: shared storage size.  Must be a multiple of ``50``.
   :type size: ``int``

   :rtype: JSON


.. function:: change_password(password=None)

   Changes the password for accessing shared storages.

   :param password: new shared storage password.
   :type password: ``str``

   :rtype: JSON


.. function:: delete_shared_storage(shared_storage_id=None)

   Delete a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :rtype: JSON


.. function:: detach_server_shared_storage(shared_storage_id=None, server_id=None)

   Detach a server from a shared storage.

   :param shared_storage_id: the unique identifier for the shared storage.
   :type shared_storage_id: ``str``

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :rtype: JSON


The "SharedStorage" Class
==========================

.. class:: SharedStorage(name=None, description=None, size=None)
   
   
   Pass a :class:`SharedStorage` instance into the :func:`create_shared_storage` 
   method to create a shared storage.  There are also a few helper methods available to perform simple requests after creating your shared storage.

   :param name: shared storage name.
   :type name: ``str``

   :param description: shared storage description.
   :type description: ``str``

   :param size: shared storage size.  Must be a multiple of ``50``.
   :type size: ``int``

   **Methods:**

   .. method:: get()
      
      Retrieves the shared storage's current specs.

   .. method:: servers()
      
      Returns a list of the servers attached to the shared storage.

   .. method:: wait_for()
      
      Polls the :class:`SharedStorage` resource until an ``'ACTIVE'``, ``'POWERED_ON'``, or ``'POWERED_OFF'`` state is returned.


The "AttachServer" Class
==========================

.. class:: AttachServer(server_id=None, rights=None, server_ip_id=None)
   
   
   Use the :class:`AttachServer` class to attach servers or server IPs to various containers.

   :param server_id: the unique identifier for the server.
   :type server_id: ``str``

   :param rights: server rights for accessing a shared storage.  Possible values are ``'R'`` or ``'RW'``.  This parameter is only needed when attaching servers to a shared storage.
   :type rights: ``str``

   :param server_ip_id: the unique identifier for the server's IP.
   :type server_ip_id: ``str``