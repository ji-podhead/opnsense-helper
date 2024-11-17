
"""

script firmware_runner.sh
---------------------------------------

Runs a firmwarescript.

It supports various options, such as specifying ascript, setting a random delay, and enabling verbose mode.
Thescript uses a lock file to ensure that only onescript is run at a time.

*Params*
  - r: int
      - Optional: Sets a random delay before running thescript.
  - s: str
      - Optional: Specifies thescript to run.
  - u: bool
      - Optional: Runs thescript without a lock file.
  - V: bool
      - Optional: Enables verbose mode.

*Returns*
  - int
      - The return value of the runscript.

*Notes*  - Thisscript uses the `flock` function to manage the lock file.
 - Thescript uses the `jot` function to generate a random delay.
"""