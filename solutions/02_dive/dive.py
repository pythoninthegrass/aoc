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


class MoveItMoveIt:
    def __init__(self):
        self.pos = 0
        self.depth = 0

    def move(self, cmd):
        if cmd[0] == "forward":
            self.pos += int(cmd[1])
        elif cmd[0] == "down":
            self.depth += int(cmd[1])
        elif cmd[0] == "up":
            self.depth -= int(cmd[1])
        # else:
        #     raise Exception("Unknown command")
        return self.pos, self.depth


def get_pos(cmds):
    m = MoveItMoveIt()
    for cmd in cmds:
        m.move(cmd)
    return int(m.pos * m.depth)


# TODO: `get_pos` is null; try list comp on num to get pos
with open(f"{cwd}/input.txt", "r") as f:
    lines = f.readlines()
    ini_list = np.array(lines)
    ini_list = [i for i in ini_list]
    for i in ini_list:
        cmd = str(i)
        ic(cmd)
        # num = str(i.rsplit(' ', 1)[1]).strip()    # 4
        num = str(i.strip().split(' ', 1))          # "['forward', '4']"
        ic(num)
        ic(get_pos(i))
    # df = pd.Series(data=ini_list, dtype=np.int64, index=range(len(ini_list)))
