:Publish Date: 2012-02-02

.. _tomcatserver:

Tomcat
======

Runs a `Tomcat <http://tomcat.apache.org>`_ server as a container for custom
Java applications. The server listens on *localhost:8091* for HTTP
requests to access the deployed applications.

Components
----------

* Sun JDK
* Tomcat server
* JDBC postgresql

Configuration
-------------

The main configuration is managed automatically with the following flexible
parts editable by service users:

* :file:`/etc/tomcat-6/tomcat-users.xml` to define users, passwords and roles
  for accessing the tomcat management interfaces.

* :file:`/etc/tomcat-6/Catalina/localhost` to place context definitions for deploying applications.

The server is configured to not automatically reload applications when their
on-disk deployment files change.

Applications may be dynamically deployed using the `manager application
<http://tomcat.apache.org/tomcat-6.0-doc/manager-howto.html>`_.

Interaction
-----------

After configuration changes, invoke :command:`sudo /etc/init.d/tomcat-6
restart` as service user to acticate the new configuration.

If dynamic class-loading is used heavily the JVM's permanent generation space
may fill up causing Tomcat to become completely unresponsive. In this case a
restart using the init script is required.

Monitoring
----------

We monitor by default:

* whether the local HTTP port is reachable and responsive
* whether a reasonable number of Tomcat processes are running
