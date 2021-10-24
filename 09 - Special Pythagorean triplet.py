# A Pythagorean triplet is a set of three natural
# numbers, a < b < c, for which,

# a² + b² = c²

#For example, 3² + 4² = 9 + 16 = 25 = 5².

# There exists exactly one Pythagorean triplet for
# which a + b + c = 1000.

# Find the product abc. 
import math

def specialPythagorean(n):
    CList = []

    for i in range(2 ,n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                    CList.append(i)
                    CList.append(j)
                    CList.append(k)
                    CList.append('Sum: ')
                    CList.append(i + j + k)
                    CList.append('Product: ')
                    CList.append(i*j*k)

    return CList

print(specialPythagorean(1000))
