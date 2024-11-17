"""
script netboot.php
-------------------------------------

A script to reboot the system after confirmation.

This script uses the `fopen`, `fgets`, `chop`, `strcasecmp`, `passthru`, and `fclose` functions to interact with the user and execute the reboot command.
The script assumes that the `/usr/local/etc/rc.reboot` command is available on the system and will reboot the system.

*Parameters*

  -   $fp: The file pointer for standard input

*Functions* 
  -   fopen(string $filename, string $mode): Opens a file pointer
  -   fgets(resource $fp): Reads a line from the file pointer
  -   chop(string $string): Removes trailing whitespace from a string
  -   strcasecmp(string $str1, string $str2): Compares two strings in a case-insensitive manner
  -   passthru(string $command): Executes a shell command and displays the output
  -   fclose(resource $fp): Closes a file pointer

*Flow*
 - Opens the standard input file pointer
 -  Prompts the user to confirm the reboot
 -  Reads the user input and checks if it matches 'y' (case-insensitive)
 -  If confirmed, executes the `/usr/local/etc/rc.reboot` command to reboot the system
 -  Closes the standard input file pointer

*Outputs*

  -   The output of the reboot command (if executed)

"""