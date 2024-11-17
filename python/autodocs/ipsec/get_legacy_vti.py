"""

script get_legacy_vti.php
--------------------------------------------------------------------------------------------------------

This script uses the ipsec_get_configured_vtis() function to retrieve the list of configured IPsec VTIs.

The result is output in JSON format using the json_encode() function.

*Returns*
  -   A JSON-encoded array containing the list of configured IPsec VTIs.

*Functions*
  -   require_once(string $filename) : void -  Includes the specified file.
  -   ipsec_get_configured_vtis() : array -  Retrieves a list of configured IPsec VTIs.
  -   json_encode(array $data) : string -  Encodes the data in JSON format.

*Arguments*
  -   result : array -  An array to store the result.
  -   vti : array -  The current VTI.
  -   record : array -  An array to store the VTI record.

"""