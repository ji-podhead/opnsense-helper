"""
script updaterrd.php
---------------------------------------------------------------------

This script updates the RRD (Round-Robin Database) statistics for OPNsense.

It uses the OPNsense\Core\Config class to retrieve the RRD configuration.
It also uses the OPNsense\RRD\Factory class to collect and update the RRD statistics.
The script checks if the RRD statistics are enabled and if the /var/db/rrd directory exists.
If debug mode is enabled, the script outputs the total runtime and collection time.

*Params* 
     - $argv : array
           -h : bool
                -      Display help message and exit.
           -d : bool
                -      Enable debug mode, output errors to stdout.

*Returns* 
  -   int
    - 0 on success, non-zero on failure.
"""