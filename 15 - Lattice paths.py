""" Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

# Thoughts:
After some pencil dance I found a correlation between Pascals Triangle and the amount of routes:
    1
  1 2 1        <- 1 x 1 Square, where 2, the biggest number, is the answer!
 1 3 3 1
1 4 6 4 1      <- 2 x 2 Square, where 6, the biggest number, is the answer!
... True for every number!
"""
import time
from math import factorial
import numpy as np

Start = time.process_time()


def pascal_triangle(n):
    n = n * 2
    pascals_notes = []

    for i in range(1, n + 2, 2):
        temporary_list = []
        c = 1

        for j in range(1, i + 1):
            # first value in a line is always 1
            temporary_list.append(c)

            # using Binomial Coefficient
            c = c * (i - j) // j

        temporary_list.sort()
        pascals_notes.append(temporary_list)

    return pascals_notes


Side = 20
PascalNotes = pascal_triangle(Side)

print(f'Result: The number of routes of a grid with the side of {Side} is: {PascalNotes[-1][-1]}')

print(f'Finished in {time.process_time() - Start} seconds')
