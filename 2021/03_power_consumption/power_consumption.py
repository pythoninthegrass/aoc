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
You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""


def check_file(file):
    if not os.path.exists(file) or not os.path.getsize(file) > 0:
        print(f"File {file} does not exist or is empty")
        return True


def get_raw_data(file):
    with open(file, 'r') as f:
        return f.readlines()


def format_data(file):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
        df = pd.read_csv(file, dtype=str)
        df = df.to_string(index=False)
    return df

# TODO: calculate most common bit/least common bit (binary)
if __name__ == "__main__":
    raw_file = Path(cwd / "example.txt")
    check_file(raw_file)
    # data = get_raw_data(raw_file)
    data = format_data(raw_file)
    # ic(data)
    print(data)
