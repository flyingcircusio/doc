(gis)=

# Mapnik

Provides libraries and tools for processing geographical data.

## Components

- [proj.4](http://trac.osgeo.org/proj/)
- [geos](http://trac.osgeo.org/geos/)
- [mapnik](http://mapnik.org/)
- [postgis](http://postgis.net/)

Note that a version of PostgreSQL 9.x must be installed as well.

## Upgrading

If PostGIS related database query show errors of the following form:

```
ERROR:  could not access file "$libdir/postgis-2.0": No such file or directory
```

the installed PostGIS database extensions need to be upgraded. Refer to
PostGIS' [upgrading guide](http://postgis.net/docs/manual-2.1/postgis_installation.html#upgrading) for
instructions.

% vim: set spell spelllang=en:
