
from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution():

        """ Coin Sums

        In the United Kingdom the currency is made up of pound (£) and pence (p).
        There are eight coins in general circulation:

            1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

        It is possible to make £2 in the following way:

            1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

        How many different ways can £2 be made using any number of coins?
        """

        # === == === Solution === == ===  #

        # I could not for my life find the solution for this problem, maybe I gave up
        # too early, but here goes a solution by Beta Projects at:
        # https://betaprojects.com/solutions/project-euler/project-euler-problem-031-solution/

        target = 200  # 200p
        coins = (1, 2, 5, 10, 20, 50, 100, 200)

        # ways[1, 0, 0, 0, 0, 0, ... ]
        ways = [1] + [0]*target

        for coin in coins:
            for i in range(coin, target + 1):
                ways[i] += ways[i - coin]

        return ways[target]


Problem.solution()  # Result: 73682


