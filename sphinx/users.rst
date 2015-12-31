Users
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_users(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all users.

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


.. function:: get_user(user_id=None)

   Retrieve information about a specific user.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :rtype: JSON


.. function:: api_info(user_id=None)

   Retrieve information about a user's API privileges.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :rtype: JSON


.. function:: show_api_key(user_id=None)

   Retrieve a user's API key.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :rtype: JSON

.. function:: ips_api_access_allowed(user_id=None)

   List IP's from which API access is allowed for a user.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :rtype: JSON


.. function:: create_user(name=None, password=None, email=None, description=None)

   Create a user.

   :param name: user name.
   :type name: ``str``

   :param password: user password.
   :type password: ``str``

   :param email: user email.
   :type email: ``str``

   :param description: user description.
   :type description: ``str``

   :rtype: JSON


.. function:: add_user_ip(user_id=None, user_ips=None)

   Add user IPs.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :param user_ips: a list containing at least one IP string.
   :type user_ips: ``list``

   :rtype: JSON


.. function:: modify_user(user_id=None, description=None, email=None, password=None, state=None)

   Modify a user.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :param password: user password.
   :type password: ``str``

   :param email: user email.
   :type email: ``str``

   :param description: user description.
   :type description: ``str``

   :param state: allows you to enable and disable users.  Possible values are ``"ACTIVE"`` or ``"DISABLE"``.
   :type state: ``str``

   :rtype: JSON


.. function:: modify_user_api(user_id=None, active=None)

   Modify a user's API privileges.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :param active: API access.
   :type active: ``bool``

   :rtype: JSON


.. function:: change_api_key(user_id=None)

   Change a user's API key:

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :rtype: JSON


.. function:: delete_user(user_id=None)

   Delete a user.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :rtype: JSON


.. function:: remove_user_ip(user_id=None, ip=None)

   Remove a user IP.

   :param user_id: the unique identifier for the user.
   :type user_id: ``str``

   :param ip: IP to be removed.
   :type ip: ``str``

   :rtype: JSON
   