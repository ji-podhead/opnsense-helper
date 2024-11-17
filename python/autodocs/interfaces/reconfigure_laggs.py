"""
script reconfigure_laggs.php
-------------------------------------------------------------------------

A script to reconfigure LAGG interfaces.

This script uses the `file_exists`, `filesize`, `fopen`, `flock`, `fread`, `fwrite`, `ftruncate`, `explode`, `trim`, and other functions to interact with the file system and configure the LAGG interfaces

*Arguments* 
  -   $laggs_todo: An array to store the LAGG interfaces to reconfigure
  -   $vfilename: The path to the file containing the LAGG interfaces to reconfigure
  -   $lagg_configure: An array to store the LAGG interfaces to reconfigure

*Functions* 
  -   file_exists(string $filename): Checks if a file exists
  -   filesize(string $filename): Returns the size of a file
  -   fopen(string $filename, string $mode): Opens a file pointer
  -   flock(resource $handle, int $operation): Locks or unlocks a file
  -   fread(resource $handle, int $length): Reads from a file pointer
  -   fwrite(resource $handle, string $string): Writes to a file pointer
  -   ftruncate(resource $handle, int $size): Truncates a file to a specified size
  -   explode(string $delimiter, string $string): Splits a string into an array using a delimiter
  -   trim(string $string): Removes whitespace from a string
  -   OPNsense\Interfaces\Lagg()->lagg->iterateItems(): Iterates over the LAGG interfaces
  -   legacy_interface_destroy(string $interface): Destroys a legacy interface
  -   _interfaces_lagg_configure(array $lagg): Configures a LAGG interface

*Flow*
 - Reads the file containing the LAGG interfaces to reconfigure
 -  Collects the LAGG interfaces to reconfigure
 -  Removes non-existing interfaces
 -  Reconfigures the still existing LAGG interfaces
"""