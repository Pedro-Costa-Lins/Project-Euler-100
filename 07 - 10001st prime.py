# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10001st prime number?

## Notes ##

# After 2, all subsequent primes are odd, only half of the numbers
# need to be tested.

# Also they're not multiple of 3, so 1/3 of the odds won't be tested.

# Neither ends with 5, isPrime method is verifying if it ends with 5.

# There is a possibility to skip multiples of 9 and 7, but seems to
# be getting complicated, for now, only the other skips will be used.
# 9 is being taken by removing multiples of 3. 7 is dumb.

import numpy as np

def nPrime(number):
    
    def is_Prime(n):
        '''Verifies for primes, returns a boolean.'''

        for i in range(3, int( np.floor( np.sqrt(n) ) ) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    Counter = 1
    Flip = True
    i = 1

    while Counter < number:
        if Flip:
            
            if is_Prime(i):
                Counter = Counter + 1
                if Counter == 10001:
                    return i
            
            Flip = False
            i = i + 4
        else:
            
            if is_Prime(i):
                Counter = Counter + 1
                if Counter == 10001:
                    return i

            Flip = True
            i = i + 2
    return i

print(nPrime(10001))
