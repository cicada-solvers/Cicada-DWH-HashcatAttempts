# Cicada-DWH-HashcatAttempts 

To run tests yourself, clone this repository into your hashcat directory (so that 
Cicada-DWH-HashcatAttempts is its own subdirectory).

Then copy the allbytes.hcchr into your hashcat directory

Delete the contents of the `results` folder, but not the folder itself.

Run `python3 run_checks.py` to generate all of the results.
If you know the name of a specific check and hash you want to generate, the full command options are:
`python3 run_checks.py [checkname [hashname]]`

Tests and supported hashes can be changed from the `presets.py` file.

These tests were performed on Windows, however it *should* work with linux as well.
