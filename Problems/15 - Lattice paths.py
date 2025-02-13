from decorators import time_it


class Problem:

    @time_it
    def solution(n=20):

        """ Lattice paths
        Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
        there are exactly 6 routes to the bottom right corner.

        How many such routes are there through a 20×20 grid?
        """

        # === == === Solution === == ===  #

        paths = 1

        for i in range(n):
            paths *= (2 * n) - i
            paths /= i + 1

        return int(paths)


Problem.solution()  # Result: 137846528820
