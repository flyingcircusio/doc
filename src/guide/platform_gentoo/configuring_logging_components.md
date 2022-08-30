(configuring-logging-components)=

# Configuring the log host components

There are two parts of the logging infrastructure that are important for you to
configure: the logstash-forwarder and the logstash server.

The logstash-forwarder picks up log files from a machine and forwards it to the
logstash server. The logstash server receives log data and can filter,
transform, store and forward this data (e.g. to other locations, triggering
actions, or sending notification mails).

(configure-logstash-forwarder)=

## logstash-forwarder

For your configuration entry points and how to control the daemon, see
{ref}`here <loghost_configuration>`.  If you need help with the configuration
concepts and syntax, please consult the [logstash-forwarder online
documentation][logstash-forwarder online documentation] for reference.

When configuring logstash-forwarder, you typically only need to define the log
files you wish to forward to logstash. In the following example, we forward some
application logs:

```
{
   "files": [
    {
      "paths": [
        "/var/log/myapp/instance.log"
      ],
      "fields": { "type": "myapp_instance" }
    },
    {
      "paths": [
        "/var/log/myapp/*-worker.log"
      ],
      "fields": { "type": "myapp_worker" }
    }
  ]
}
```

Now your logs are forwarded to the central logstash. For further processing, you
need to {ref}`configure logstash accordingly <configure_logstash>`.

(configure-logstash)=

## Logstash

For your configuring entry points and how to control the daemon, see {ref}`here
<loghost_configuration>`.  If you need help with the configuration concepts and
syntax, please see the [logstash online documentation] for reference.

Now that we have {ref}`configured logstash-forwarder
<configure_logstash-forwarder>` to forward our application log files to
logstash, we can configure the processing of our logs.

In the following example, we define a grok expression that extracts certain
values from each log line. The values will then be available for search {ref}`in
Kibana <using_kibana>`:

```
filter {
   if [type] == "myapp_instance" {
      grok {
         match => { "message" => "%{IP:remote_addr} - %{NOTSPACE:remote_user} \[%{HTTPDATE:time_local}\] \"(?:%{WORD:http_verb} %{NOTSPACE:http_request}(?: HTTP/%{NUMBER:http_version})?|%{DATA:raw_request})\" %{NUMBER:status} (?:%{NUMBER:body_bytes_sent}|-) \"%{NOTSPACE:http_referer}\" \"%{DATA:http_user_agent}\" \"%{NOTSPACE:gzip_ratio}\" \"%{NOTSPACE:upstream_http_content_type}\"" }
      }
   }
}
```

:::{note}
There is a nice online tool to create custom grok rules called [Grok
Constructor][grok constructor].
:::

[grok constructor]: http://grokconstructor.appspot.com/
[logstash online documentation]: https://github.com/elastic/logstash#configuring
[logstash-forwarder online documentation]: https://github.com/elastic/logstash-forwarder#configuring
