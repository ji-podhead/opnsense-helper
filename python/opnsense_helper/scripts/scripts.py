
from  opnsense_helper.utils.exec_class import Exec_Class
Exec_Class
scripts_folder="/usr/local/opnsense/scripts/"

class Scripts():
     """
     class Scripts
     -----------------------------

     Initialize the Scripts class.
     * its just a wrapper for all the opnsense scripts classes. see attributes below.
    
     **Usage**

          .. code-block:: python

               Onsense_Helper.scripts.<attribute>.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class 
               * The parent object containing the needed ssh connection and the temp path to the config.xml.
     
     **Attributes**

         * unbound : unbound instance
         * system : system instance
         * syslog : syslog instance
         * suricata : suricata instance
         * shell : shell instance
         * shaper : shaper instance
         * routes : routes instance
         * openvpn : openvpn instance
         * openssh : openssh instance
         * netflow : netflow instance
         * ipsec : ipsec instance
         * interfaces : interfaces instance
         * health : health instance
         * firmware : firmware instance
         * filter : filter instance
         * dns : dns instance
         * dhcp : dhcp instance
         * auth : auth instance
         * Wireguard : Wireguard instance
     """
     def __init__(self,base):

          
          self.unbound=unbound(base)
          self.system=system(base)
          self.syslog=syslog(base)
          self.suricata=suricata(base)
          self.shell=shell(base)
          self.shaper=shaper(base)
          self.routes=routes(base)
          self.openvpn=openvpn(base)
          self.openssh=openssh(base)
          self.netflow=netflow(base)
          self.ipsec=ipsec(base)
          self.interfaces=interfaces(base)
          self.health=health(base)
          self.firmware=firmware(base)
          self.filter=filter(base)
          self.dns=dns(base)
          self.dhcp=dhcp(base)
          self.auth=auth(base)
          self.Wireguard=Wireguard(base)

class unbound(Exec_Class):
     """
     class unbound
     -----------------------------

     * Initializes the unbound class, inheriting from Exec_Class. 
    
     **Usage**

          .. code-block:: python

               Scripts.unbound.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details

     **Attributes**

     - commands : dict
          A dictionary of command configurations with keys for configctl options,
          each containing command details such as the command string, arguments, 
          and flags.

          scripts:
               * wrapper: executes wrapper.py
               * stats: executes stats.py
               * start: executes start.sh
               * restore_db: executes restore_db.py
               * logger: executes logger.py
               * check: executes check.sh*
               * cache: executes cache.sh*
               * blocklists: executes blocklists.py
     """  
     def __init__(self, base):
   
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "wrapper":{ "command":scripts_folder+"ubound/wrapper.py*","flags":[]},
          "stats":{ "command":scripts_folder+"ubound/stats.py*","flags":[]},
          "start":{ "command":scripts_folder+"ubound/start.sh*","flags":[]},
          "restore_db":{ "command":scripts_folder+"ubound/restore_db.py*","flags":[]},
          "logger":{ "command":scripts_folder+"ubound/logger.py*","flags":[]},
          "check":{ "command":scripts_folder+"ubound/check.sh*","flags":[]},
          "cache":{ "command":scripts_folder+"ubound/cache.sh*","flags":[]},
          "blocklists":{ "command":scripts_folder+"ubound/blocklists.py*","flags":[]},
          "blocklists":{ "command":scripts_folder+"ubound/blocklists/","flags":[]},
          }
class system(Exec_Class):
     """
     class system
     -----------------------------

     Initializes the system class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.system.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for system operations,
          each containing command details such as the command string and flags.

          scripts:
               * trigger_config_changed_events: executes trigger_config_changed_events.py
               * temperature: executes temperature.sh
               * sysctl: executes sysctl.py
               * status: executes status.php
               * ssl_ciphers: executes ssl_ciphers.py
               * rrd_pfstate_info: executes rrd_pfstate_info.py
               * rfc5246_cipher_suites: executes rfc5246_cipher_suites.csv
               * remote_backup: executes remote_backup.php
               * nameservers: executes nameservers.php
               * certctl: executes certctl.py
               * activity: executes activity.py
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "trigger_config_changed_events":{"command":scripts_folder+"system/trigger_config_changed_events.py*", "flags":[]},
          "temperature":{"command":scripts_folder+"system/temperature.sh*", "flags":[]},
          "sysctl":{"command":scripts_folder+"system/sysctl.py*", "flags":[]},
          "status":{"command":scripts_folder+"system/status.php*", "flags":[]},
          "ssl_ciphers":{"command":scripts_folder+"system/ssl_ciphers.py*", "flags":[]},
          "rrd_pfstate_info":{"command":scripts_folder+"system/rrd_pfstate_info.py*", "flags":[]},
          "rfc5246_cipher_suites":{"command":scripts_folder+"system/rfc5246_cipher_suites.csv", "flags":[]},
          "remote_backup":{"command":scripts_folder+"system/remote_backup.php*", "flags":[]},
          "nameservers":{"command":scripts_folder+"system/nameservers.php*", "flags":[]},
          "certctl":{"command":scripts_folder+"system/certctl.py*", "flags":[]},
          "activity":{"command":scripts_folder+"system/activity.py*", "flags":[]},
          }
class syslog(Exec_Class):
     """
     class syslog
     -----------------------------

     Initializes the syslog class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.syslog.run(<command>,<argument>,<flags>)
     
     **Parameters**

          base : Base_Class instance
          The parent object containing necessary SSH connection details and  configuration settings. 

     **Attributes**

     - commands : dict
          A dictionary of command configurations for syslog operations,
          each containing command details such as the command string and flags.

          scripts:
               * queryLog: executes queryLog.py
               * logformats: executes logformats/
               * log_archive: executes log_archive*
               * lockout_handler: executes lockout_handler*
               * list_applications: executes list_applications.php
               * generate_certs: executes generate_certs*
               * clearlog: executes clearlog.php
     """

     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "queryLog":{"command":scripts_folder+"syslog/ queryLog.py*", "flags":[]},
          "logformats":{"command":scripts_folder+"syslog/ logformats/", "flags":[]},
          "log_archive":{"command":scripts_folder+"syslog/ log_archive*", "flags":[]},
          "lockout_handler":{"command":scripts_folder+"syslog/ lockout_handler*", "flags":[]},
          "list_applications":{"command":scripts_folder+"syslog/ list_applications.php*", "flags":[]},
          "generate_certs":{"command":scripts_folder+"syslog/ generate_certs*", "flags":[]},
          "clearlog":{"command":scripts_folder+"syslog/ clearlog.php*", "flags":[]},
          }
class suricata(Exec_Class):
     """
     class suricata
     -------------------------------------------------
     
     Initializes the suricata class, inheriting from Exec_Class.
    
     **Usage**

          .. code-block:: python

               Scripts.suricata.run(<command>,<argument>,<flags>)
     
     **Parameters**

          base : Base_Class instance
          The parent object containing necessary SSH connection details and  configuration settings. 

     **Attributes**

     - commands : dict
          A dictionary of command configurations for suricata operations

          scripts:
               * setup: executes setup.sh*
               * rule-updater: executes rule-updater.py*
               * queryInstalledRules: executes queryInstalledRules.py*
               * queryAlertLog: executes queryAlertLog.py*
               * metadata: executes metadata/
               * listRuleMetadata: executes listRuleMetadata.py*
               * listInstallableRulesets: executes listInstallableRulesets.py*
               * listAlertLogs: executes listAlertLogs.py*
               * lib: executes lib/
               * installRules: executes installRules.py*
               * dropAlertLog: executes dropAlertLog.py*
               * __init__: executes __init__.py*
     """
     def __init__(self, base):
    
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "setup":{"command":scripts_folder+"suricata/setup.sh*", "flags":[]},
          "rule-updater":{"command":scripts_folder+"suricata/rule-updater.py*", "flags":[]},
          "queryInstalledRules":{"command":scripts_folder+"suricata/queryInstalledRules.py*", "flags":[]},
          "queryAlertLog":{"command":scripts_folder+"suricata/queryAlertLog.py*", "flags":[]},
          "metadata":{"command":scripts_folder+"suricata/metadata/", "flags":[]},
          "listRuleMetadata":{"command":scripts_folder+"suricata/listRuleMetadata.py*", "flags":[]},
          "listInstallableRulesets":{"command":scripts_folder+"suricata/listInstallableRulesets.py*", "flags":[]},
          "listAlertLogs":{"command":scripts_folder+"suricata/listAlertLogs.py*", "flags":[]},
          "lib":{"command":scripts_folder+"suricata/lib/", "flags":[]},
          "installRules":{"command":scripts_folder+"suricata/installRules.py*", "flags":[]},
          "dropAlertLog":{"command":scripts_folder+"suricata/dropAlertLog.py*", "flags":[]},
          "__init__":{"command":scripts_folder+"suricata/__init__.py*", "flags":[]},
          }
class shell(Exec_Class):
     """
     class Shell
     ..........

     Initializes the shell class, inheriting from Exec_Class.
    
     **Usage**

          .. code-block:: python

               Scripts.shell.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
          The parent object containing necessary SSH connection details and  configuration settings. 

     **Attributes**

     - commands : dict
          A dictionary of command configurations for shell operations,
          each containing command details such as the command string and flags.

          scripts:
               * setports: executes setports.php
               * setaddr: executes setaddr.php
               * restore: executes restore.sh
               * reboot: executes reboot.php
               * ping: executes ping.php
               * password: executes password.php
               * halt: executes halt.php
               * firmware: executes firmware.sh
               * defaults: executes defaults.php
               * banner: executes banner.php
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "setports":{"command":scripts_folder+"shell/setports.php*","flags":[]},
          "setaddr":{"command":scripts_folder+"shell/setaddr.php*","flags":[]},
          "restore":{"command":scripts_folder+"shell/restore.sh*","flags":[]},
          "reboot":{"command":scripts_folder+"shell/reboot.php*","flags":[]},
          "ping":{"command":scripts_folder+"shell/ping.php*","flags":[]},
          "password":{"command":scripts_folder+"shell/password.php*","flags":[]},
          "halt":{"command":scripts_folder+"shell/halt.php*","flags":[]},
          "firmware":{"command":scripts_folder+"shell/firmware.sh*","flags":[]},
          "defaults":{"command":scripts_folder+"shell/defaults.php*","flags":[]},
          "banner":{"command":scripts_folder+"shell/banner.php*","flags":[]},
          }
class shaper(Exec_Class):
     """
     class Shaper
     -----------------------------

     Initializes the shaper class, inheriting from Exec_Class.
    
     **Usage**

          .. code-block:: python

               Scripts.suricata.shaper(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for shaper operations,
          each containing command details such as the command string and flags.

          scripts:
               * update_tables: executes update_tables
               * lib: executes lib/
               * dummynet_stats: executes dummynet_stats.py*
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "update_tables":{"command":scripts_folder+"shaper/update_tables*","flags":[]},
          "lib":{"command":scripts_folder+"shaper/lib/","flags":[]},
          "dummynet_stats":{"command":scripts_folder+"shaper/dummynet_stats.py*","flags":[]},
          }
class routes(Exec_Class):
     """
     class routes
     -----------------------------

     Initializes the routes class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.routes.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for routes operations,
          each containing command details such as the command string and flags.

          scripts:
               * show_routes: executes show_routes.py
               * gateways: executes gateways.php
               * gateway_watcher: executes gateway_watcher.php
               * gateway_status: executes gateway_status.php
               * del_route: executes del_route.py
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "show_routes":{"command":scripts_folder+"routes/show_routes.py*","flags":[]},
          "gateways":{"command":scripts_folder+"routes/gateways.php*","flags":[]},
          "gateway_watcher":{"command":scripts_folder+"routes/gateway_watcher.php*","flags":[]},
          "gateway_status":{"command":scripts_folder+"routes/gateway_status.php*","flags":[]},
          "del_route":{"command":scripts_folder+"routes/del_route.py*","flags":[]},
          }
class openvpn(Exec_Class):
     """
     class openvpn
     -----------------------------
     
     Initializes the openvpn class, inheriting from Exec_Class.

    
     **Usage**

          .. code-block:: python

               Scripts.openvpn.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for openvpn operations,
          each containing command details such as the command string and flags.

          scripts:
               * user_pass_verify: executes user_pass_verify.php
               * tls_verify: executes tls_verify.php
               * ovpn_status: executes ovpn_status.py
               * ovpn_service_control: executes ovpn_service_control.php
               * ovpn_event: executes ovpn_event.py
               * kill_session: executes kill_session.py
               * client_disconnect: executes client_disconnect.sh
               * client_connect: executes client_connect.php
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "user_pass_verify":{"command":scripts_folder+"openvpn/user_pass_verify.php*", "flags":[]},
          "tls_verify":{"command":scripts_folder+"openvpn/tls_verify.php*", "flags":[]},
          "ovpn_status":{"command":scripts_folder+"openvpn/ovpn_status.py*", "flags":[]},
          "ovpn_service_control":{"command":scripts_folder+"openvpn/ovpn_service_control.php*", "flags":[]},
          "ovpn_event":{"command":scripts_folder+"openvpn/ovpn_event.py*", "flags":[]},
          "kill_session":{"command":scripts_folder+"openvpn/kill_session.py*", "flags":[]},
          "client_disconnect":{"command":scripts_folder+"openvpn/client_disconnect.sh*", "flags":[]},
          "client_connect":{"command":scripts_folder+"openvpn/client_connect.php*", "flags":[]},
          }
class openssh(Exec_Class):
     """
     class openssh
     ------------------------------
     
     Initializes the openssh class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.openssh.run(<command>,<argument>,<flags>)
     
     **Parameters**

     base : Base_Class instance
          The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for openssh operations,
          each containing command details such as the command string and flags.

          scripts:
               * ssh_query: executes ssh_query.py
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={ 
          "ssh_query":{"command":scripts_folder+"openssh/ssh_query.py*","flags":[]}
          }

class netflow(Exec_Class):
     """
     class netflow
     ------------------------------

     Initialize the netflow class, inheriting from Exec_Class.

     **Usage**

     .. code-block:: python

          Scripts.netflow.run(<command>,<argument>,<flags>)

     **Parameters:**
     base : Base_Class instance
          The parent object containing necessary SSH connection details.

     **Attributes:**
     - commands : dict
          A dictionary of command configurations for netflow operations,
          each containing command details such as the command string and flags.

          scripts:
          - lib: executes the netflow library directory
          - get_top_usage: executes get_top_usage.py script
          - get_timeseries: executes get_timeseries.py script
          - flush_all: executes flush_all.sh script
          - flowd_aggregate_metadata: executes flowd_aggregate_metadata.py script
          - flowd_aggregate: executes flowd_aggregate.py script
          - export_details: executes export_details.py script
          - dump_log: executes dump_log.py script
          - flowctl_stats: executes flowctl_stats.py script
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "lib":{"command":scripts_folder+"netflow/lib/","flags":[]},
          "get_top_usage":{"command":scripts_folder+"netflow/get_top_usage.py*","flags":[]},
          "get_timeseries":{"command":scripts_folder+"netflow/get_timeseries.py*","flags":[]},
          "flush_all":{"command":scripts_folder+"netflow/flush_all.sh*","flags":[]},
          "flowd_aggregate_metadata":{"command":scripts_folder+"netflow/flowd_aggregate_metadata.py*","flags":[]},
          "flowd_aggregate":{"command":scripts_folder+"netflow/flowd_aggregate.py*","flags":[]},
          "flowctl_stats":{"command":scripts_folder+"netflow/flowctl_stats.py*","flags":[]},
          "export_details":{"command":scripts_folder+"netflow/export_details.py*","flags":[]},
          "dump_log":{"command":scripts_folder+"netflow/dump_log.py*","flags":[]},
          }
class ipsec(Exec_Class):
     """
     class ipsec
     ------------------------------
     
     Initializes the ipsec class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.ipsec.run(<command>,<argument>,<flags>)
               
     **Parameters:**
     base : Base_Class instance
          The parent object containing necessary SSH connection details.

     **Attributes:**
     - commands : dict
          A dictionary of command configurations for ipsec operations,
          each containing command details such as the command string and flags.

          scripts:
          - lib: executes the ipsec library directory
          - updown_event: executes updown_event.py
          - spddelete: executes spddelete.py
          - saddelete: executes saddelete.py
          - list_status: executes list_status.py
          - list_spd: executes list_spd.py
          - list_sad: executes list_sad.py
          - list_leases: executes list_leases.py
          - get_legacy_vti: executes get_legacy_vti.php
          - disconnect: executes disconnect.py
          - connect: executes connect.py
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "updown_event":{"command":scripts_folder+"ipsec/updown_event.py*","flags":[]},
          "spddelete":{"command":scripts_folder+"ipsec/spddelete.py*","flags":[]},
          "saddelete":{"command":scripts_folder+"ipsec/saddelete.py*","flags":[]},
          "list_status":{"command":scripts_folder+"ipsec/list_status.py*","flags":[]},
          "list_spd":{"command":scripts_folder+"ipsec/list_spd.py*","flags":[]},
          "list_sad":{"command":scripts_folder+"ipsec/list_sad.py*","flags":[]},
          "list_leases":{"command":scripts_folder+"ipsec/list_leases.py*","flags":[]},
          "lib":{"command":scripts_folder+"ipsec/lib/","flags":[]},
          "get_legacy_vti.":{"command":scripts_folder+"ipsec/get_legacy_vti.php*","flags":[]},
          "disconnect":{"command":scripts_folder+"ipsec/disconnect.py*","flags":[]},
          "connect":{"command":scripts_folder+"ipsec/connect.py*","flags":[]},
          }
class interfaces(Exec_Class):
     """
     class interfaces
     ---------------------------------

     Initializes the interfaces class, inheriting from Exec_Class.
    
     **Usage**

          .. code-block:: python

               Scripts.interfaces.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for interfaces operations,
          each containing command details such as the command string and flags.

          scripts:
               * traffic_top: executes traffic_top.py
               * traffic_stats: executes traffic_stats.php
               * traceroute: executes traceroute.py
               * rtsold_resolvconf: executes rtsold_resolvconf.sh
               * reconfigure_vlans: executes reconfigure_vlans.php
               * reconfigure_vips: executes reconfigure_vips.php
               * reconfigure_neighbors: executes reconfigure_neighbors.php
               * reconfigure_laggs: executes reconfigure_laggs.php
               * ppp-uptime: executes ppp-uptime.sh
               * ppp-rename: executes ppp-rename.sh
               * ppp-linkup: executes ppp-linkup.sh
               * ppp-linkdown: executes ppp-linkdown.sh
               * portprobe: executes portprobe.py
               * ping: executes ping.py
               * mpd: executes mpd.script
               * macinfo: executes macinfo.py
               * list_sockstat: executes list_sockstat.py
               * list_ndp: executes list_ndp.py
               * list_macdb: executes list_macdb.py
               * list_arp: executes list_arp.py
               * ifctl: executes ifctl.sh
               * dhclient: executes dhclient-script
               * carp_set_status: executes carp_set_status.php
               * carp_global_status: executes carp_global_status.php
               * capture: executes capture.py
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "traffic_top":{"command": scripts_folder+"interfaces/traffic_top.py*", "flags":[]},
          "traffic_stats":{"command": scripts_folder+"interfaces/traffic_stats.php*", "flags":[]},
          "traceroute":{"command": scripts_folder+"interfaces/traceroute.py*", "flags":[]},
          "rtsold_resolvconf":{"command": scripts_folder+"interfaces/rtsold_resolvconf.sh*", "flags":[]},
          "reconfigure_vlans":{"command": scripts_folder+"interfaces/reconfigure_vlans.php*", "flags":[]},
          "reconfigure_vips":{"command": scripts_folder+"interfaces/reconfigure_vips.php*", "flags":[]},
          "reconfigure_neighbors":{"command": scripts_folder+"interfaces/reconfigure_neighbors.php*", "flags":[]},
          "reconfigure_laggs":{"command": scripts_folder+"interfaces/reconfigure_laggs.php*", "flags":[]},
          "ppp-uptime":{"command": scripts_folder+"interfaces/ppp-uptime.sh*", "flags":[]},
          "ppp-rename":{"command": scripts_folder+"interfaces/ppp-rename.sh*", "flags":[]},
          "ppp-linkup":{"command": scripts_folder+"interfaces/ppp-linkup.sh*", "flags":[]},
          "ppp-linkdown":{"command": scripts_folder+"interfaces/ppp-linkdown.sh*", "flags":[]},
          "portprobe":{"command": scripts_folder+"interfaces/portprobe.py*", "flags":[]},
          "ping":{"command": scripts_folder+"interfaces/ping.py*", "flags":[]},
          "mpd":{"command": scripts_folder+"interfaces/mpd.script*", "flags":[]},
          "macinfo":{"command": scripts_folder+"interfaces/macinfo.py*", "flags":[]},
          "list_sockstat":{"command": scripts_folder+"interfaces/list_sockstat.py*", "flags":[]},
          "list_ndp":{"command": scripts_folder+"interfaces/list_ndp.py*", "flags":[]},
          "list_macdb":{"command": scripts_folder+"interfaces/list_macdb.py*", "flags":[]},
          "list_arp":{"command": scripts_folder+"interfaces/list_arp.py*", "flags":[]},
          "ifctl":{"command": scripts_folder+"interfaces/ifctl.sh*", "flags":[]},
          "dhclient":{"command": scripts_folder+"interfaces/dhclient-script*", "flags":[]},
          "carp_set_status":{"command": scripts_folder+"interfaces/carp_set_status.php*", "flags":[]},
          "carp_global_status":{"command": scripts_folder+"interfaces/carp_global_status.php*", "flags":[]},
          "capture":{"command": scripts_folder+"interfaces/capture.py*", "flags":[]},
          }
class health(Exec_Class):
     """
     class heatlh
     -----------------
     
     Initializes the health class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.health.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for health operations,
          each containing command details such as the command string and flags.

          scripts:
               * listReports: executes listReports.py
               * flush_rrd: executes flush_rrd.py
               * fetchData: executes fetchData.py
     """
     def __init__(self, base):

          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "listReports":{"command":scripts_folder+"health/listReports.py*","flags":[]},
          "flush_rrd":{"command":scripts_folder+"health/flush_rrd.py*","flags":[]},
          "fetchData":{"command":scripts_folder+"health/fetchData.py*","flags":[]},
          }
class firmware(Exec_Class):
     """
     clas firmware 
     ---------------
     
     Initializes the firmware class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.firmware.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for firmware operations,
          each containing command details such as the command string and flags.

          scripts:
               * upgrade: executes upgrade.sh
               * update: executes update.sh
               * unlock: executes unlock.sh
               * sync.subr: executes sync.subr.sh
               * sync: executes sync.sh
               * security: executes security.sh
               * running: executes running.sh
               * resync: executes resync.sh
               * remove: executes remove.sh
               * reinstall: executes reinstall.sh
               * register.: executes register.php
               * reboot: executes reboot.sh
               * read: executes read.sh
               * query: executes query.sh
               * product.: executes product.php
               * plugin: executes plugin.sh
               * lock: executes lock.sh
               * license: executes license.sh
               * launcher: executes launcher.sh
               * latest.: executes latest.php
               * install: executes install.sh
               * health: executes health.sh
               * connection: executes connection.sh
               * check: executes check.sh
               * changelog: executes changelog.sh
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "upgrade":{"command":scripts_folder+"firmware/upgrade.sh*","flags":[]},
          "update":{"command":scripts_folder+"firmware/update.sh*","flags":[]},
          "unlock":{"command":scripts_folder+"firmware/unlock.sh*","flags":[]},
          "sync.subr":{"command":scripts_folder+"firmware/sync.subr.sh*","flags":[]},
          "sync":{"command":scripts_folder+"firmware/sync.sh*","flags":[]},
          "security":{"command":scripts_folder+"firmware/security.sh*","flags":[]},
          "running":{"command":scripts_folder+"firmware/running.sh*","flags":[]},
          "resync":{"command":scripts_folder+"firmware/resync.sh*","flags":[]},
          "remove":{"command":scripts_folder+"firmware/remove.sh*","flags":[]},
          "reinstall":{"command":scripts_folder+"firmware/reinstall.sh*","flags":[]},
          "register.":{"command":scripts_folder+"firmware/register.php*","flags":[]},
          "reboot":{"command":scripts_folder+"firmware/reboot.sh*","flags":[]},
          "read":{"command":scripts_folder+"firmware/read.sh*","flags":[]},
          "query":{"command":scripts_folder+"firmware/query.sh*","flags":[]},
          "product.":{"command":scripts_folder+"firmware/product.php*","flags":[]},
          "plugin":{"command":scripts_folder+"firmware/plugin.sh*","flags":[]},
          "lock":{"command":scripts_folder+"firmware/lock.sh*","flags":[]},
          "license":{"command":scripts_folder+"firmware/license.sh*","flags":[]},
          "launcher":{"command":scripts_folder+"firmware/launcher.sh*","flags":[]},
          "latest.":{"command":scripts_folder+"firmware/latest.php*","flags":[]},
          "install":{"command":scripts_folder+"firmware/install.sh*","flags":[]},
          "health":{"command":scripts_folder+"firmware/health.sh*","flags":[]},
          "connection":{"command":scripts_folder+"firmware/connection.sh*","flags":[]},
          "check":{"command":scripts_folder+"firmware/check.sh*","flags":[]},
          "changelog":{"command":scripts_folder+"firmware/changelog.sh*","flags":[]},
          }
class filter(Exec_Class):
     """
     class filter
     --------------
     Initializes the filter class, inheriting from Exec_Class.
     
     **Usage**

          .. code-block:: python

               Scripts.filter.run(<command>,<argument>,<flags>)
     
     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details and  configuration settings. 

     **Attributes**

     - commands : dict
          A dictionary of command configurations for filter operations

          scripts:
               * update_tables: executes update_tables.py*
               * update_bogons: executes update_bogons.sh*
               * run_unittests: executes run_unittests.py*
               * rule_stats: executes rule_stats.py*
               * rollback_timer.: executes rollback_timer.php*
               * rollback_cancel.: executes rollback_cancel.php*
               * read_log: executes read_log.py*
               * pftop: executes pftop.py*
               * pftablecount: executes pftablecount.py*
               * pfstatistics: executes pfstatistics.py*
               * list_tables: executes list_tables.py*
               * list_table: executes list_table.py*
               * list_states: executes list_states.py*
               * list_rule_ids: executes list_rule_ids.py*
               * list_pfsync: executes list_pfsync.py*
               * list_osfp: executes list_osfp.py*
               * kill_table: executes kill_table.py*
               * kill_states: executes kill_states.py*
               * find_table_references: executes find_table_references.py*
               * download_geoip: executes download_geoip.py*
               * delete_table: executes delete_table.py*
     """
     def __init__(self, base):
    
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "update_tables":{"commands":scripts_folder+"filter/update_tables.py*","flags":[]},
          "update_bogons":{"commands":scripts_folder+"filter/update_bogons.sh*","flags":[]},
          "run_unittests":{"commands":scripts_folder+"filter/run_unittests.py*","flags":[]},
          "rule_stats":{"commands":scripts_folder+"filter/rule_stats.py*","flags":[]},
          "rollback_timer.":{"commands":scripts_folder+"filter/rollback_timer.php*","flags":[]},
          "rollback_cancel.":{"commands":scripts_folder+"filter/rollback_cancel.php*","flags":[]},
          "read_log":{"commands":scripts_folder+"filter/read_log.py*","flags":[]},
          "pftop":{"commands":scripts_folder+"filter/pftop.py*","flags":[]},
          "pftablecount":{"commands":scripts_folder+"filter/pftablecount.py*","flags":[]},
          "pfstatistics":{"commands":scripts_folder+"filter/pfstatistics.py*","flags":[]},
          "list_tables":{"commands":scripts_folder+"filter/list_tables.py*","flags":[]},
          "list_table":{"commands":scripts_folder+"filter/list_table.py*","flags":[]},
          "list_states":{"commands":scripts_folder+"filter/list_states.py*","flags":[]},
          "list_rule_ids":{"commands":scripts_folder+"filter/list_rule_ids.py*","flags":[]},
          "list_pfsync":{"commands":scripts_folder+"filter/list_pfsync.py*","flags":[]},
          "list_osfp":{"commands":scripts_folder+"filter/list_osfp.py*","flags":[]},
          "kill_table":{"commands":scripts_folder+"filter/kill_table.py*","flags":[]},
          "kill_states":{"commands":scripts_folder+"filter/kill_states.py*","flags":[]},
          "find_table_references":{"commands":scripts_folder+"filter/find_table_references.py*","flags":[]},
          "download_geoip":{"commands":scripts_folder+"filter/download_geoip.py*","flags":[]},
          "delete_table":{"commands":scripts_folder+"filter/delete_table.py*","flags":[]},
          }
class dns(Exec_Class):
     """
     class dns
     ------------
     
     Initializes the dns class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.dns.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict

          scripts:
               * query_dns: executes query_dns.py
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "query_dns":{"commands":scripts_folder+"dns/query_dns.py*","flags":[]}
          }

class dhcp(Exec_Class):
     """
     class dhcp
     -----------
     
     Initializes the dhcp class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.dhcp.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict

          scripts:
               * unbound_watche: executes unbound_watcher.py*
               * prefixe: executes prefixes.sh*
               * prefixes: executes prefixes.php*
               * get_leases: executes get_leases6.py*
               * get_lease: executes get_leases.py*
               * get_kea_lease: executes get_kea_leases.py*
               * dnsmasq_watche: executes dnsmasq_watcher.py*
               * cleanup_leases6: executes cleanup_leases6.php*
               * cleanup_leases4: executes cleanup_leases4.php*
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "unbound_watche":{"command":scripts_folder+"dhcp/unbound_watcher.py*","flags":[]},
          "prefixe":{"command":scripts_folder+"dhcp/prefixes.sh*","flags":[]},
          "prefixes":{"command":scripts_folder+"dhcp/prefixes.php*","flags":[]},
          "get_leases":{"command":scripts_folder+"dhcp/get_leases6.py*","flags":[]},
          "get_lease":{"command":scripts_folder+"dhcp/get_leases.py*","flags":[]},
          "get_kea_lease":{"command":scripts_folder+"dhcp/get_kea_leases.py*","flags":[]},
          "dnsmasq_watche":{"command":scripts_folder+"dhcp/dnsmasq_watcher.py*","flags":[]},
          "cleanup_leases6":{"command":scripts_folder+"dhcp/cleanup_leases6.php*","flags":[]},
          "cleanup_leases4":{"command":scripts_folder+"dhcp/cleanup_leases4.php*","flags":[]},
          }
class auth(Exec_Class):
     """
     class  auth
     ---------------
     
     Initializes the auth class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.auth.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for auth operations,
          each containing command details such as the command string and flags.

          scripts:
               * list_group_members: executes list_group_members.php
               * add_user: executes add_user.php
     """
     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "list_group_members":{"command":scripts_folder+"auth/list_group_members.php*","flags":[]},
          "add_user":{"command":scripts_folder+"auth/add_user.php*","flags":[]},
          }
class Wireguard(Exec_Class):
     """
     class Wireguard
     -----------------

     Initializes the Wireguard class, inheriting from Exec_Class.

     **Usage**

          .. code-block:: python

               Scripts.Wireguard.run(<command>,<argument>,<flags>)

     **Parameters**

          base : Base_Class instance
               The parent object containing necessary SSH connection details.

     **Attributes**

     - commands : dict
          A dictionary of command configurations for Wireguard operations,
          each containing command details such as the command string and flags.

          scripts:
               * wg_show: executes wg_show.py
               * wg-service-control: executes wg-service-control.php
               * reresolve-dns: executes reresolve-dns.py
               * gen_keypair: executes gen_keypair.py
     """

     def __init__(self, base):
     
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "wg_show":{"command":scripts_folder+"wireguard/wg_show.py*","flags":[]},
          "wg-service-control":{"command":scripts_folder+"wireguard/wg-service-control.php*","flags":[]},
          "reresolve-dns":{"command":scripts_folder+"wireguard/reresolve-dns.py*","flags":[]},
          "gen_keypair":{"command":scripts_folder+"wireguard/gen_keypair.py*","flags":[]},
          }