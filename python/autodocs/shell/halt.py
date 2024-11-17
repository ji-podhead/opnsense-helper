"""

script halt.php
----------------------------------------------------------------------

This script halts the system and powers it off after the user confirms that they want to proceed.

This script uses the passthru() function to execute the system command '/usr/local/etc/rc.halt'.
The user must confirm that they want to proceed before the system is shut down.

*Functions*
  -   require_once(string $filename) : void - Includes the specified file.
  -   fopen(string $filename, string $mode) : resource -  Opens a file or other file system.
  -   fgets(resource $stream) : string -  Reads a line from a file stream.
  -   strcasecmp(string $str1, string $str2) : int -  Compares two strings without considering case.
  -   passthru(string $command) : void -  Executes a system command and returns the output.
  -   fclose(resource $stream) : bool -  Closes a file stream.

*Variables*
    - fp : resource
    - A file stream opened to the standard input.

"""