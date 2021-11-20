""" Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

20, 19, 18, 17, 16, 15, 14, 13, 12, 11 <- only numbers to worry about

# Thoughts:
    Should be even (Throught iterations of an even number it is resolved)
    Should finish with 20, 40, 60, 80 or 00 (Throught iterations of 20 it is resolved)
"""
def is_multiple(n, numbers):

    #If the 'n' is not multiple, it's ruled out.
    for j in range(numbers[0], numbers[1]): 
        if n % j != 0:
            return False
    return True


def small_multiple(numbers):
    notFound = True
    notOne = False
    iteration = 20
    n = 20
    
    while notFound:
        if is_multiple(n, numbers):
            notFound = False
        n = n + iteration
    
    return n
    
    
print(small_multiple(numbers=[11, 20]))
