"""

script ppp-ipv6.php
-------------------------------------

A script to configure PPP connections for IPv6.

*Arguments* 
  -   $argv[1]: The name of the interface
  -   $argv[2]: The family of the IP address (4 or 6)

*Parameters*

  -   $config: The system configuration
  -   $interface: The name of the interface
  -   $family: The family of the IP address

*Functions* 
  -   convert_real_interface_to_friendly_interface_name(string $interface): Converts the interface name to a friendly name
  -   interface_ppps_bound(string $interface, int $family): Checks if the interface is bound to a PPP connection
  -   interface_dhcpv6_prepare(string $interface, array $config): Prepares the DHCPv6 configuration for the interface
  -   interface_dhcpv6_configure(string $interface, array $config): Configures the DHCPv6 connection for the interface
  -   interface_static6_configure(string $interface, array $config): Configures the static IPv6 address for the interface
  -   system_routing_configure(bool $reload, string $interface, bool $ipv6, string $family): Configures the routing table for the interface

*Flow*
 - Checks if the required arguments are present
 -  Converts the interface name to a friendly name
 -  Checks if the interface is bound to a PPP connection
 -  Checks if the family of the IP address is correct
 -  Configures the DHCPv6 connection for the interface, if the family is 6
 -  Configures the static IPv6 address for the interface, if the family is 6
 -  Configures the routing table for the interface

*Outputs*

  -   No output, if the configuration is successful
  -   Exit code 1, if the configuration fails
"""