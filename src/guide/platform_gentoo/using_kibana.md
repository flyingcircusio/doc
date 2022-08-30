(using-kibana)=

# Analyzing logs with Kibana

Kibana is accessible on [My Flying Circus](https://my.flyingcircus.io) via the
*Tools* drop-down box of the machine having the loghost role assigned:

```{image} ../../images/loghost_access_kibana.png
:width: 220px
```

:::{note}
You need the {ref}`stats permission <permissions>` to access Kibana.
:::

## Creating an index pattern

When accessing your {ref}`loghost's <gentoo-loghost>` Kibana for the first time, you
will be asked to create an *index pattern*.  Choose *@timestamp* as your
*Time-field name*:

```{image} ../../images/loghost_kibana_index_pattern.png
:width: 360px
```

Now, you can start using Kibana. We recommend the [tutorial from Tim Roes](https://www.timroes.de/2015/02/07/kibana-4-tutorial-part-1-introduction/) if
you are new to Kibana.

Kibana will show all the data that is stored in Elasticsearch. Initially, these
are the inputs that are included by us:

- [syslog input plugin](http://logstash.net/docs/1.4.2/inputs/syslog)
- custom filter pattern for HAPRoxy ({file}`/var/log/haproxy.log`)
- custom filter pattern for nginx access logs ({file}`/var/log/nginx/*access.log`)
- custom filter pattern for nginx performance logs ({file}`/var/log/nginx/performance.log`)

For additional data sources, just add your own {ref}`configuration snippets
<configuring_logging_components>` to {ref}`configure_logstash` or
{ref}`configure_logstash-forwarder`, respectively.

## Refreshing your index pattern (reload field list)

Every time your index properties in Elasticsearch change (e.g. when adding new
logstash inputs), make sure to update your respective index patterns pattern in
Kibana to reflect these changes.

:::{warning}
if you miss this step, you might not see your changes in Kibana (e.g. newly
introduced fields).
:::

To update your index pattern, go to *Settings* -> *Indices* and select your
*index pattern* (logstash-\* in our case). Then, just hit the *Reload field list* button:

```{image} ../../images/loghost_kibana_refresh_index_pattern.png
:width: 400px
```
