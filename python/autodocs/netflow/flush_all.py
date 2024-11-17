
"""

script flush_all.sh
------------------------------

Flushes local netflow data.

If the "all" argument is provided, it stops the flowd and flowd_aggregate services,
removes all netflow data files and log files, and then starts the services again.

*Params*
  - ${1}: str
      - If str == "all" provided, all local netflow data will be flushed.


"""