
"""
script start.sh
---------------------------------------

Starts the Unbound DNS resolver and configures it for use with OPNsense.

It removes any existing configuration files, checks for the presence of the root.key file, and runs unbound-anchor if necessary.
Thescript then copies configuration files from /usr/local/etc/unbound.opnsense.d to /var/unbound/etc and sets the ownership of the files to the unbound user.
Finally, thescript starts the Unbound service and loads the DNS cache.

*Params*
 - ${1} : str
     - DOMAIN: The domain name to use for DHCP and DNS configuration.

*Notes*
 - Thisscript assumes that the necessary commands (`unbound`, `unbound-anchor`, `unbound-control-setup`, `chown`, `daemon`) are available.
 - Thescript uses the `/usr/local/opnsense/scripts/unbound` directory for Unbound-relatedscripts and configuration files.
"""