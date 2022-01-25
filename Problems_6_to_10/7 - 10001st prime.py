from super import Problem


def is_prime(number):
    from math import ceil, sqrt

    for i in range(3, ceil(sqrt(number))):
        if not (number % i):
            return False

    return True


class Problem007(Problem):

    def solution(self, number=10001):

        """ 10001st prime
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

        What is the 10001st prime number?
        """

        # # Thoughts:
        #
        #     After 2, all subsequent primes are odd, only half of the numbers need to be tested.
        #     Also they're not multiple of 3, so 1/3 of the odds won't be tested.
        #     Neither ends with 5, isPrime method is verifying if it ends with 5.
        #     There is a possibility to skip multiples of 9 and 7, but seems to be getting complicated, for now,
        #     only the other skips will be used.
        #     9 is being taken by removing multiples of 3. 7 is dumb.

        counter = 1
        flip = True
        i = 1

        while counter < number:
            if flip:
                if is_prime(i):
                    counter = counter + 1
                flip = False
                i = i + 4

            elif is_prime(i):
                counter = counter + 1
                flip = True
                i = i + 2

        return i