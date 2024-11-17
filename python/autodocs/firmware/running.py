
"""script running.sh
---------------------------------------

Checks if the OPNsense system is currently locked for updates.

It uses the `flock` command to check if the lock file is available.

*Returns*
  - "ready" if the system is not locked
  - "busy" if the system is locked

*Notes*
 - Thisscript assumes that the necessary commands (`flock`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
 - Thescript uses the `${LOCKFILE}` file to store the lock information.
"""