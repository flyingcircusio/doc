---
Publish Date: '2013-06-13'
---

(hardware-specs)=

# Hardware specifications

All hardware we procure for our infrastructure will comply to the following
specifications. Older hardware may have been bought adhering to former
versions of the specification and will be upgraded over time and as necessary.

Housing customers' equipment also needs to comply to the specification valid
at the time of installation.

## Servers

All servers, independently of their role, require:

- 2 10 GE copper network ports, onboard, shared IPMI port (Intel)
- OS disks: 2 SSDs (internal or rear side)
- CPU-Architecture: x86_64
- BMC supporting IPMI 2.0 with serial console via LAN on shared port
- Redundant power supply
- Sliding rack rails
- Support contract for at least 5 years (next business day, parts
  included)
- Bootable, built-in rescue system

Historic requirements, usually always given nowadways:

- Needs to be bootable from USB flash drive
- PCIe bus

### Application servers

- Chassis: Thomas Krenn RI2208
- 512 GiB RAM
- 2x18 Core CPU at affordable speed
- Microarchitecture: Westmere+
- Machine name: kyleXX

### Storage servers

- Base: Thomas Krenn RI2224
- 16 slots for hard drives
- at leat 16 cores with sufficient thread performance (2x Intel Xeon E5-2640v3 8-Core)
- 128 GiB RAM
- HDD Pool: 2-3 Micron S610DC
- SSD Pool: 2-3 Intel 800 GB SATA III Intel SSD MLC 2,5" (DC S3610 Series)
- Journal: 400 GB Intel SSD MLC NVMe PCI-E 3.0 (DC P3700 Series)
- code name: cartmanXY

### Backup servers

- Base: Thomas Krenn RI1316
- No separate drives for system needed, it's OK to install on the big raid.
% FIXME: barbrady06 appears to use mdraid instead
- High-end hardware RAID controller (Avago MegaRAID 9361-8i SAS3 8x internal) including safe controller cache
- at least 15 x 2 TB SAS 7.2k disks, depending on actual requirements.
- at least 12 GiB RAM
- at least 4 processor cores
- code name: barbradyXY

### Routers

- at least 4 GiB RAM
- Power saving CPU
- code name: kennyXY

## Network infrastructure

### Switches

- Recommended models: Brocade VDX 6740T
- 24 Ports
- code name: stanXY

### Cabling

- Use Cat7
- Respect color coding
