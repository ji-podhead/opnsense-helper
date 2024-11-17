
"""
script rtsold_resolvconf.sh
-------------------------------

Processes Router Advertisements (RA) with RDNSS and DNSSL options.

Thisscript is invoked by rtsold when a Router Advertisement with RDNSS  and DNSSL options is received. It extracts the interface, router, and DNS information from the arguments and STDIN.

*Params*
 - ${1} : str
      - Action: 
           - "-a" to add DNS information
           - "-d" to delete DNS information
 - ${2} : str
      - Interface information: "ifname:slaac:[RA source address]"

*Notes*
 - Thisscript uses the ifctl(8) and configctl(8) commands to modify
   the interface configuration.
 - It uses the /var/etc/radvd.conf file to recognize its own configuration.
"""