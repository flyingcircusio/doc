(infrastructure-storage)=

# Virtual Disks / Block Storage

VM storage is provided by a Ceph cluster as virtual disks / block devices.
The data in the cluster is transparently encrypted before being stored onto
physical disks, see [](#data-at-rest-encryption) for details.

Each virtual disk is visible in VMs as {file}`/dev/vda` and reflects an
underlying Ceph [RBD volume][rbd volume].

## Disk Layout

VMs are fitted with 3 different virtual disks:

`/dev/vda`

: This disk contains an XFS partition and is mounted to the VFS root(`/`) and
  has the nominal size as requested in the VM configuration. The minimum size
  is 30 GiB and it contains the operating system as well as your application
  and user data.

  Depending on the installed software you may need to reserve between 5-15 GiB
  of this disk for the operating system. Our use of NixOS has a higher
  footprint here than other OSes as we support atomic updates and may need to
  keep up to 4 copies of the OS environment in this store at some points in
  time.

`/dev/vdb`

: This disk contains swap. It is sized depending on your machine's memory and 
  is at least 1 GiB or 32 times the square root of your VMs memory.

  Swap is only provided to allow the VM some wiggle room if it runs out of
  memory in critical situations and allows for some room to interact and
  diagnose VMs that are running low on memory. Our VM configuration prefers to
  not use swap as much as possible as it impacts performance quite badly. 

  | VM memory | Swap size |
  |---|---|
  | 1 GiB | 1 GiB |
  | 2 GiB | 1.4 GiB |
  | 4 GiB | 2 GiB |
  | 8 GiB | 2.8 GiB |
  | 16 GiB | 4 GiB |
  | 32 GiB | 5.7 GiB |
  | 64 GiB | 8 GiB |

`/dev/vdc`

: contains an XFS partition used as a bounded `/tmp` filesystem. Some
  applications (like MySQl) exercise their use of /tmp based on available space
  of this partition and - if mounted to `/` - can cause the disk to fill up and
  cause issues for other applications.

  If your application needs a larger or more specific amount of temporary
  space, create a separate directory in your deployment and point your
  application to it by setting the `TMPDIR` environment variable (or use
  application specific configuration to adjust this).

  This disk is sized depending on your root disk: it is at least 5 GiB or
  the square root of your root disk.

  | VM root disk | /tmp size |
  |---|---|
  | 10 GiB | 5 GiB |
  | 50 GiB | 7 GiB |
  | 100 GiB | 10 GiB |
  | 250 GiB | 15 GiB |
  | 500 GiB | 22 GiB |

(infrastructure-storage-performance)=

## Storage Performance

We provide multiple storage pools with different performance characteristics, named **HDD** and **SSD** as an indicator of the expected performance:

|                 | HDD         | SSD        |
|:----------------|:-----------:|:----------:|
| IOPS (regular)  |         250 |      10000 |
| IOPS burst rate | 10× for 60s | 2× for 60s |
| bandwidth       |   250 MiB/s |  500 MiB/s |

The IOPS limit is accounted and enforced separately for *read* and *write* operations.  \
The bursting limits are calculated through the Qemu [*leaky bucket*][qemu-throttling] mechanism and thus can extend the burst period for burst rates smaller than the maximum.

[qemu-throttling]: https://github.com/qemu/qemu/blob/3656e761bcdd207b7759cdcd608212d2a6f9c12d/docs/throttle.txt

VM disks can be migrated between those pools by selecting a new pool. The VM
will detect the change and schedule a maintenance to perform the migration at a
convenient time.

Initialising the migration itself is a short offline operation, but takes only a
few seconds until the VM is then started again. The actual data migration
happens transparently in the background.

To speed up the process you can take the VM offline and online again to
initiate the migration immediately.


## Growing and shrinking disks

Virtual disks can be grown on the fly without shutting down the VM but shrinking
is not supported.

When *growing* a virtual disk, we enlarge the underlying RBD volume, adapt the
partition table and resize the main filesystem. This procedure is fully
transpart and can be performed without downtime.

*Shrinking* a virtual disk is not supported. To shrink a disk you need to 
provision a new VM and copy the data to a smaller disk.

[rbd volume]: http://docs.ceph.com/docs/master/architecture/

# S3-compatible Object Storage

Our Ceph cluster also provides an S3-compatible object storage.
The data in the cluster is transparently encrypted before being stored onto
physical disks, see [](#data-at-rest-encryption) for details.

## Creation

S3 users are managed in the customer portal at [my.flyingcircus.io](https://my.flyingcircus.io) in the "S3 Users" page.

```{image} ../images/infrastructure_s3_users_main.png
```

Click the "Add S3 user" button to create a new user. *manager* permission is required for this.

The user id is a suffix appended to the resource group name.
It can be used when there are multiple applications in one resource group which should not have access to each others data.
The display name is for your discretion to explain the use of the user. If left empty, it defaults to the user id.

```{image} ../images/infrastructure_s3_users_add.png
```

You will be redirected to a page that shows the secret key of the user.
Secret keys of a user are only shown once. If you loose the secret key, you can rotate the key in the customer portal.
This will invalidate the old secret key!

After a user is created, please allow up to 10 minutes for it to be created in the cluster.
You can see the current status of the user in the portal.
While the status is pending, it is not yet available:

```{image} ../images/infrastructure_s3_users_main_pending.png
```

As soon as the status changes to active, it can be used.

```{image} ../images/infrastructure_s3_users_main_active.png
```

## Deletion

When an S3 user is deleted, all owned buckets are also deleted in a multi-stage process that takes around 20 days.

The stages of deletion are:

Soft

: (at t=0)

  Revoke access keys. Acccess to the user and it's buckets is no longer possible.

  At this point you can still cancel the deletion. A new secret key is then generated.

Hard

: (t+14 days)

  Delete the S3 user and all owned buckets.

Recycle

: (t+20 days)

  Delete the S3 user deletion notice which will allows the S3 user id to be reused. 

## Access the cluster

To access our S3 cluster, you need to setup a gateway on a VM. Our support is happy to assist with that.
Currently, we only support path-style URL access. 

## Application Implementation Guidance

Object storages are flexible and scalable without having to worry too much
how they store the data. However, long term experience shows that a few rules
should be respected when implementing object storage in your application
to avoid problems later on and increase compatibility with third party
applications.

### Store the object locations in your application's database

The best investment you can make when starting (or evolving) your usage of S3
storage in your application is to store the specific bucket and object key in
your application's database together with the main object record. If you have a
table like "documents" then store your IDs like this:

```
ID      | object  | ... application data ... | s3uri
--------+---------+--------------------------|-----------------------------------------
5       | preview | ...                      | s3://myapp-2022-76fb4d2/preview/5.jpg
298376  | preview | ...                      | s3://myapp-2023-45df511/preview/298376.jpg
```

This allows you to later decide for a different organization scheme and change your application's code that generates those bucket names and object keys without having to immediately update your database or keep multiple generations of key generation code alive.

You can then write a (slow) migration script that checks all objects whether their bucket and id is still the one that your application would generate now and if it is not you can copy the object, update the database and delete the old object, to perform a no-downtime migration.

### Organize your objects using prefixes (use /pictures/1234.jpg instead of picture1234.jpg)

Theoretically you can grow bucket sizes almost infinitely and just throw objects
into it without any structure. However, S3 supports something resembling a file
hierarchy within a bucket by putting forward slashes ("/") into the key names.
This helps utilities that need to list keys because the API allows to
efficiently retrieve those listings by providing a search prefix. The "/" is a
common delimiter that many tools (like rclone) can automatically recognize and
use.

See details about using prefixes in S3 in the original documentation
(https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html). Be
aware that key lengths must be shorter than 1024 bytes!

Within a bucket your could use a "per client" and/or "per type" hierarchy, e.g. "<customer>/<type>/<objectid>" that would result in "acme/pictures/1234.jpg".

An alternative sharding criterion if your data does not have a native hierarchy
is to extract a prefix from within the name. If your data has some randomness
early in the filename then you could create an additional sharding layer.
Consider this list of files:

```
11-8999103.pdf
11-8999103.thumbnail.png
11-8999424.pdf
11-8999424.thumbnail.png
11-8999777.pdf
11-8999777.thumbnail.png
11-9000018.pdf
11-9000018.thumbnail.png
11-9000025.pdf
11-9000025.thumbnail.png
11-9000370.pdf
11-9000370.thumbnail.png
11-9000371.pdf
```

Which could be organized with the first 5 characters as a sharding layer:

```
.
├── 11-89
│   ├── 11-8999103.pdf
│   ├── 11-8999103.thumbnail.png
│   ├── 11-8999424.pdf
│   ├── 11-8999424.thumbnail.png
│   ├── 11-8999777.pdf
│   └── 11-8999777.thumbnail.png
└── 11-90
    ├──  11-9000018.pdf
    ├──  11-9000018.thumbnail.png
    ├──  11-9000025.pdf
    ├──  11-9000025.thumbnail.png
    ├──  11-9000370.pdf
    ├──  11-9000370.thumbnail.png
    └──  11-9000371.pdf
```

If your data does not have sufficient randomness in this way you can generate a
sharding layer by hashing your filenames and using the first few characters:

```
>>> import hashlib
>>> print(hashlib.sha256("11-9999991.thumbnail.png").hexdigest()[:2])
'72'
>>> print(hashlib.sha256("11-9999991.pdf").hexdigest()[:2])
'89'
```

This would result in the following sharding structure that distributes quite evenly on the first layer:

```
.
├── 40
│   └──11-9000370.pdf
├── 54
│   └──11-8999777.thumbnail.png
├── 59
│   └──11-9000025.pdf
├── 80
│   └──11-8999424.thumbnail.png
├── 84
│   └──11-9000018.thumbnail.png
├── 89
│   └──11-9000370.thumbnail.png
├── 99
│   └──11-9000018.pdf
├── 9b
│   ├──11-8999424.pdf
│   └──11-8999777.pdf
├── a3
│   └──11-9000025.thumbnail.png
├── c8
│   └──11-8999103.pdf
├── de
│   └──11-8999103.thumbnail.png
└── df
    └──11-9000371.pdf
```

### Be aware of the global bucket namespace (suffix your buckets with short uuids – "app-2022-d7b54fd")

S3 considers the bucket namespace to be global "within a partition". This means
that you must not rely in specific bucket names to be available to your
application. See Amazon's "Buckets overview" for more information.

Our recommendation is to use a combination of your applications name, the
sharding criteria and a short random uuid (7 hexdigits) and be prepared to
regenerate the random uuid if it already exists but was created by another
account. Examples of good bucket names:

```
myapp-2022-76ba5dd
myapp-cust1-54fdb32
```

Due to the inclusion of a random uuid you will also need to store the specific
bucket names that you have created in your application's database for certain
purposes, like ("this year's bucket for customer X is
named "myapp-X-2022-54fdb32").

### Limit total bucket size (organize buckets with "app-2022" or "app-customer1")

Another layer to make things more manageable is to create new buckets to
restrict a single bucket's total size (number of objects and data size). In
general you should not have a lot of buckets. It's fine to have large buckets
as long as you organize them as shown above. However, two reasons exist to
split your data into multiple buckets: failure domain and customer data
separation requirements.

Buckets are a failure domain in the sense that they maintain an internal index.
If this index becomes corrupt (which happens very rarely but has happened due
to bugs in the past) you need to rebuild the bucket based on your applications
data and copy the data to a new bucket. This can become extremely expensive and
slow (think: days or weeks) and may block other operations that rely on the
index (like backups) while rebuilding.

Also, if your customer requires a high level of data separation then it might be
reasonable to create a bucket per customer.

In general our recommendation is: if you don't have a per-customer separation
requirement, then default to splitting your buckets on a time basis, if you
don't know better, then create a new bucket every year.

Amazon hints that their default limit for number of buckets per customer is 100,
so creating a bucket structure that ends up with only few objects per buckets
is not generally recommended. Using multiple criteria to separate buckets will
almost always end up with too many buckets, so most applications will be fine
by sharding the buckets yearly and end up with something like this:

```
myapp-2021-65fdb33
myapp-2022-5ff14d5
myapp-2023-46663de
```
