
"""

script connection.sh
------------------------------

Checks connectivity to OPNsense servers and verifies server certificates.

It uses the `opnsense-update` commands to determine the URLs of the servers,
and then checks connectivity to these servers over IPv4 and IPv6.
Finally, it verifies the server certificates.
"""