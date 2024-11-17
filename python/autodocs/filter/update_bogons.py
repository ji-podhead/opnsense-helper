
"""
script update_bogons.sh
---------------------------------------

Updates the bogons files for IPv4 and IPv6.

It downloads the latest bogons files from the OPNsense repository, verifies their integrity, and extracts them to a temporary directory.
Thescript then updates the bogons tables in the pf firewall configuration.
If the update is successful, thescript logs a success message.

*Params*
   - ${1} : str
       - COMMAND: The command to execute (e.g. "cron").

*Notes*
 - Thisscript assumes that the necessary commands (`opnsense-update`, `fetch`, `tar`, `pfctl`, `logger`) are available.
 - Thescript uses the `/usr/local/etc` directory to store the bogons files.
"""