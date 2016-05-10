General assumptions
===================

Maintaining the security of IT systems is an ongoing effort. We strive to
improve our understanding and measures for security continuously. For this we
rely on new insights generated in the IT security community from various
sources.

Process
-------

We currently do not employ a static formal process for developing security,
however our assessments and measures are based on formal processes like
ISO/IEC 27001, the German data security law, German IT Grundschutz, and
others.

.. note::
   Requirements that we intend to follow may be added to our documentation even
   if they have not been implemented yet. Those requirements are marked
   accordingly.


Low-security locations
----------------------

The Flying Circus operates two low-security zones called `development` (used
for the development of the Flying Circus infrastructure) and `WHQ` (used to
operate the Flying Circus offices and as a staging installation for
Flying Circus updates within a production context).

Those locations are currently not allowed to be used for customer data storage
as they not sufficiently protected to conform to the German federal data
protection laws.

Due to this limitation high-security locations are not allowed to depend on
services provided in low-security locations.
