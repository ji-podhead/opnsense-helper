
"""
script sync.sh
---------------------------------------

Synchronizes the OPNsense system with the latest configuration.

It uses the `sync.subr.sh`script to perform the synchronization and logs its actions to the `${LOCKFILE}` file.

*Notes*
 - Thisscript assumes that the necessary commands (`opnsense-version`, `sync.subr.sh`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""