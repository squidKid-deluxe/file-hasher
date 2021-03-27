# file_hasher.py

`python3 file_hasher.py [command] [extension]`

File hasher takes command-line arguments, for example, to run `pylint <filename>` on all `*.py` files in the current directory, run

`python3 file_hasher.py pylint py`

The script concurrently checks if any `*.[extension]` files in the specified directory have changed, and if so, runs the `[command]` on each one individually.
