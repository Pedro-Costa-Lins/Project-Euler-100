'''
The sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is .

3025 - 385 = 2640

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
'''

def sumSquareDifference(n):
    SumSqr = 0
    SqrSum = 0
    
    for i in range(1, n + 1):
        SumSqr = SumSqr + (i ** 2)
        SqrSum = SqrSum + i
    
    SqrSum = SqrSum ** 2
    
    return SqrSum - SumSqr

print(sumSquareDifference(100))
