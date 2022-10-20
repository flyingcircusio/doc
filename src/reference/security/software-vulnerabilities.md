% last review: XXXX

% review schedule: 1 year

% ISMSControl: A.12.6.1

# Software vulnerabilities

Security issues with software installed on machines are monitored using a platform-specific process. Our processes (and specifically timelines) to mitigate vulnerabilities
depend on the support status of the respective platform.

When mitigating a vulnerability we may choose different strategies depending
on the situation:

- Ideally we will update the package to an unaffected version that stays API
  compatible.
- We may update to a package with API incompatibility but will help our customers
  to fix breakage.
- We may stay on the existing version and include a patch provided by the
  vendor, security researchers, other distributions or other sources we
  deem trustworthy after a review.
- We may contain the effect of the vulnerability by disabling features, adjusting
  configuration, firewalling or other measures.
- We may choose to ignore the security vulnerability if the impact or attack
  vectors are not relevant on our platform.
- We might take other actions not listed here, depending on the situation.

## NixOS 19.03

We actively monitor our code base and the packages that are actually installed
on customer systems (excluding user environments) for matches against public
vulnerability databases (i.e. NIST CVE).

We perform a scan for new vulnerabilities once a week and create work tickets
with different priorities based on multiple criteria of the vulnerability.

As we included some packages from the upstream NixOS unstable branch we
regularly keep this branch updated and thus include security fixed provided
by the NixOS community in a timely manner.

## NixOS 15.09 (outdated)

No security updates are provided. Customers in need of guaranteed security
updates are advised to update to NixOS 19.03.

## Gentoo (outdated)

We provide selective security updates by reviewing the published list of
Gentoo Linux Security Advisories (GLSA) every 2 months and selecting
critical security updates where necessary.
