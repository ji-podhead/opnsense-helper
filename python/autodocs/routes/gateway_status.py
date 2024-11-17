"""

script gateway_status.php
--------------------------------------------------------------------------------------------------------

This script retrieves the status of gateways using the dpinger_status() function, and generates a JSON-encoded result containing information about each gateway.



*Returns* 
  -   A JSON-encoded array containing information about each gateway.

*Functions* 
  -   dpinger_status() : Retrieves the status of gateways.

*Variables*

  -   result : array - An array to store the result of the script.
  -   gateways_status : array    - An array containing the status of each gateway.
  -   gname : string - The name of the current gateway.
  -   gw : array - An array containing information about the current gateway.
  -   gatewayItem : array    - An array to store information about the current gateway.
  -   status_translated : string - A translated version of the status of the current gateway.

"""