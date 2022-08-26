(nixos-elasticsearch)=

# Elasticsearch

Managed instance of [Elasticsearch](https://www.elastic.co/products/elasticsearch) 2.4.

## Configuration

Upon activating the role, Elasticsearch forms a cluster named as the VM's name. To change the cluster name, add a file {file}`/etc/local/elasticsearch/clusterName`, with the cluster name as its sole contents. To activate run {command}`sudo fc-manage --build` (see {ref}`nixos-local` for details).

Elasticsearch instances are configured with a reasonable memory configuration, depending on the VMs configured memory.

## Monitoring

The following checks are active initially:

- Circuit Breakers active
- Cluster Health
- File descriptors in use
- Heap too full
- Node status
- Shard allocation status
