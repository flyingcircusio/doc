(nixos-redis)=

# Redis

Runs a [Redis](http://redis.io) database server. The server listens on the
*srv* interface on port 6379.

## Components

- Redis

## Configuration

The Redis configuration is fully managed. Currently there are no adaptable
options.

The authentication password is automatically generated upon installation
and can be read *and changed* by service users. It can be found in
{file}`/etc/local/redis/password`.

## Interaction

Service users may invoke {command}`sudo fc-manage --build` to apply
service configuration changes and trigger service restarts (if necessary).

## Monitoring

The default monitoring setup checks that the Redis server is running, and is responding to [PING](https://redis.io/commands/ping).

% vim: set spell spelllang=en:
