
"""

script hostnames.sh
------------------------------

Retrieves the hosts of the repositories configured on the system.

It uses the `opnsense-verify` command to get the list of repositories,
and then parses the repository configuration files to extract the URLs.
It filters out non-HTTPS URLs and extracts the host from the remaining URLs.
The unique hosts are then printed to the console.

*Returns*
  - A list of unique hosts of the repositories.

"""