"""
script tls_verify.php
---------------------------------------------------------------------

This script verifies the certificate depth for OpenVPN authentication.

It uses the OPNsense\OpenVPN\OpenVPN class to retrieve the server instance by ID.
It also uses the OPNsense\Trust\Store class to validate the OCSP response.
The script checks the certificate depth and OCSP validation for the given server ID.
If the verification fails, it logs a warning message and exits with a non-zero status code.

*Params*
    - argsv[0] : str
         - The auth_server  identifier for authentication.

*Returns* 
  - int
     - 0 on success, 1 on failure.
"""