#!/usr/bin/env python3

import numpy as np
import pandas as pd
import os
from pathlib import Path
from icecream import ic

## env
home = os.path.expandvars("$HOME")
cwd = Path(__file__).parent.absolute()

"""
PT I
Count the number of times a depth measurement increases from the previous measurement.
How many measurements are larger than the previous measurement?
"""


# QA
# 7 measurements that are larger than the previous measurement
# test = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
# nums = [int(i) for i in test]
# df = pd.Series(data=nums, dtype=np.int64, index=range(len(nums)))
# pos_measures = df[df > df.shift()]
# print(pos_measures.count())

with open(f"{cwd}/input.txt", "r") as f:
    lines = f.readlines()
    ini_list = np.array(lines)
    # ic("intial list: ", str(ini_list))
    ini_list = [int(i) for i in ini_list]   # convert to int
    df = pd.Series(data=ini_list, dtype=np.int64, index=range(len(ini_list)))
    # ic(s.diff())
    pos_measures = df[df > df.shift()]
    ic(pos_measures.count())


"""
PT II
Count the number of times the sum of measurements in this sliding window
increases from the previous sum. So, compare A with B, then compare B with C,
then C with D, and so on. Stop when there aren't enough measurements left to
create a new three-measurement sum.
How many sums are larger than the previous sum?
"""

