def is_prime(number):
    from math import ceil, sqrt

    for i in range(3, ceil(sqrt(number))):
        if not(n % i):
            return False
    
    return True

