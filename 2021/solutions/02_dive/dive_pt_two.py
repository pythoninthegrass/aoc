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
PT II
Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

    -down X increases your aim by X units.
    -up X decreases your aim by X units.
    -forward X does two things:
        - It increases your horizontal position by X units.
        - It increases your depth by your aim multiplied by X.

Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.
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
        df = pd.read_csv(file)
        # print(df.to_string(index=False))
        return df


def write_formatted_data(data, file):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
        df = pd.DataFrame(data, columns=['direction', 'steps'])
        df.to_csv(file, index=False)
        # print(df.to_string(index=False))
        return df

class MoveItMoveIt:
    def __init__(self):
        self.pos = 0
        self.depth = 0
        self.aim = 0


    def move(self, direction, steps):
        if direction == 'forward':
            self.pos += steps
            self.depth += self.aim * steps
        elif direction == "down":
            self.aim += steps
        elif direction == "up":
            self.aim -= steps
        return self.pos, self.depth


    def get_pos(self):
        return self.pos, self.depth

if __name__ == "__main__":
    raw_file = Path(cwd / "input.txt")
    formatted_file = Path(cwd / "input.csv")
    if check_file(formatted_file):
        raw_data = get_raw_data(raw_file)
        raw_data = [i.split() for i in raw_data]
        write_formatted_data(raw_data, formatted_file)

    df = get_formatted_data(formatted_file)
    ic(df)

    m = MoveItMoveIt()
    for item, row in df.iterrows():
        m.move(row['direction'], row['steps'])

    direction, depth = m.get_pos()
    ic(direction * depth)
