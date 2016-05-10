.. _loadbalancer:

haproxy
=======

Description
-----------

High-performance and high-availability HTTP and TCP load balancer.

Components
----------

- haproxy

Configuration
-------------

- The file :file:`/etc/haproxy/haproxy.cfg` is provided with a template that
  does not do much. It may be edited/replaced by service users. Please don't
  change the listening port (8002), the user or the logging configuration.

Interaction
-----------

- Service users may restart haproxy  after configuration changes with
  :command:`sudo /etc/init.d/haproxy reload`.

Monitoring
----------

- We monitor that the haproxy process is running and the haproxy port is open.
