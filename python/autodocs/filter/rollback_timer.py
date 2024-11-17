"""
script rollback_timer.php
-----------------------------------------------------------------------

A script to manage the rollback timer for firewall filter changes.

It uses the OPNsense\Firewall\Filter class to manage firewall filter changes.
It is used to manage the rollback timer for firewall filter changes.

*Params*   
  - argsv[0] : int
     - (optional): The revision number to cancel

*Functions* 
  -   OPNsense\Firewall\Filter::rollback($revision): Rolls back to the specified revision
  -   OPNsense\Core\Backend::configdRun($command): Runs a command on the backend

*Flow*
 - Checks the command-line arguments for the revision number
 -  Creates a lock file for the revision
 -  Waits for 60 seconds for the API to callback
 -  If the lock file is deleted, exits with success
 -  If the lock file still exists, rolls back to the specified revision
 -  Reloads the firewall filter configuration if the rollback is successful

"""