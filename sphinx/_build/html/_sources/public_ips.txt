Public IPs
**********

OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_public_ips(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all public IPs.

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

.. function:: get_public_ip(ip_id=None)

	Retrieve a single public IP by ID.

	:param ip_id: the unique identifier for the IP.
	:type ip_id: ``str``

	:rtype: JSON

.. function:: create_public_ip(reverse_dns=None, ip_type=None)

   Create a public IP.

   :param reverse_dns: reverse dns name.
   :type reverse_dns: ``str``

   :param ip_type: can only be set to ``'IPV4'`` at this time.
   :type ip_type: ``str``

   :rtype: JSON

.. function:: modify_public_ip(ip_id=None, reverse_dns=None)

   Modify a public IP.

   :param ip_id: the unique identifier for the IP.
   :type ip_id: ``str``

   :param reverse_dns: reverse dns name.
   :type reverse_dns: ``str``

   :rtype: JSON

.. function:: delete_public_ip(ip_id=None)

   Delete a public IP.

   :param ip_id: the unique identifier for the IP.
   :type ip_id: ``str``

   :rtype: JSON