"""

script setports.php
---------------------------------------------------------------------

This script configures the networking interfaces and ports for the system.

The script stops local servers to prevent faulty leases and then configures the interfaces, routing, DHCP, and VPN settings.



*Returns* 
  -   bool
    - true if the configuration was successful, false otherwise

This script requires the following files to be included:
 - config.inc
 - console.inc
 - filter.inc
 - util.inc
 - system.inc
 - interfaces.inc

"""