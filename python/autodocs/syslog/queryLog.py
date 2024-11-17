"""
script queryLog.py
------------------------------------------

*Parameters*
                        
* output : str
    * Description: output type [json/text] 
    * options : ['--output'] 
    * default : json 
    * required : False
* filter : str
    * Description: filter results 
    * options : ['--filter'] 
    * default :  
    * required : False
* limit : str
    * Description: limit number of results 
    * options : ['--limit'] 
    * default :  
    * required : False
* offset : str
    * Description: begin at row number 
    * options : ['--offset'] 
    * default :  
    * required : False
* filename : str
    * Description: log file name (excluding .log extension) 
    * options : ['--filename'] 
    * default :  
    * required : False
* module : str
    * Description: module 
    * options : ['--module'] 
    * default : core 
    * required : False
* severity : str
    * Description: comma separated list of severities 
    * options : ['--severity'] 
    * default :  
    * required : False
* valid_from : str
    * Description: oldest data to search for (epoch) 
    * options : ['--valid_from'] 
    * default :  
    * required : False
"""                  