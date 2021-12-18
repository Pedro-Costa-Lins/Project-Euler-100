""" Special Pythagorean
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which:

a + b + c = 1000.

Find the product abc. 
"""


def special_pythagorean(n):
    
    for i in range(2, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i+j+k == 1000 and i**2 + j**2 == k**2:
                    
                    return f'Numbers: {i} {j} and {k}. Sum: {i+j+k}. Product: {i*j*k}.'

    return f'Not found matches for {n}.'

Number = 1000
print(special_pythagorean(Number))
