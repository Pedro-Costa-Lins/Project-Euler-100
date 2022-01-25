from decorators import log, time_it


class Test:

    @log
    @time_it
    def solution(number=1015):
        """ Attempt to fix this dumb code."""

        return number ** 50


Test.solution()
