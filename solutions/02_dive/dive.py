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
Your horizontal position and depth both start at 0. The steps above
would then modify them as follows:

    - forward 5 adds 5 to your horizontal position, a total of 5.
    - down 5 adds 5 to your depth, resulting in a value of 5.
    - forward 8 adds 8 to your horizontal position, a total of 13.
    - up 3 decreases your depth by 3, resulting in a value of 2.
    - down 8 adds 8 to your depth, resulting in a value of 10.
    - forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal
position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after
following the planned course. What do you get if you multiply your
final horizontal position by your final depth?
"""


def check_file(file):
    if not os.path.exists(file) or not os.path.getsize(file) > 0:
        print(f"File {file} does not exist or is empty")
        return True


def get_raw_data(file):
    with open(file, 'r') as f:
        return f.readlines()


def get_formatted_data(file):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
        # df = pd.read_csv(file)
        df = pd.read_feather(file)
        # print(df.to_string(index=False))
        return df


def write_formatted_data(data, file):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
        df = pd.DataFrame(data, columns=['direction', 'steps'])
        # df.to_csv(file, index=False)
        df.to_feather(file)
        # print(df.to_string(index=False))
        return df

class MoveItMoveIt:
    def __init__(self):
        self.pos = 0
        self.depth = 0

    # TODO: feather regression: `TypeError: unsupported operand type(s) for +=: 'int' and 'str'`
    def move(self, direction, steps):
        if direction == 'forward':
            self.pos += steps
        elif direction == "down":
            self.depth += steps
        elif direction == "up":
            self.depth -= steps
        # else:
        #     raise Exception("Unknown command")
        return self.pos, self.depth


def get_pos(direction, steps):
    m = MoveItMoveIt()
    for item in range(len(direction)):
        m.move(direction, steps)

    return m.pos, m.depth
    # return int(m.pos * m.depth)

# TODO: QA feather file
# TODO: now have pos and depth, need to multiply them
if __name__ == "__main__":
    raw_file = Path(cwd / "input.txt")
    formatted_file = Path(cwd / "formatted_input.feather")
    if check_file(formatted_file):
        raw_data = get_raw_data(raw_file)
        raw_data = [i.split() for i in raw_data]
        write_formatted_data(raw_data, formatted_file)

    df = get_formatted_data(formatted_file)
    ic(df)

    for item, row in df.iterrows():
        # ic(row['direction'], row['steps'])
        pos = get_pos(row['direction'], row['steps'])
        ic(pos)
        # pos_depth = pos[0] * pos[1]
        # ic(pos_depth)
