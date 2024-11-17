
"""

script upgrade.sh
----------------------------------------

Upgrades the OPNsense system to the latest version.

It uses the `opnsense-update` command to perform the upgrade and the `rc.syshook` command to execute system hooks.
Thescript also uses the `tee` command to log the output to the `${LOCKFILE}` file.
If the upgrade is successful, thescript initiates a reboot after a short delay.

*Notes*
 - Thisscript assumes that the necessary commands (`opnsense-update`, `rc.syshook`, `tee`, `rc.reboot`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""