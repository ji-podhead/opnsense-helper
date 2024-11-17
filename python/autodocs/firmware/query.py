
"""
script query.sh
----------------------------------------

Retrieves version information for OPNsense.

It uses the `opnsense-version` command to retrieve version information for the base and kernel sets.
It also uses the `pkg` command to retrieve package information.
Thescript supports three modes:
 - local: Retrieves version information for the local OPNsense installation.
 - remote: Retrieves version information from a remote repository.
 - tiers: Retrieves product tier annotations from a remote repository.

*Params*
 - ${1} : str
     - MODE: The mode to retrieve version information (local, remote, tiers).

*Returns*
  - str
    - The version information in a formatted string.

*Notes*
 - Thisscript assumes that the necessary commands (`opnsense-version`, `pkg`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
"""