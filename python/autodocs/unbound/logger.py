"""
script logger.py
------------------------------------------

*Parameters*
                        
* pipe : str
    * Description: named pipe file location 
    * options : ['--pipe'] 
    * default : /var/unbound/data/dns_logger 
    * required : False
* targetdb : str
    * Description: duckdb filename 
    * options : ['--targetdb'] 
    * default : /var/unbound/data/unbound.duckdb 
    * required : False
* backup_dir : str
    * Description: backup directory 
    * options : ['--backup_dir'] 
    * default : /var/cache/unbound.duckdb 
    * required : False
* flush_interval : str
    * Description: interval to flush to db 
    * options : ['--flush_interval'] 
    * default : 10 
    * required : False
"""                  