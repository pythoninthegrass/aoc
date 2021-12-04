#!/usr/bin/env python3

# SOURCES:

import numpy as np
import pandas as pd
import os
from pathlib import Path
from icecream import ic

## env
home = os.path.expandvars("$HOME")
cwd = Path(__file__).parent.absolute()

"""
Count the number of times a depth measurement increases from the previous measurement.
How many measurements are larger than the previous measurement?
"""

# QA
# 7 measurements that are larger than the previous measurement
test = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
nums = [int(i) for i in test]
df = pd.Series(nums)
ic(df.diff())
df_list = df.values.tolist()
ic(df_list)

# with open(f"{cwd}/input.txt", "r") as f:
#     lines = f.readlines()
#     ini_list = np.array(lines)
#     # ic("intial list: ", str(ini_list))
#     ini_list = [int(i) for i in ini_list]   # convert to int
#     s = pd.Series(ini_list)
#     ic(s.diff())
