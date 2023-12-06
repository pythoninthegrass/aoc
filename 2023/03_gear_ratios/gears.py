#!/usr/bin/env python

import re
from pathlib import Path

fn = Path("input.txt")
lines = fn.read_text().splitlines()


def part_one():
    matches = []

    # iterate over the lines
    for i in range(len(lines)):
        # Find all occurrences of integers
        for match in re.finditer(r'\d+', lines[i]):
            # Get the start and end position of the match
            start, end = match.span()
            # Get the corresponding characters in the same line, the line above, and the line below
            chars_same = lines[i][max(0, start - 1):min(len(lines[i]), end + 1)]
            chars_above = lines[i - 1][max(0, start - 1):min(len(lines[i - 1]), end + 1)] if i > 0 else ''
            chars_below = lines[i + 1][max(0, start - 1):min(len(lines[i + 1]), end + 1)] if i < len(lines) - 1 else ''
            # If any of the characters is a special character that isn't a dot, print the matched integer
            if any(char not in '.0123456789' for char in chars_same + chars_above + chars_below):
                matches.append(int(match.group()))

    return sum(matches)


if __name__ == '__main__':
    print(part_one())
