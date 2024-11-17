"""
script password.php
-------------------------------------

A script to reset the root user account.

*Parameters*

  - $argv[2] and $argv[3]: Options for the script
     - -h 0: Mocking "pw usermod root -h 0"
     - -x 0: Creates a new root user if none exists
  -   $fp : input stream

*Functions* 
  -   getUserEntryByUID(int $uid): Returns the user entry for the given UID
  -   local_user_set_password(array $user, string $password): Sets the password for the given user
  -   local_user_set(array $user): Saves the user entry
  -   write_config(string $message): Writes a message to the configuration

*Flow*
 - Checks if the options -h 0 or -x 0 were provided
 -  If -h 0, sets the password for the root user
 -  If -x 0, creates a new root user if none exists and sets the password
 -  If no options were provided, asks if the user wants to restore the default authentication mode
 -  If the user wants to restore the default authentication mode, sets the password for the root user

*Outputs*

  -   Messages for resetting the root user account
  -   Error messages if the password is empty or does not match
"""