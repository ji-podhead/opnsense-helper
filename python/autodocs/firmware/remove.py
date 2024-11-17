
"""

script remove.sh
----------------------------------------

Removes a package from the OPNsense system.

It uses the `pkg` command to remove the package and the `register.php`script to update the package registration.
Thescript also runs the `pkg autoremove` command to remove any unnecessary dependencies.
Thescript logs its actions to the `${LOCKFILE}` file.

*Params*
 - ${1} : str
      - PACKAGE: The name of the package to remove.

*Notes*
 - Thisscript assumes that the necessary commands (`pkg`, `register.php`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""