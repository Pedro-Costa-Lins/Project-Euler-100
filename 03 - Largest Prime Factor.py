""" Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import numpy as np


def largestPrimeFactor(number):

    
    # Verifies for primes, returns a boolean.
    def is_Prime(n):
        
        #Starts with an odd number and skips all even.
        for i in range(3, int(np.floor(np.sqrt(n))) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    # If the number is a factor and is Prime, it is the biggest.
    for i in range(3, number, 2):
        if number % i == 0 and is_Prime(number / i):
            return number / i


number = 600851475143
print(largestPrimeFactor(number))
