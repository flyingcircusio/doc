.. _nixos-datadoc:

Datadog integration
===================

Managed instance of the `Datadog Agent <https://www.datadoghq.com>`_.

Components
----------

* Datadog agent (dd-agent)

Configuration
-------------

Service users may drop a JSON config file containing the basic configuration
into :file:`/etc/local/datadog/datadog.json`::

    {
      "api_key": "your-api-key",
      "hostname": "your-optional-alias",
      "tags": ["your", "tags", "(optional)"]
    }

Additionally you may add .yaml (like mysql.yaml) files for further customization.
Please consult the datadog integrations help for details.


Interaction
-----------

Service users may invoke :command:`sudo fc-manage --build` to apply
service configuration changes and trigger service restarts (if necessary).

Monitoring
----------

The default monitoring setup checks that the relevant processes are running.

.. vim: set spell spelllang=en:
