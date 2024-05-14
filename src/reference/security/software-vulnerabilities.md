% last review: 2024-05-07

% review schedule: 1 year

% ISMSControl: A.12.6.1

# Software vulnerabilities

Security issues with system software installed on machines mainly rely on the
NixOS security process for mitigations. 

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

## NixOS 24.05 (upcoming)

This is the currently actively developed NixOS release that receives timely
security updates.

We update our platform frequently to follow upstream development.

## NixOS 23.11 (current)

This is the currently actively maintained NixOS release that receives timely
security updates. 

We update our platform with security updates every 2 weeks, but may update
intermittently if high risk vulnerabilities become known.

## NixOS 23.05 and older (outdated)

No security updates are provided. Customers in need of guaranteed security
updates are advised to update to NixOS 23.11

## NixOS 21.05 (outdated)

We are currently using NixOS 21.05 as our hardware platform due to interlocking
reasons to update some of the lower level infrastructure. We apply security
updates as needed for the components used.

Customers are not receiving security updates on 21.05 any longer.

## Gentoo (retired)

We do not provide security updates for this platform any longer. Customers
have been informed about the sunsetting of Gentoo since 2018. 
