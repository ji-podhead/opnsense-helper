
"""
script reboot.sh
--------------------------------------------

Provides a hint to the console to reboot the system.

It checks if an update to the OPNsense core package is available and if the system needs to be rebooted.
Thescript uses the `pkg` command to query the package database and the `opnsense-update` command to check for updates.
If an update is available, thescript prints the next version number and exits with a status code of 0.
If no update is available, thescript exits with a status code of 1.

*Returns*
  - int
    - 0 if a reboot is not necessary, 1 if a reboot is necessary.

*Notes*
 - Thisscript assumes that the necessary commands (`pkg`, `opnsense-update`, `pluginctl`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""