""" Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import numpy as np

SumOf = str(2**1000)

SumList = np.array([int(SumOf[i]) for i in range(len(SumOf))])

print(f'Result: The sum of the digits made by 2^1000: {np.sum(SumList)}.')
