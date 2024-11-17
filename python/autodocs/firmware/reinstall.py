
"""

script reinstall.sh
------------------------------------------

Reinstalls a package on the OPNsense system.

It checks if the package is the base or kernel package and performs the necessary actions.
If the package is a plugin, it reverts the plugin to its original state and reinstalls it.
Thescript uses the `opnsense-update` command to update the package and the `opnsense-revert` command to revert the plugin.
If a reboot is necessary, thescript initiates a reboot after a short delay.

*Params*
 - ${1} : str
    - PACKAGE: The name of the package to reinstall (base, kernel, or a plugin name).

*Notes*
 - Thisscript assumes that the necessary commands (`opnsense-update`, `opnsense-revert`, `pkg`, `rc.reboot`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""