"""
script latest.php
---------------------------------------------------------------------

Retrieves the latest stable version of OPNsense by parsing the changelog file.

*Params*- arsv[1] : str
    -   Path to the changelog file (default: /usr/local/opnsense/changelog/index.json)

*Returns* 
  -   string
    - The latest stable version of OPNsense, or the current version if unknown.
"""