% last review: 2024-05-07

% review schedule: 1 year

% ISMSControl: A.9.2.2
% ISMSControl: 5.18


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

- Users are distinguished as human or service users.
- All users of a resource group are configured (e.g. visible via `getent`) on all
  nodes of a resource group.
- The following attributes are globally unique: UID for users; group
  name and GID for groups. 
- The presence of an account alone does not imply any permission assignments.

## Human users

- The username is globally unique and must not start with `s-`.
- The primary group is `users`.
- The home directory is located in {file}`/home/$USER`.

(service-users)=

## Service users

- The primary group is `service`.
- Usernames usually start with `s-` and are unique within a resource group.
  Different resource groups can reuse the same service user names.
- The home directory is located in {file}`/srv/$USER`.
- No SSH login is allowed by default to support the general data protection guidelines. In exceptional cases SSH access may be granted.
- Human users that have the *sudo-srv* permission in a project are
  allowed to change to the service user ({command}`sudo -u <service_user_name>
  -i`) and execute commands as a service user ({command}`sudo -u
  <service_user_name> <command>`).

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
