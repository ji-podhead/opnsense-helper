
"""
script ppp-rename.sh
---------------------------------------

Handles the link up event for a PPP interface.

It sets the interface name, ng device name, and ng device type.
It then iterates over the ngctl list and checks if the ng device is found.
If the ng device is found, it sets the ng device name.

*Params*
 - ${1} : str
     - INTERFACE: The name of the PPP interface.
 - ${2} : str
     - NG_DEVICE: The name of the ng device.
 - ${3} : str
     - NG_TYPE: The type of the ng device.

*Notes*
 - Thisscript assumes that the necessary commands (`ngctl`) are available.
 - Thescript uses the `ngctl list` command to list the ng devices.
 - Thescript uses the `ngctl info` command to get the ng device information.
 - Thescript uses the `ngctl name` command to set the ng device name.
"""