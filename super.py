from decorators import time_it, log  # custom! :)


class Problem:

    @log
    @time_it
    def solution(self, number):

        """No specific docstring has been made.
        Calling without given arg will default
        to the original problem proposition."""

        pass

    # def show_code(self):  # Not good, at least not this way.
    #
    #     """Fetches a file called 'plain_code.txt' present
    #     in the file of every problem, then displays it."""
    #
    #     with open('plain_code.txt', 'r') as f:
    #         print(f.read())

    def __init__(self):
        if __name__ == "__main__":
            print(self.solution())
