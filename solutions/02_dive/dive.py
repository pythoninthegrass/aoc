#!/usr/bin/env python3

import numpy as np
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


def get_data():
    try:
        formatted_file = Path(cwd / "formatted_input.txt")
        if os.path.exists(formatted_file) and os.path.getsize(formatted_file) > 0:
            with open(f"{cwd}/formatted_input.txt", 'r') as data:
                ic(data)
                return data.read().splitlines()
        else:
            with open(f"{cwd}/input.txt", 'r') as data:
                output = open(formatted_file, 'w')
                output.write(formatted_file, str(data))
    except Exception as e:
        print(f"Error: {e}")


class MoveItMoveIt:
    def __init__(self):
        self.pos = 0
        self.depth = 0

    def move(self, cmd):
        if cmd == "forward":
            self.pos += int(cmd[1])
        elif cmd == "down":
            self.depth += int(cmd[1])
        elif cmd == "up":
            self.depth -= int(cmd[1])
        # else:
        #     raise Exception("Unknown command")
        return self.pos, self.depth


def get_pos(direction):
    m = MoveItMoveIt()
    for item in direction:
        m.move(item)
    return int(m.pos * m.depth)


# TODO: `get_pos` is null; try list comp on times to get pos
if __name__ == "__main__":
    for item in get_data():
        item = str(item).strip()
        ic(item)
        print(get_pos(item))
        # times = str(item.rsplit(' ', 1)[1]).strip()    # 4
        # # times = str(item.strip().split(' ', 1))          # "['forward', '4']"
        # ic(times)
        # print(f"{item} -> {get_pos(str(item))}")
        # # df = pd.Series(data=ini_list, dtype=np.int64, index=range(len(ini_list)))
