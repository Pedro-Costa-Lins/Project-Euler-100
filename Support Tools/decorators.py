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
        
            # Nice presentation.
            print(f'Result: {val}\nTime:   {time_taken} seconds.')
        
        except Exception:
            print(f'There was an error, invalid input given or ({func.__name__}) is not working.')
        except KeyboardInterrupt:
            print('WHY? Did you do something wrong again?')
        finally:
            print(f'\nEnd of {func.__name__}.')
        
        
    return wrapper
