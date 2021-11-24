""" 18 / 67 - Maximum path sum I & II.py
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
(Triangle excluded from here, now using the triangle from problem 67 from the site)

Problems links: https://projecteuler.net/problem=18 || https://projecteuler.net/problem=67
"""

import numpy as np
import urllib

file = urllib.request.urlopen('https://projecteuler.net/project/resources/p067_triangle.txt')

TriangleStr = [i.decode('utf-8').split() for i in file]

Triangle = [[int(i) for i in j] for j in TriangleStr]


def below_maximum_sum(triangle):
  for line in reversed(range(len(triangle)-1)):
    for item in range(len(triangle[line])):
      if (triangle[line][item] + triangle[line+1][item]) >= (triangle[line][item] + triangle[line+1][item+1]):
        triangle[line][item] = triangle[line][item] + triangle[line+1][item]
      else:
        triangle[line][item] = triangle[line][item] + triangle[line+1][item+1]
  
  return triangle[0][0]

below_maximum_sum(triangle=Triangle)
