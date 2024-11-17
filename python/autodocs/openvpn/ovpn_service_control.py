"""
script ovpn_service_control.php
----------------------------------------------------------------------------------------------------------

Controls the OpenVPN instances on the system.
It can be used to start, stop, restart, or configure instances.

*Parameters*
     - $argv : array
         - $argsv[-2] : str
             - action: stop|start|restart|configure
     - $argsv[-1] : str 
           - uuid: UUID of the instance
     - -a: all instances
     - -h: help

*Functions* 
  -   setup_interface($instance): Configures the network interface for the OpenVPN instance.
  -   ovpn_start($instance, $fhandle): Starts the OpenVPN instance.
  -   ovpn_stop($instance, $destroy_if = false): Stops the OpenVPN instance.
  -   ovpn_instance_stats($instance, $fhandle): Reads the statistics of the OpenVPN instance.
  -   get_vhid_status(): Reads the status of the CARP instances.
"""