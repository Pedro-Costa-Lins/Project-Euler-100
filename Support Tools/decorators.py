import time


def time_it(func):
    def wrapper(*args, **kwargs):
        print(f'Start of {func.__name__}.')
        print(f'Description:\n\t{func.__doc__}', end='\n\n')
        
        # Will only time the function itself, hopefully.
        try:
            before = time.time()
            val = func(*args, **kwargs)
            time_taken = time.time() - before
        except Exception:
            return 'There is a problem'
        
        # Nice presentation.
        print(f'Result: {val}\nTime:   {time_taken} seconds.')
        
        
        print(f'\nEnd of {func.__name__}.')
        
    return wrapper



from math import sqrt, ceil


@time_it
def balagunga(number):
    
    """Verify if it is a prime number."""
    
    for i in range(3, ceil(sqrt(number))):
        if number%i == 0:
            return False
    return True
        

# 218315467
balagunga()
