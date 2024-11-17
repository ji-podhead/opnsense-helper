
"""
script ppp-linkup.sh
---------------------------------------

Handles the link up event for a PPP interface.


It configures the interface for the specified address family (inet or inet6).
It sets the DNS servers and router IP address if provided.
It also triggers the `configctl` command to update the interface configuration.

*Params*
 ${1} : str
     - IF: The name of the PPP interface.
 ${2} : str
     - AF: The address family (inet or inet6).
 ${3} : None
     - (unused)
 ${4} : str
     - ROUTER: The IP address of the router (optional).
 ${5} : None
     - (unused)
 ${6} : str
     - DNS1: The first DNS server IP address (optional).
 ${7} : str
     - DNS2: The second DNS server IP address (optional).

*Notes*
 - Thisscript assumes that the necessary commands (`ifctl`, `configctl`, `ppp-ipv6.php`) are available.
 - Thescript uses the `/tmp/${IF}_uptime` file to store the uptime of the PPP connection.
"""