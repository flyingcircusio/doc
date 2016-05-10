:Publish Date: 2011-12-13

.. _webcache:

Varnish
=======

Description
-----------

High-performance HTTP caching.

Components
----------

- Varnish

Configuration
-------------

- The file :file:`/etc/varnish/default.vcl` is provided with a template. It can be
  edited/replaced by service users. Please note that the default Varnish
  incoming port is 8008. You need to reflect this in your webserver config to
  use Varnish.

Interaction
-----------

- Service users may restart Varnish after configuration changes with
  :command:`sudo /etc/init.d/varnishd restart`.

Monitoring
----------

- We monitor that the varnishd process is running and the varnishd port is open.

Debugging
---------

Varnish may refuse to start when provided with an invalid VCL configuration
without giving much information. In this case it may be helpful to [#sf398680]_:

* start Varnish with a known good configuration
* attach to varnishadm via :command:`varnishadm -T 127.0.0.1:6082`
* load the new config with :command:`vcl.load error <path_to_your_vcl>`


.. [#sf398680] As seen on `StackOverflow <https://serverfault.com/questions/398680/custom-vcl-prevents-varnish-from-starting#398760>`_.

