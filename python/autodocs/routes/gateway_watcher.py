"""
script gateway_watcher.php
----------------------------------------------------------------------------------------------------------

Dieses Script überwacht die Gateways und generiert Alarme, wenn ein Gateway nicht erreichbar ist.

*Params*
    - $argv[1] : string
         - the action to execute: `configd_run($action)`

*Functions* 
   - signalhandler($signal) : Function called when a signal is received.
   - dpinger_status() : Function that returns the status of the gateways.
   - config_read_array($section, $key) : Function that returns an array from the configuration.
   - shell_safe($command, $args) : Function that safely executes a command.
   - syslog($priority, $message) : Function that writes a message to the system log.

*Variables*

  - $config : array The system configuration.
  - $mode : array An array that stores the status of the gateways.
  - $poll : int The poll interval in seconds.
  - $wait : int The wait interval in seconds.
  - $alarm : bool A flag that indicates whether an alarm has been generated.
"""