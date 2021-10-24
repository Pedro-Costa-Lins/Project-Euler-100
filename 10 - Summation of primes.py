# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Notes:
# A little better this time using class and functions.

import math

class nPrime:

    def __init__(self, number):
        self.number = number
        self.Sum = 4
        self.fill_List()

    def __str__(self):
        return self.bar_final()

    def is_Prime(self, n):
        for i in range(3, int(math.floor(math.sqrt(n))) + 1, 2):
            if n % i == 0:
                return False
        return True
              
    def fill_List(self):
        StartingPart = self.bar_incial()
        Part = StartingPart
        Flip = True
        i = 1
        while i < self.number:
            if i > Part:
                Part = Part + StartingPart
                print('|', end='')
            if Flip:
                if self.is_Prime(i):
                    self.Sum = self.Sum + i
                Flip = False
                i = i + 4
            else:
                if self.is_Prime(i):
                    self.Sum = self.Sum + i
                Flip = True
                i = i + 2
        return True

    def bar_incial(self):
        print('\n\n|------------------------PROGRESS-------------------------|\n|---------------------------------------------------------|\n', end='')
        return math.ceil(self.number / 60)
        
    def bar_final(self):
        return f'\nFinished. Result: {self.Sum}\n\n'

Prime = nPrime(2000000)

print(Prime)
