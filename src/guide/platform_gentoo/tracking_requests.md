(tracking-requests)=

# End-to-end tracking of HTTP requests

In order to track individual requests through the whole chain of involved
components (nginx, Varnish, HAProxy), we have introduced a custom HTTP header
({code}`X-Request-ID`) that is added to each request in our nginx installations:

```{image} ../../images/loghost_kibana_request_id.png
:width: 300px
```

:::{note}
The value is computed from nginx' PID, the connection number, and the request
number in this connection. It is reasonably unique but might be re-used
later.
:::

Tracking an individual request is done by entering its :code:request_id in
{ref}`Kibana <using_kibana>`'s search field:

```{image} ../../images/loghost_kibana_request_id_search.png
:width: 470px
```

This shows two matching entries, one from nginx, the other one from HAProxy.

You might want to integrate your application here. To do so, see {ref}`here
<integrating_app_with_elk>`. You can then extract the header from the request
reaching your application to generate a logstash event that contains the
{code}`request_id` field and others with the information you need.
