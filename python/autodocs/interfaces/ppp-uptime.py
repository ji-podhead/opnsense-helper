
"""

script ppp-uptime.sh
---------------------------------------

Calculates the uptime of a PPP connection.

It checks if the `/tmp/${IF}_uptime` file exists.
If the file exists, it calculates the uptime by subtracting the modification time of the file from the current time.
The uptime is returned in seconds.

*Params*
 - ${1} : str
    - IF: The name of the PPP interface.

*Returns*
- int
   - The uptime of the PPP connection in seconds.

*Notes*
 - Thisscript assumes that the necessary commands (`date`, `stat`) are available.
 - Thescript uses the `/tmp/${IF}_uptime` file to store the uptime of the PPP connection.
"""