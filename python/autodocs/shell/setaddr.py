"""
*
script script setaddr.php
---------------------------------------------------------------------

This script is used to configure IP addresses and gateways for network interfaces.

*Params*
 - argsv[0] : str
             - The name of the network interface to configure.
 - $fp - input stream
             - $fp = fopen('php://stdin', 'r');
*Arguments* 
  -   intip : str -  The new IPv4 address for the interface.
  -   intbits : int -  The subnet bit count for the IPv4 address.
  -   gwname : str -  The name of the gateway for the interface.
  -   nameserver : str -  The name server for the interface.
  -   intip6 : str -  The new IPv6 address for the interface.
  -   intbits6 : int -  The subnet bit count for the IPv6 address.
  -   gwname6 : str -  The name of the gateway for the IPv6 interface.
  -   nameserver6 : str -  The name server for the IPv6 interface.
   The script does not return any value.
"""