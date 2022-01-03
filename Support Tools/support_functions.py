from math import ceil, sqrt

def is_prime(number):
    
    for i in range(3, ceil(sqrt(number))):
        if not(n % i):
            return False
    
    return True
