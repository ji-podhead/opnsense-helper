
"""
script unlock.sh
---------------------------------------

Unlocks a package or set on the OPNsense system.

It uses the `opnsense-update` command to unlock the base or kernel sets, and the `pkg` command to unlock other packages.
Thescript logs its actions to the `${LOCKFILE}` file.

*Params*
 - ${1} : str
     - PACKAGE: The name of the package or set to unlock.

*Notes*
 - Thisscript assumes that the necessary commands (`opnsense-update`, `pkg`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""