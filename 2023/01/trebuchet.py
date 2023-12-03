#!/usr/bin/env python

import re
from pathlib import Path

fn = Path("input.txt")
data = fn.read_text().splitlines()

# extract all digits from the input by line
digits = [re.findall(r"\d+", line) for line in data]

# convert all digits to integers
ints = [list(map(int, line)) for line in digits]

# concatenate list of integers
cats = [int(str(line[0]) + str(line[-1])) for line in ints]

# iterate over concatenated integers and concatenate first and last digit of each integer
more_cats = []
for i in range(len(cats)):
    cats[i] = int(str(cats[i])[0] + str(cats[i])[-1])
    more_cats.append(cats[i])

# [print(i) for i in more_cats]

# print sum of all integers in more_cats
print(sum(more_cats))
