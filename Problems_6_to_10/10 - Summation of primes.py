from super import Problem


def is_prime(number):
    from math import ceil, sqrt

    for i in range(3, ceil(sqrt(number))):
        if not (number % i):
            return False

    return True


def bar_initial(size):
    """Sends the first two rows of the progress visualizer."""

    print('\n\n|------------------------PROGRESS-------------------------|\n\
               |---------------------------------------------------------|\n', end='')

    return size // 60


class Problem010(Problem):

    def solution(self, number=2_000_000):
        """ Summation of primes
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        Find the sum of all the primes below two million.
        """

        # === == === Solution === == ===  #

        part = starting_part = bar_initial(number)
        flip = True
        i = 1
        total = 4
        
        while i < number:
            
            # Creates progress lines
            if i > part:
                part = part + starting_part
                print('|', end='')
            
            if flip:
                if is_prime(i):
                    total = total + i
                flip = False
                i = i + 4
            else:
                if is_prime(i):
                    total = total + i
                flip = True
                i = i + 2

        return total
