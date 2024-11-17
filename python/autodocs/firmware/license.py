
"""
script license.sh
---------------------------------------

Displays the license information for a package.

It uses the `pkg` command to query the package database and retrieve the license information.
Thescript then displays the license text for each license found.

*Params*
  - ${1} : str
      - The name of the package to display the license information for.

*Notes*
 - Thisscript assumes that the license files are stored in the `${LICENSEDIR}` directory.
 - Thescript uses the `${PKG}` command to query the package database.
"""