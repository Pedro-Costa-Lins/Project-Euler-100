from decorators import time_it, log  # custom! :)


class Problem:

    def solution(number=None):

        """No specific docstring has been made.
        Calling without given arg will default
        to the original problem proposition."""

        pass

    @log
    @time_it
    def run(self):
        print(self.solution())

    def __init__(self):
        if __name__ == "__main__":
            self.run()



