from decorators import time_it, log  # custom! :)


class Problem:

    @log
    @time_it
    def solution(self, number=None):

        """No specific docstring has been made.
        Calling without given arg will default
        to the original problem proposition."""

        pass

    def __init__(self):
        if __name__ == "__main__":
            print(self.solution())
