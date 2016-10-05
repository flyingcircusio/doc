.. _process-management:

Process management
===================

Supervisord
-----------

We recommend the use of `supervisord`_ to monitor your application and restart
the process in case of problems.

To install supervisord into your virtualenv add a supervisor section to your
:file:`buildout.cfg`::

   [buildout]
   parts = django supervisor

   [...]

   [supervisor]
   recipe = collective.recipe.supervisor
   programs = 10 django ${buildout:bin-directory}/django [runserver 8000]

Run buildout again to install supervisord::

   $ ./bin/buildout

Start the supervisord.::

   $ ./bin/supervisord

You can now manage your Django instance with supervisord::

  $ ./bin/supervisorctl

.. _userinit:

Init scripts
------------

Service users may have their own init scripts to start and stop services on
machine startup/shutdown. The system invokes user-specific init scripts in the
user's context.

Init script location
^^^^^^^^^^^^^^^^^^^^

Init scripts are automatically picked up by the system if they are placed in the
directory :file:`/var/spool/init.d/{USERNAME}`.::

   $ tree /var/spool/init.d
   /var/spool/init.d
   `-- srvuser
       |-- 10supervisor
       `-- 20other_app

.. note::

   All directories beneath :file:`/var/spool/init.d` must have the same name as
   the service user that owns them. Otherwise the scripts in the directory will
   not be run by the system.

On system start, init scripts are run as user `srvuser` in the following
order::

   /var/spool/init.d/srvuser/10supervisor start
   /var/spool/init.d/srvuser/20other_app start

On system shutdown, init scripts are run as user `srvuser` in the following
order::

   /var/spool/init.d/srvuser/20other_app stop
   /var/spool/init.d/srvuser/10supervisor stop


The system runs all executable scripts which have file names that conform to the
:command:`run-parts --lsbsysinit` namespaces. It is recommended to use only
alphanumerical characters. For details, see the :manpage:`run-parts(1)` manual
page.

If init scripts do not terminate (e.g. start services in the foreground), they
will be killed after 5 minutes. So be sure that your init scripts start services
in the background.

supervisord
^^^^^^^^^^^

Unfortunately, the `supervisord` provides no single command that accepts
:command:`start` and :command:`stop` arguments in a way that is compatible to
the user init scheme.

To work around this limitation, write a shell script which starts and stops
`supervisord` accordingly and place/symlink it into the
:file:`/var/spool/init.d/{USERNAME}` directory::

   #!/bin/bash
   # Wrapper script to start/stop supervisord from userinit.
   # Copyright (c) gocept gmbh & co. kg
   # See also LICENSE.txt
   set -e

   PATH="${PATH}:/usr/local/sbin:/usr/sbin:/sbin"
   DAEMON="${HOME}/myproject/bin/supervisord"
   CTL="${HOME}/myproject/bin/supervisorctl"
   PIDFILE="/run/local/supervisord-myproject.pid"

   start() {
       start-stop-daemon --start -p "$PIDFILE" -i -- "$DAEMON"
   }

   stop() {
       "$CTL" shutdown
   }

   restart() {
       "$CTL" restart all
   }

   status() {
       "$CTL" status
   }

   case $1 in
       start|stop|status)
           $1;;
       restart)
           restart || {
               stop || true
               start
           }
           ;;
   esac

Note that the `set -e` line causes the shell to exit the whole script
unsuccessfully if one of the invoked commands exits unsuccessfully.

.. _supervisord: http://supervisord.org/


Testing
-------

To test the setup, you can invoke the user-specific init scripts manually
when logged in as service user::

   $ userinit -v start
   run-parts: executing /var/spool/init.d/srvuser/10supervisor start

   $ userinit -v stop
   run-parts: executing /var/spool/init.d/srvuser/10supervisor stop

If these tests succeed, the services will very likely start at system boot time.


Error handling
--------------

Userinit tries to proceed if one of the configured services fail to start or
stop. All errors and other messages are logged to syslog. We assume that there
are monitoring checks that fire off if required processes are not
running.

To determine what happened during actual startup or shutdown of the machine, you
can consult :file:`/var/log/rc.log`.

.. _supervisord: http://supervisord.org/
