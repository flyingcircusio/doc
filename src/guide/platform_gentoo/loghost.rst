.. _gentoo-loghost:

Loghost
=======

Provides centralized logging infrastructure inside a project
including remote `rsyslog <http://www.rsyslog.com/>`_ and ELK (`Elasticsearch
<https://www.elastic.co/products/elasticsearch>`_, `Logstash
<https://www.elastic.co/products/logstash>`_, `Kibana
<https://www.elastic.co/products/kibana>`_).

Please refer to chapter :ref:`Logging <logging>` for configuration examples
and hints on using the ELK stack.

Components
----------

* rsyslog (:ref:`srv interface <logical_networks>`, port UDP 514)
* Elasticsearch (:ref:`srv interface <logical_networks>`, ports TCP 9200 and
  9300)
* elasticsearch-curator
* Logstash

  * `syslog input <http://logstash.net/docs/1.4.2/inputs/syslog>`_
    (*localhost*, ports UDP 5000 and TCP 5000)
  * `Lumberjack input <http://logstash.net/docs/1.4.2/inputs/lumberjack>`_
    (:ref:`srv interface <logical_networks>`, port TCP 5043)

* logstash-forwarder
* Kibana

Default setup
-------------

* Elasticsearch, Logstash and Kibana are installed on the loghost.
* logstash creates elasticsearch indices of the pattern *logstash-YYYY.MM.DD*.
* elasticsearch-curator deletes indices older than 90 days.
* logstash-forwarder ships locally generated logs from all machines to
  the loghost.
* rsyslog forwards all syslog entries to the loghost.

.. _loghost_configuration:

Configuration
-------------

Below is a list of your configuration entry points for the involved components.

.. warning::

   All configuration needs to be performed as a :ref:`service user
   <service_users>`.

* *rsyslog*: :file:`/etc/rsyslog.d/{SNIPPET}.conf`
* *logstash-forwarder*: :file:`/etc/logstash-forwarder/conf.d/{SNIPPET}.conf`
* *logstash*: :file:`/etc/logstash/conf.d/{SNIPPET}.conf`

Interaction
-----------

* *rsyslog*: :command:`sudo /etc/init.d/rsyslog restart` for restarts after
  configuration changes

  .. note::

    rsyslog ignores invalid configuration statements, so be sure to check
    :file:`/var/log/messages` for errors after a restart.

* *logstash-forwarder*: :command:`sudo /etc/init.d/logstash-forwarder restart`
  for restarts after configuration changes
* *Logstash*: :command:`sudo /etc/init.d/logstash restart` for restarts after
  configuration changes
* *Kibana*: refer to our :ref:`Logging <logging>` section for how to interact
  with Kibana


Monitoring
----------

We monitor for:

* running processes
* reachable ports
* correctly written log files
* correctly pruned Elasticsearch indices

.. vim: set spell spelllang=en:
