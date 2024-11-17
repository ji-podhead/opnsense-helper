"""

script gateways.php
------------------------------------------------------------------------

Retrieves a list of gateways and their corresponding IP addresses or protocols.

This script retrieves a list of gateways and their corresponding IP addresses or protocols, and outputs the result in JSON format.

*Params*
    - $argvs : array
         -  -g : Adds gateway groups to the result.
         -  -h : Displays the usage help.

*Returns* 
  -   A JSON-encoded array containing the list of gateways and their corresponding IP addresses or protocols.

*Functions* 
    - getopt(string $shortopts, array $longopts = [], int &$optind = 0) : array
    - Parses the command-line options.
    - array_slice(array $array, int $offset, int $length = null) : array
    - Extracts a slice of the array.
    - is_ipaddr(string $ip) : bool
    - Checks if the given string is a valid IP address.

*Variables*
  -   mdl : \OPNsense\Routing\Gateways -  An instance of the Gateways class.
  -   gateways : array -  An array containing the list of gateways.
  -   ret : array -  An array to store the result.
  -   opts : array -  An array containing the parsed command-line options.
  -   args : array -  An array containing the remaining command-line arguments.


"""