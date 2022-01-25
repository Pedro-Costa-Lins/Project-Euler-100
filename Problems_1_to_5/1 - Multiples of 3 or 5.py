from super import Problem


class Problem001(Problem):

    def solution(self, number=1000):

        """Multiples of 3 and 5.
        If we list all the natural numbers below 10 that are
        multiples of 3 or 5, we get 3, 5, 6 and 9.

        The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000.
        """

        # === == === Solution === == ===  #

        final_sum = 0
        for i in range(3, number):
            if not(i % 3) or not(i % 5):
                final_sum += i

        return final_sum
