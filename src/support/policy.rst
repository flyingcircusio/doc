Policy
======

How do people get help?
-----------------------

The preferred way to report support/feature requests and failure complaints to
the system administration team should be via the Flying Circus' RT ticket
system.

Sending email to support@flyingcircus.io causes
a ticket to be created that will be followed up by our system administrators.

Requests reported via alternative communications should get an associated
ticket if they require a non-trivial amount of work.


How do we respond to support tickets?
-------------------------------------

The following steps are taken by our support team to ensure an adequate
response to support requests. For requests that require a response time
according to an SLA this procedure must be completed for the SLA to have been
fulfilled:

1. The incoming ticket is manually reviewed for two factors: importance and
   urgency.  Importance indicates the size of business impact if the problem
   does not get solved.  Urgency indicates a time limit until the request needs
   to be solved.  The two factors are dealt with in a binary way
   (important/unimportant, urgent/not urgent).

2. Depending on the outcome of the review the following steps will be taken
   within the response time limit:

   Important and urgent (Q1)
        A support person is allocated to the task and begins work on the
        issue.

   Important but not urgent (Q2)
        A support person is allocated to the task and a proposed date
        is announced when work will be started.

   Not important and urgent (Q3) or not important and not urgent (Q4)
        The support ticket will usually be moved to a regular maintenance
        tracker and dealt with "as soon as time allows".

   No classification possible due to missing information
        We will inquire with the reporter of the issue about missing
        information to allow classification for importance and urgency.

   Having inquired for the information will be counted as having reacted
   within the response time.


Emergency contacts
------------------

What is an emergency?
+++++++++++++++++++++

An emergency is any situation that prevents the Flying Circus from fulfilling
it's contractual duties in a substantial amount. This includes large customer
visible outages or the inability to proceed with development. Emergencies
should be reported immediately to a member of the system administration team.


Handling of an emergency
++++++++++++++++++++++++

In case of an emergency, the system administration team concentrates all
resources towards a resolution. Other work is postponed until the problem is
resolved. Information about emergencies and disruptive work is published on our
`status page <http://status.flyingcircus.io/>`_.

SLA contact
+++++++++++

Clients with a specific service level agreement (defines standby times,
response times and penalties) receive a client specific identification number
(PIN).  In case of an emergency, there are the following ways to activate the
standby support:

* Automatic system monitoring (nagios) detects an outage.

* The client sends an email to emergency+<PIN>@flyingcircus.io (If your PIN is
  `1234`, send an email to `emergency+1234@flyingcircus.io`).

* The client calls emergency support number *+49 345 95990625* and enters the
  client-specific PIN.

  The call is forwarded to the active primary supporter who either picks up
  immediately or calls back within the allowed time frame of the SLA.

In any case there will be a support ticket created automatically.

.. WARNING::

    The standby support is *only* notified during the hours booked
    according to the SLA.

.. NOTE::

    When an emergency ticket is created the active supporters are notified via

    * Pushover (https://pushover.net/),

    * Pager (http://www.ecityruf.de/) and

    * Email.


Non-SLA contact
+++++++++++++++

Clients without a specific SLA need to notify the support via the non emergency
ways:

* Email to support@flyingcircus.io (will be handled as stated obove in
  :ref:`supporttickets`.

* Phone call to our office at *+49 345 219401-0*.

.. _supporttickets:


Responsibilities of the system administration team
--------------------------------------------------

The system administration team ensures that the servers and networks run as
expected. It performs maintenance of the installed components, maintains
security, and develops new features.
