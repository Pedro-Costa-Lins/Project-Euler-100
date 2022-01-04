def is_prime(number):
    from math import ceil, sqrt

    for i in range(3, ceil(sqrt(number))):
        if not(number % i):
            return False
    
    return True

