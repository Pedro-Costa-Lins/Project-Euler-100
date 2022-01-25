from decorators import time_it, log  # custom! :)


class Problem:

    def solution(number=None):
        print('super here')

    @log
    @time_it
    def run(self):
        print(self.solution())

    def __init__(self):
        self.run(self)



