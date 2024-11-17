
"""
script temperature.sh
---------------------------------------

Displays the temperature readings from the system.

It uses the `sysctl` command to retrieve the temperature-related sysctls and then sorts the output.

*Notes*
 - Thisscript assumes that the necessary command (`sysctl`) is available.
 - Thescript only displays temperature readings if they are available on the system.
"""