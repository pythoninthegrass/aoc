#!/usr/bin/env python3

# import feather
# import numpy as np
import pandas as pd
import os
from pathlib import Path
from icecream import ic

# env
home = os.path.expandvars("$HOME")
cwd = Path(__file__).parent.absolute()
ic.configureOutput(includeContext=True)


def check_file(file):
    if not os.path.exists(file) or not os.path.getsize(file) > 0:
        print(f"File {file} does not exist or is empty")
        return True


def get_raw_data(file):
    with open(file, 'r') as f:
        return f.readlines()
    """
    with open(f"{cwd}/input.txt", "r") as f:
            lines = f.readlines()
            ini_list = np.array(lines)
            # ic("intial list: ", str(ini_list))
            ini_list = [int(i) for i in ini_list]   # convert to int
            print(ini_list)
    """


def get_formatted_data(file):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
        df = pd.read_csv(file)
        # print(df.to_string(index=False))
        return df


def write_formatted_data(data, file):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
        df = pd.DataFrame(data, columns=['energy', 'steps'])
        df.to_csv(file, index=False)
        # print(df.to_string(index=False))
        return df


# TODO: get x,y coordinates of octopi in 10x10 grid
class MoveItMoveIt:
    def __init__(self):
        self.pos = 0


        def move(self, steps):
            if steps:
                self.pos += steps
        return self.pos


    def get_pos(self):
        return self.pos


class BlazeIt:
    def __init__(self):
        self.energy = 0
        self.flash = 0


    def light_up(self, energy, flash):
        # First, the energy level of each octopus increases by 1
        energy += 1

        # any octopus with an energy level greater than 9 flashes
        if energy > 9:
            self.flash
            energy += 1

        # If this causes an octopus to have an energy level greater than 9, it also flashes
        if energy > 9:
            self.flash
            self.energy = 0

        return self.energy, self.flash


# Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?

pre =  """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

post = """
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637
"""

# TODO: commit; zip pre/post lines; calc diff; scale to 100 steps
raw_pre = [i.split() for i in pre]
raw_post = [i.split() for i in post]

if __name__ == "__main__":
    ic(pre)
    ic(raw_pre)
    ic(post)
    ic(raw_post)
    
    """
    raw_file = Path(cwd / "input.txt")
    formatted_file = Path(cwd / "input.csv")
    try:
        if check_file(formatted_file):
            raw_data = get_raw_data(raw_file)
            raw_data = [i.split() for i in raw_file]
            write_formatted_data(raw_data, formatted_file)
    
            df = get_formatted_data(formatted_file)
            ic(df)
        
            m = MoveItMoveIt()
            for item, row in df.iterrows():
                m.move(row['direction'], row['steps'])
        
            steps = m.get_pos()
    except FileNotFoundError:
        print(f"{formatted_file} not found. Exiting...")
    """
    