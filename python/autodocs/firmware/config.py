
"""script env_init.sh
------------------------------

Initializes the environment for OPNsense firmware operations.

It checks if the OPNsense update is available and if so, sets environment
variables to disable TLS versions below 1.3, refreshes CRL files, and tells
libfetch to verify from the trust store.
"""