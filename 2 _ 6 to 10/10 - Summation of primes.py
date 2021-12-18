""" Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import numpy as np


class n_prime:

    def __init__(self, number):
        self.number = number
        self.Sum: np.intc = 4
        self.primes_sum()

        
    def __str__(self):
        return self.results()

    
    def is_prime(self, n):
        '''Verifies for primes, returns a boolean.'''

        for i in range(3, int(np.floor(np.sqrt(n))) + 1, 2):
            if n % i == 0:
                return False
        return True
         
        
    def primes_sum(self):
        """Sums all the primes. Starts the visual representation."""
        
        startingPart = self.bar_incial()
        part = startingPart
        flip = True
        i = 1
        
        while i < self.number:
            
            # Creates progess lines
            if i > part:
                Part = Part + StartingPart
                print('|', end='')
            
            if flip:
                if self.is_prime(i):
                    self.Sum = self.Sum + i
                flip = False
                i = i + 4
            else:
                if self.is_prime(i):
                    self.Sum = self.Sum + i
                flip = True
                i = i + 2

        return True

    
    def bar_incial(self):
        """Sends the first two rows of the progress visualizer."""

        print('\n\n|------------------------PROGRESS-------------------------|\n\
                   |---------------------------------------------------------|\n', end='')
        
        return np.ceil(self.number / 60)
    
    
    def results(self):
        return f'\nFinished. Result: {self.Sum}\n\n'


Number = 2000000
print(n_prime(Number))