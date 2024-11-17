
"""
script plugin.sh
---------------------------------------

Checks if a plugin is installed.

It uses the `opnsense-version` command to check if the plugin is installed, either in stable or development version.
Thescript returns 0 if the plugin is not installed, and 1 if it is installed.

*Params*
   - ${1} : str 
      - PLUGIN: The name of the plugin to check.

*Returns*
  - int
      - 0 if the plugin is not installed, 1 if it is installed.

*Notes*
 - Thisscript assumes that the `opnsense-version` command is available.
"""