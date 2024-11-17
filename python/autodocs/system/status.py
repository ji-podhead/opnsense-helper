"""
script status.php
---------------------------------------------------------------------

This script uses the OPNsense\System\SystemStatus class to retrieve the system status.

If an action is specified (dismiss), the script will dismiss the corresponding status.
If no action is specified, the script will display the system status in JSON format.

*Params*
  -   argsv[0] : str 
    - The action to perform on the system status (dismiss).

*Returns* 
  -   string
    - The system status in JSON format if no action is specified.

"""