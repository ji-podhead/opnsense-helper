"""
script OPNsense.php
---------------------------------------------------------------------

Updates the OPNsense configuration based on the system settings.

It also checks for a subscription key and appends the URL suffix if present.
If no subscription key is set, the license file is deleted.

*Params*

  - argsv : array
         - -A: specifies the ABI (Architecture-Based Interface) to use
         - -m: specifies the mirror URL to use
         - -n: specifies the flavour to use 
"""