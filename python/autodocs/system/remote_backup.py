"""
script remote_backup.php
-----------------------------------------------------------------------

This script uses the BackupFactory class to manage backup providers.

The script assumes that the backup providers are configured correctly and that the necessary dependencies are .
This script is designed to be run remotely and can be used to perform backups at random intervals.

*Arguments* 
  -   $random_delay (optional): A random delay in seconds to add before starting the backup

*Functions* 
  -   BackupFactory::listProviders(): Returns a list of backup providers
  -   BackupProvider::isEnabled(): Checks if a backup provider is enabled
  -   BackupProvider::backup(): Performs a backup using a provider

*Flow*
 - Adds a random delay in seconds before starting the backup (if specified)
 -  Creates a BackupFactory instance
 -  Iterates over the list of backup providers
 -  Checks if each provider is enabled and performs a backup if it is
"""