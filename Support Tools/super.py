from datetime.datetime import date
from decorators import time_it, log

class problem:

def __init__(self):
    solution_date = date(2021, 20, 10)

@log
@time_it
def solution():
    pass


def show_code():
    with open('plain_code.txt', 'r') as f:
        print(f.read())