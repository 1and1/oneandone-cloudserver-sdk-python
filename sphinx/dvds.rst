DVDs
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_dvds(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all the operative systems and tools that you can load into your virtual DVD unit.

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

.. function:: get_dvd(iso_id=None)

   Retrieve information about a specific DVD.

   :param iso_id: the unique identifier for the DVD.
   :type iso_id: ``str``

   :rtype: JSON