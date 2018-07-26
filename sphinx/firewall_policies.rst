Firewall Policies
*****************


OneAndOneService Methods
=========================

.. note:: All of the methods below can be called on a :class:`OneAndOneService` instance.

.. function:: list_firewall_policies(page=None, per_page=None, sort=None, q=None, fields=None)

   
   Returns a list of your firewall policies.

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


.. function:: get_firewall(firewall_id=None)

   Retrieve information about a firewall policy.

   :param firewall_id: the unique identifier for the firewall.
   :type firewall_id: ``str``

   :rtype: JSON


.. function:: list_firewall_servers(firewall_id=None)

   Returns a list of the servers attached to a firewill policy.

   :param firewall_id: the unique identifier for the firewall.
   :type firewall_id: ``str``

   :rtype: JSON


.. function:: get_firewall_server(firewall_id=None, server_ip_id=None)

   Retrieve a information about a server attached to a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :param server_ip_id: the unique identifier for a server's IP.  This is different from ``server_id``.
   :type server_ip_id: ``str``

   :rtype: JSON


.. function:: list_firewall_policy_rules(firewall_id=None)

   Returns a list of the rules of a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :rtype: JSON


.. function:: get_firewall_policy_rule(firewall_id=None, rule_id=None)

   Retrieve information about a firewall policy rule.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :param rule_id: the unique identifier for the firewall rule.
   :type rule_id: ``str``

   :rtype: JSON


.. function:: modify_firewall(firewall_id=None, name=None, description=None)

   Modify a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :param name: firewall policy name.
   :type name: ``str``

   :param description: firewall policy description.
   :type description: ``str``

   :rtype: JSON


.. function:: create_firewall_policy(firewall_policy=None, firewall_policy_rules=None)

   Create a firewall policy.

   :param firewall_policy: an instantiation of the :class:`FirewallPolicy` class.
   :type firewall_policy: ``obj``

   :param firewall_policy_rules: a list of :class:`FirewallPolicyRule` instances.
   :type firewall_policy_rules: ``list``

   :rtype: JSON


.. function:: add_firewall_policy_rule(firewall_id=None, firewall_policy_rules=None)

   Add rules to a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :param firewall_policy_rules: a list of :class:`FirewallPolicyRule` instances.
   :type firewall_policy_rules: ``list``

   :rtype: JSON


.. function:: attach_server_firewall_policy(firewall_id=None, server_ips=None)

   Attach servers to a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :param server_ips: a list of :class:`AttachServer` instances.
   :type server_ips: ``list``

   :rtype: JSON


.. function:: delete_firewall(firewall_id=None)

   Delete a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :rtype: JSON


.. function:: remove_firewall_rule(firewall_id=None, rule_id=None)

   Remove a rule from a firewall policy.

   :param firewall_id: the unique identifier for the firewall policy.
   :type firewall_id: ``str``

   :param rule_id: the unique identifier for the firewall policy rule.
   :type rule_id: ``str``

   :rtype: JSON

The "FirewallPolicy" Class
==========================

.. class:: FirewallPolicy(name=None, description=None)
   
   
   Pass a :class:`FirewallPolicy` instance into the :func:`create_firewall_policy` 
   method to create a firewall policy.  There are also a few helper methods available to perform simple requests after creating your firewall policy.

   :param name: firewall policy name.
   :type name: ``str``

   :param description: firewall policy description.
   :type description: ``str``


   **Methods:**

   .. method:: get()
      
      Retrieves the firewall policy's current specs.

   .. method:: ips()
      
      Returns a list of the server IPs attached to the firewall.

   .. method:: rules()
      
      Returns a list of the rules attached to the firewall.

   .. method:: wait_for()
      
      Polls the :class:`FirewallPolicy` resource until an ``ACTIVE``, ``POWERED_ON``, or ``POWERED_OFF`` state is returned.


The "FirewallPolicyRule" Class
================================

.. class:: FirewallPolicyRule(protocol=None, port_from=None, port_to=None, source=None)
   
   
   Use the :class:`FirewallPolicyRule` class to create or modify firewall policy rules.

   :param protocol: internet protocol.  Possible values are ``"TCP"``, ``"UDP"``, ``"ICMP"``, ``"AH"``, ``"ESP"``, ``"GRE"``.
   :type protocol: ``str``

   :param port_from: first port in range.
   :type port_from: ``int``

   :param port_to: second port in range.
   :type port_to: ``int``

   :param source: IPs from which access is available. Setting ``0.0.0.0`` all IPs are allowed.
   :type source: ``str``

   :param description: Rule description.
   :type description: ``str``

   :param action: Action to be done in the rule. Deny is only allowed with protocol ANY to deny all ports.
   :type action: ``str``

   :param port: Port or range of ports to be included in the rule. Can be used instead of port_from, port_to.
   :type port: ``str``


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
