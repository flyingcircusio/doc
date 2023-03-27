(infrastructure-storage)=

# Virtual Disks / Block Storage

VM storage is provided by a Ceph cluster. Each block device visible in VMs
(e.g., {file}`/dev/vda` or {file}`/dev/sda`) reflects an underlying Ceph [RBD
volume][rbd volume].

## Disk Layout

Each RBD volume contains a complete virtual disk image consisting of a partition
table and one or more filesystems. We use both XFS and ext4 filesystems in VMs.

## Growing and shrinking disks

Such a virtual disk is quite easy to grow but not so easy to shrink.

When *growing* a virtual disk, we enlarge the underlying RBD volume, adapt the
partition table and resize the main filesystem. This procedure is fully
transpart and can be performed without downtime.

*Shrinking* a virtual disk is not directly supported. On customer request, we
install a filesystem quota to ensure that no more space is used than booked. On
newer NixOS VMs with XFS filesystems, tools like
{command}`df` report that reduced size correctly. Older Gentoo-based VMs
with ext4 filesystems are not so smart; {command}`df` still
reports the old size even when a quota is installed.  Nonetheless, we will
monitor disk usage on basis of the reduced disk size.

[rbd volume]: http://docs.ceph.com/docs/master/architecture/

# S3-compatible Object Storage

Our Ceph cluster also provides an S3-compatible object storage. Contact our
support to get you started with credentials.

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
