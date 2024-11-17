
"""

script ifctl.sh
---------------------------------------

Configures and manages interface settings.

It supports various modes, including nameserver, prefix, router, and searchdomain.
It also supports IPv4 and IPv6 address families.
Thescript can perform various actions, including clearing, flushing, dumping, and listing interface settings.

*Params*
  - CMD: str
      Optional command to specify the action to perform.
      Possible values: -c, -d, -f, -l, -O
  - IF: str
      Interface name.
  - MD: str
      Mode to operate in. Possible values: nameserver, prefix, router, searchdomain
  - AF: str
      Address family. Possible values: inet, inet6
  - EX: str
      Extension to append to the file name.
  - DO_CONTENTS: str
      Contents to write to the file.
  - DO_VERBOSE: str
      Flag to enable verbose mode.

*Functions*

 - flush_routes: Flushes routes for the specified interface and mode.
 - flush_slaac: Flushes SLAAC addressing for the specified interface.

*Notes*  - Thisscript uses temporary files to store interface settings.
 - Thescript uses the `route` command to manipulate routes.
 - Thescript uses the `ifconfig` command to manipulate interface settings.
 - This Script uses getopts to parse command-line options:
       - getopts: getopts optstring name [arg ...]
       - Getopts is used by shell procedures to parse positional parameters as options.
"""