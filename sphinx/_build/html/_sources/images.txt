Images
******


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_images(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of all images.

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

.. function:: get_image(image_id=None)

	Retrieve a single image by ID.

	:param image_id: the unique identifier for the image.
	:type image_id: ``str``

	:rtype: JSON

.. function:: create_image(image=None)

   Create an image.

   :param image: an instantiation of the :class:`Image` class.
   :type image: ``obj``

   :rtype: JSON

.. function:: modify_image(image_id=None, name=None, description=None, frequency=None)

   Modify an image.

   :param image_id: the unique identifier for the image.
   :type image_id: ``str``

   :param name: image name.
   :type name: ``str``

   :param description: image description.
   :type description: ``str``

   :param frequency: can only be changed to ``'ONCE'``
   :type frequency: ``str``

   :rtype: JSON

.. function:: delete_image(image_id=None)

   Delete an image.

   :param image_id: the unique identifier for the image.
   :type image_id: ``str``

   :rtype: JSON


The "Image" Class
=================

.. class:: Image(server_id=None, name=None, description=None, frequency=None, num_images=None)
   
   
   Pass an :class:`Image` instance into the :func:`create_image` 
   method to create an image.  There are also a few helper methods available to perform simple requests after creating your image.

   :param server_id: the ID of the server to be copied.
   :type server_id: ``str``

   :param name: image name.
   :type name: ``str``

   :param description: image description.
   :type description: ``str``

   :param frequency: the image's creation policy.  Possible values are 
      ``'ONCE'``, ``'DAILY'``, and ``'WEEKLY'``.
   :type frequency: ``str``

   :param num_images: maximum number of images.
   :type num_images: ``int``

   **Methods:**

   .. method:: get()
      
      Retrieves the image's current specs.

   .. method:: wait_for()
      
      Polls the :class:`Image` resource until an ``'ACTIVE'``, ``'POWERED_ON'``, or ``'POWERED_OFF'`` state is returned.
