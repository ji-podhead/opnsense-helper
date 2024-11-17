
"""
script ppp-linkdown.sh
---------------------------------------

Handles the link down event for a PPP interface.

It shuts down the PPP connection using `ngctl`.
It performs different actions based on the address family:
 - For inet, it disables IPv4 forwarding and routing, and removes the IPv4 address.
 - For inet6, it disables IPv6 forwarding and routing, and removes the IPv6 address.
It also logs the uptime of the PPP connection and updates the uptime log file.

*Params*
 - {1}: str
      - The name of the PPP interface.
 - {2} : str
      - The address family (inet or inet6).

*Notes*
 - Thisscript assumes that the necessary commands (`ngctl`, `ifctl`, `configctl`, `ppp-uptime.sh`) are available.
 - Thescript uses the `/conf/${IF}.log` file to log the uptime of the PPP connection.
 - Thescript uses the `/tmp/${IF}_uptime` file to store the uptime of the PPP connection.
"""