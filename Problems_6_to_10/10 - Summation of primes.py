from super import Problem


def is_prime(number):
    from math import ceil, sqrt

    for i in range(3, ceil(sqrt(number))):
        if not (number % i):
            return False

    return True


class Problem010(Problem):

    def solution(self, number=2_000_000):
        """ Summation of primes
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        Find the sum of all the primes below two million.
        """

        # # Thoughts:
        #
        #     After 2, all subsequent primes are odd, only half of the numbers
        #     need to be tested.
        #     Also they're not multiple of 3, so 1/3 of the odds won't be tested.
        #     Neither ends with 5, isPrime method is verifying if it ends with 5.
        #     There is a possibility to skip multiples of 7, but seems to
        #     be getting complicated, for now only the other skips will be used.
        #     9 is being taken by removing multiples of 3.

        # === == === Solution === == ===  #

        flip = True
        i = 1
        total = 4
        
        while i < number:

            if flip:
                if is_prime(i):
                    total += i
                flip = False
                i += 4
            else:
                if is_prime(i):
                    total += i
                flip = True
                i += 2

        return total
