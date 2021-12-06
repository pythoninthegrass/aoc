# Advent of Code Entries
<img src="https://user-images.githubusercontent.com/4097471/144654508-823c6e31-5e10-404c-9f9f-0d6b9d6ce617.jpg" width="300">

Here a few entries to the Advent of Code challenge, which is a coding challenge advent calendar created by Eric Wastl.

For more info: [Advent of Code site](http://adventofcode.com/)

## Usage
* Poetry
    * TODO
* Docker
    ```bash
    # move to repo directory
    cd aoc

    # build image w/Dockerfile
    docker build -t runner .

    # run default bash entrypoint
    docker run -it -v $(pwd):/home/appuser/app runner

    # run a script w/in container
    cd 01_sonar_sweep
    python sonar_sweep.py

    # stop container
    exit
    ```

## Debugging
* Raise cap of List Index Limit Max from 300 via
```bash
# ~/.vscode/extensions/ms-python.python-*/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_resolver.py
MAX_ITEMS_TO_HANDLE = 1000
```

## TODO
* Poetry usage
* ~~Dockerfile~~
* Keep going
