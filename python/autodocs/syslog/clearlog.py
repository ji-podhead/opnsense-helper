"""

script clearlog.php
------------------------------------------------------------------------

Clears log files for a specific module or service.

This script removes log files for a specified module or service, and restarts the system syslog service.

*Params* -    argsv : array  
    -  - -h : Show help text and exit.
    -  - -m : Specify the module name.
    -  - -f : Specify the log file name.

*Arguments* 
  -   opts : array
    - An array of command-line options.
  -   mname : string
    - The name of the module or service.
  -   fname : string
    - The name of the log file.
  -   basename : string
    - The base path of the log file.

"""