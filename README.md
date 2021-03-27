# file_hasher.py

`python3 file_hasher.py [command] file [extention]`

File hasher takes command-line arguments, for example, to run `pylint <filename>` on all `*.py` files in the current directory, run

`python3 file_hasher.py pylint file py`

The script concurrently checks if any *.[extention] files in the working directory have changed, and if so, runs the [command] on each on individually.
