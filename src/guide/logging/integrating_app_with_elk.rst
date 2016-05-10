.. _integrating_app_with_elk:

Integrating your application
----------------------------

A lot of logging frameworks already provide handlers for logging to logstash.
Just look around, maybe there already is one out there for your
framework/language. Here are some examples of handlers for different languages:

* Python: `python-logstash <https://pypi.python.org/pypi/python-logstash>`_
* PHP: `monolog <https://github.com/Seldaek/monolog/>`_ already comes with `a
  formatter
  <https://github.com/Seldaek/monolog/blob/master/src/Monolog/Formatter/LogstashFormatter.php>`_
  for Logstash. For example usage, `see here
  <http://engineering.blopboard.com/centralized-logging-with-monolog-logstash-and-elasticsearch>`_
* Java: using log4j with via `SocketAppender
  <https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/net/SocketAppender.html>`_.
* Ruby: `logstash-logger <http://www.rubydoc.info/gems/logstash-logger/>`_

When configuring your handler, use the canonical FQDN of your :ref:`loghost
<loghost>` as the logstash host, e.g. *myapp00.gocept.net*.

.. note::

   You will most likely have to configure some kind of listener on the logstash
   side. See the :ref:`configure_logstash` section for how to add your
   configuration to logstash.
