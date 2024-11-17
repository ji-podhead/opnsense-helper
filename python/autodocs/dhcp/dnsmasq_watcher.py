"""
script dnsmasq_watcher.py
------------------------------------------

*Parameters*
                        
* domain : str
    * Description: default domain to use 
    * options : ['--domain'] 
    * default : local 
    * required : False
* pid : str
    * Description: pid file location 
    * options : ['--pid'] 
    * default : /var/run/dnsmasq_dhcpd.pid 
    * required : False
* servicepid : str
    * Description: dnsmasq pid file location 
    * options : ['--servicepid'] 
    * default : /var/run/dnsmasq.pid 
    * required : False
* source : str
    * Description: source leases file 
    * options : ['--source'] 
    * default : /var/dhcpd/var/db/dhcpd.leases 
    * required : False
* target : str
    * Description: target config file 
    * options : ['--target'] 
    * default : /var/etc/dnsmasq-leases 
    * required : False
"""                  