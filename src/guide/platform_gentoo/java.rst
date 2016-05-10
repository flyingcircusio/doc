.. _java:

====
Java
====

This component provides the Java JDK (based on
`OpenJDK <http://openjdk.java.net/>`_).


Packages
--------

* dev-java/log4j
* net-print/cups
* dev-java/icedtea-bin


Configuration
-------------

Multiple Java versions may be installed at any point in time. However,
you may need to select which version should be active as :command:`java` in your
PATH. 

You can find out which ones are available by running
:command:`eselect java-vm list`::

    bob@vm00 ~ $ eselect java-vm list
    Available Java Virtual Machines:
      [1]   icedtea-bin-6  system-vm
      [2]   icedtea-bin-7 

To choose a specific version for your service user you can do so by running
:command:`eselect java-vm set user <slot>`. The slot number is the one that is
shown to you in the output of the list command above.

This setting then becomes permanent for all future sessions of this user.
