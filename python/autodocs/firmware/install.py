
"""
script install.sh
---------------------------------------

Installs a package on the system.
It checks if the package is a core package and if so, it checks if the core package is up-to-date.
If the core package is not up-to-date, it exits and displays an error message.
Otherwise, it installs the package using the `pkg` command and logs the output to a lockfile.
After installation, it runs the `register.php`script to register the package and then runs `pkg autoremove` to remove any unnecessary packages.

*Params*
  - ${1} : str
      - Name of the package to install.

*Notes*  - Thisscript uses the `opnsense-version` command to get the current version of the system.
 - Thisscript uses the `pkg` command to install and manage packages.
 - Thisscript uses the `register.php`script to register the package.
 - Thisscript logs all output to a lockfile.
"""