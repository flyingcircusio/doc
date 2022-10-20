% last review: XXX

% review schedule: 1 year

% ISMSControl: A.9.2.2


```{image} ../../images/users250.png
:class: logo
:width: 250px
```

(useraccounts)=

# User accounts

```{toctree}
:hidden: true

ssh-keygen
```

## Principles

- Users are either humans, or non-human users for services.
- All users of a resource group are configured (e.g. visible via getent) on all
  hosts of a resource group.
- The following attributes are globally unique: username, UID, group
  name, GID. XXX
- The bijections between username/UID and group name/GID are globally unique. XXX
- The presence of an account alone does not imply any permission assignments.

## Human users

- The primary group is `users`.
- The home directory is located in {file}`/home/$USER`.

(service-users)=

## Service users

- The primary group is `service`.
- Usernames usually start with `s-`
- The home directory is located in {file}`/srv/$USER`.
- No SSH login is allowed by default to support the general data protection guidelines. In exceptional cases SSH access may be granted.
- human users that have the *sudo-srv* permission in a project are
  allowed to change to the service user ({command}`sudo -u <service_user_name>
  -i`) and execute commands as a service user ({command}`sudo -u
  <service_user_name> <command>`)

(permissions)=

## Permissions

Users own a separate set of permissions for every project they are a
member of. Common permissions include:

login

: Perform interactive shell login on a machine (via SSH).

manager

: Add or remove other users from the project. Define permissions for users in the project.

sudo-srv

: Sudo into service users on a machine (password not necessary)
