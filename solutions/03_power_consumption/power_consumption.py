#!/usr/bin/env python3

# import feather
# import numpy as np
import pandas as pd
import os
from pathlib import Path
from icecream import ic

## env
home = os.path.expandvars("$HOME")
cwd = Path(__file__).parent.absolute()
ic.configureOutput(includeContext=True)

"""
PT I
"""


def check_file(file):
    if not os.path.exists(file) or not os.path.getsize(file) > 0:
        print(f"File {file} does not exist or is empty")
        return True


def get_raw_data(file):
    with open(file, 'r') as f:
        return f.readlines()


def format_data(data):
    lst = []
    for d in data:
        lst.append(d.strip())

    return lst

# TODO: calculate most common bit/least common bit (binary)
if __name__ == "__main__":
    raw_file = Path(cwd / "example.txt")
    check_file(raw_file)
    data = get_raw_data(raw_file)
    formatted_file = format_data(data)
    ic(formatted_file)
