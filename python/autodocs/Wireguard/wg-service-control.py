"""
wg-service-control.php

This script controls the Wireguard service, allowing for start, stop, restart, and configure actions.

*Usage*
  php wg-service-control.php [-a] [-h] [stop|start|restart|configure] [uuid|vhid]

*Params* -   $argsv : array
    -  - argsv[-2] : str
    -    - action: stop|start|restart|configure
    -  - argsv[-1] : str
    -    - uuid|vhid: The UUID or vhid of the Wireguard instance
    -  - -a: Perform the action on all instances
    -  - -h: Display this help message

*Actions*
  stop: Stop the Wireguard service
  start: Start the Wireguard service
  restart: Restart the Wireguard service
  configure: Configure the Wireguard service

*Parameters*
  uuid: The UUID of the Wireguard instance to control
  vhid: The vhid of the Wireguard instance to control

/**
function wg_start

Start the Wireguard service for the given server.

@param object $server The Wireguard server object
@param resource $fhandle The file handle for the stat file
@param string $ifcfgflag The interface configuration flag (default: 'up')
@param bool $reload Whether to reload the configuration (default: false)

@return void
function wg_stop

Stop the Wireguard service for the given server.

@param object $server The Wireguard server object

@return void
function wg_reconfigure_hash

Calculate a hash that determines if the Wireguard service can be reconfigured without a restart.

@param object $server The Wireguard server object

@return string The reconfiguration hash
function get_stat_hash

Get the stat hash for the given file handle.

@param resource $fhandle The file handle for the stat file

@return array The stat hash array
"""