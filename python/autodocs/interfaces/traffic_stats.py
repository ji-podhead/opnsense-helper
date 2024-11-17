"""

script traffic_stats.php
---------------------------------------------------------------------

This script uses the `legacy_config_get_interfaces` and `legacy_interface_stats` functions to collect interface information and statistics.

It also uses the `map_ifs` function to map interface data to a standardized format.
If an interval is specified, the script will collect statistics at that interval and output the results in a streaming format.
If no interval is specified, the script will collect statistics once and output the results in a single JSON object.

*Params*
 - srgsv[0] : int
     - The interval in seconds to collect traffic statistics.

*Returns* 
  - string
     - The traffic statistics in JSON format.

/
"""