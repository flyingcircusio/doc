.. image:: ../../images/logging250.png
   :class: logo
   :width: 250px

.. _logging:

*******
Logging
*******

Creating, storing, and analysing logs from components and your application is
an important part of keeping your service healthy and developing it further.

This chapter gives you an overview of our logging infrastructure and how to
integrate your application.

On the most basic level, our :ref:`managed components <managed-components>`
provide regular log files. See each component's documentation about where to
find them and how to read them.

For more advanced use cases, you can choose to use the managed :ref:`loghost
<loghost>` component: using `Elasticsearch
<https://www.elastic.co/products/elasticsearch>`_, `Logstash
<https://www.elastic.co/products/logstash>`_, and `Kibana
<https://www.elastic.co/products/kibana>`_ (known as the ELK stack)  gives you
powerful tools to store your logs from multiple machines on a central server.
There you can analyze, filter, notify, search, graph, and create dashboards
from them.

When you enable a :ref:`loghost <loghost>` it automatically picks up logs from
our managed components and gives you a starting point to integrate your
application by either logging directly from your application or integrating
custom log files.

.. toctree::
   :maxdepth: 1

   configuring_logging_components
   using_kibana
   integrating_app_with_elk
   tracking_requests
