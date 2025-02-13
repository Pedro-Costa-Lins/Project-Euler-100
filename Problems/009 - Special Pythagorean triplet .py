from decorators import time_it


class Problem:

    @time_it
    def solution(number=1000):

        """ Special Pythagorean
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

        a² + b² = c²

        For example, 3² + 4² = 9 + 16 = 25 = 5².

        There exists exactly one Pythagorean triplet for which:

        a + b + c = 1000.

        Find the product abc.
        """

        # === == === Solution === == ===  #

        for i in range(2, number):
            for j in range(i+1, number):
                for k in range(j+1, number):
                    if i+j+k == 1000 and i**2 + j**2 == k**2:

                        return f'Numbers: {i} {j} and {k}. Sum: {i+j+k}.'\
                               f' Product: {i*j*k}.'

        return f'Not found matches for {number}.'


Problem.solution()  # Result: Numbers: 200 375 and 425. Sum: 1000. Product: 31875000.
