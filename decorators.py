from functools import wraps


def time_it(func):
    import time

    @wraps(func)
    def wrapper():
        print(f'Start of {func.__name__}.')
        print(f'Description:\n\t{func.__doc__}', end='\n\n')
        
        # Will only time the function itself, hopefully.
        before = time.time()
        try:
            val = func()

        except KeyboardInterrupt:
            val = 'User interrupted.'

        finally:
            time_taken = time.time() - before
            
            # Nice presentation.
            print(f'Result: {val}\nTime:   {time_taken} seconds.')
            print(f'\nEnd of ({func.__name__}) function.')
                
    return wrapper


def log(func):
    import logging

    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)
    
    @wraps(func)
    def wrapper():
        try:
            val = func()

        except KeyboardInterrupt:
            val = 'User interrupted.'

        finally:
            logging.info(f'{func.__name__} was executed.')

        return val
    
    return wrapper
