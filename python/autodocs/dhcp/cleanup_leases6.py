"""
script cleanup_leases6.php
-------------------------------------------------------------------------

Cleans up DHCPv6 leases by removing expired or unwanted leases.

This script reads the DHCPv6 lease file, removes leases that match the specified criteria, and writes the updated lease file.

*Params*

  -   argsv : array
         - -h : Show help text and exit.
         - -s : Restart the DHCPv6 service (required when the service is active).
         - -d=xxx : Remove the specified IPv6 address.
         - -f=dhcpd6.leases : Specify the DHCPv6 lease file (default: /var/dhcpd/var/db/dhcpd6.leases).


*Arguments* 
  -   dhcp_lease_file : string - The path to the DHCPv6 lease file (default: /var/dhcpd/var/db/dhcpd6.leases).
  -   opts : array - An array of command-line options.
  -   ip_to_remove : string - The IPv6 address to remove.

*Returns* 
  -   A JSON-encoded array with the number of removed leases.

"""