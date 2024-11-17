
"""script sync.subr.sh
---------------------------------------

Installs and updates plugins on the OPNsense system.

It uses the `pluginctl` command to retrieve the list of plugins to install, and the `pkg` command to install and update them.
Thescript also checks if the core package is up-to-date and if not, it displays an error message.
If all plugins are installed successfully, thescript removes any unnecessary packages.

*Notes*
 - Thisscript assumes that the necessary commands (`pluginctl`, `pkg`, `opnsense-version`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""