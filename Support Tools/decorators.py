def time_it(func):
    import time

    def wrapper(*args, **kwargs):
        print(f'Start of {func.__name__}.')
        print(f'Description:\n\t{func.__doc__}', end='\n\n')
        
        # Will only time the function itself, hopefully.
        before = time.time()
        try:
            val = func(*args, **kwargs)
            
        except Exception:
            val = f'Error in ({func.__name__}) or invalid input.'
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
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
        except Exception:
            val = f'Error in {func.__name__} or invalid input.'
        except KeyboardInterrupt:
            val = 'User interrupted.'
        finally:
            logging.info(f'Ran with args: {args}, and kwargs: {kwrags}')
            return val
    
    return wrapper
