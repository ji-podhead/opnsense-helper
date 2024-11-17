"""
script reconfigure_vips.php
-------------------------------------------------------------------------

A script to reconfigure the Virtual IPs (VIPs).

*Functions* 
  -   legacy_interfaces_details(): Returns the interface details
  -   legacy_config_get_interfaces(): Returns the interface configurations
  -   legacy_interface_deladdress(): Deletes an IP address from an interface
  -   interface_ipalias_configure(): Configures an IP alias interface
  -   interface_carp_configure(): Configures a CARP interface
  -   interface_proxyarp_configure(): Configures the proxy ARP

*Flow*
 - Collects the IP addresses and their corresponding interfaces
 -  Removes deleted VIPs
 -  Compares the actual VIP configuration with the desired configuration
 -  Configures the VIPs based on the desired configuration
/
"""