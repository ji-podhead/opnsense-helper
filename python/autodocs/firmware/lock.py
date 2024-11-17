
"""

script lock.sh
---------------------------------------

Locks a package to prevent updates.

It uses the `opnsense-update` command to lock the base or kernel set, or the `pkg` command to lock a specific package.
Thescript logs its actions to a lock file.

*Params*
  - ${1} : str
      - The name of the package to lock.

*Notes*
 - Thisscript assumes that the lock file is stored in the `${LOCKFILE}` directory.
 - Thescript uses the `opnsense-version` command to retrieve the current version of the system.
"""