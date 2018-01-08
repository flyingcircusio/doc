.. _nixos-php:

PHP
===

For operating PHP based applications we chose to use `FPM <http://php.net/manual/en/intro.fpm.php>`_.

We assume the service user is called ``s-phpsite``, and that the docroot is :file:`/srv/s-phpsite/docroot`. But of course you can use different service user names, and different docroots.


Installation
------------

Note that on the NixOS platform it is not necessary to activate a role to install PHP. You can install PHP into the service user::

    ssh your-vm
    sudo -iu s-phpsite
    nix-env -iA nixos.php70

There are different PHP versions to choose from:

* ``nixos.php55``
* ``nixos.php56``
* ``nixos.php70``

.. NOTE:: You can install different PHP versions at the same time on the same machine in different service users.



Configuration
-------------

Add configuration for FPM (:file:`/srv/s-phpsite/phpfpm.conf`)::


    [global]
    error_log = syslog
    daemonize = yes
    log_level = notice

    [app_pool]
    listen = 127.0.0.1:9002
    pm = dynamic
    pm.max_children = 10
    pm.start_servers = 4
    pm.min_spare_servers = 4
    pm.max_spare_servers = 4
    pm.max_requests = 500

Of course the specific values depend on the expected load and the VM dimensions.

You can add a :file:`php.ini` which suits your needs to :file:`/srv/s-phpsite/php.ini`.

Register the FPM with systemd, to get a running process. Since there are some variables, like PATH to fill out, feel free to copy-paste the following shell-snippet (as service user, ``s-phpsite`` in our case)::

    (
    cat <<EOF
    [Unit]
    Description=FPM phpsite1

    [Service]
    Environment="PATH=$PATH"
    User=$USER
    Group=service

    ExecStart=$HOME/.nix-profile/bin/php-fpm -n -y $HOME/phpfpm.conf -g $HOME/phpfpm.ini
    Type=forking

    EOF
    ) > /etc/local/systemd/phpsite.service

    sudo fc-manage --build


Here is a snippet for configuring the phpfpm support into your nginx virtual host (see also the :revcF:ref:`nixos-nginx` role documentation)::

    root /srv/s-phpsite/docroot;

    location / {
        index index.php;
        if (!-f $request_filename) {
            rewrite  ^(.*)$  /index.php  last;
            break;
        }
    }

    location ~ \.php$ {
        fastcgi_pass 127.0.0.1:9001;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include /etc/local/nginx/fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param HTTPS off;
    }




Local PEAR configuration
------------------------

PEAR is shipped with PHP, and you will need a local configuration to use it::

    pear config-create $HOME $HOME/.pearrc

For PEAR to work, PHP needs to include PEAR in :file:`php.ini` (see above)::

    include_path = "/srv/s-phpsite/pear/php"


.. vim: set spell spelllang=en:

