from decorators import time_it
from useful import is_prime_brute_force as is_prime


def iterate_through_possibilities(target):
    big_a = 0
    big_b = 0
    most_primes_found = 0
    product_of_coefficients_with_max_n_of_primes = 0
    for a in range(-target+1, target):
        print(f'Testing a={a} -', end=' ')
        for b in range(-target, target+1):
            print(f'b={b}', end='|')
            ended_search = False
            n = 0
            while not ended_search:
                if not is_prime(n**2 + a*n + b):
                    ended_search = True
                else:
                    n += 1
            if most_primes_found < n:
                most_primes_found = n
                product_of_coefficients_with_max_n_of_primes = a * b
                big_a = a
                big_b = b
        print('\n')

    return f'product_of_coefficients_with_max_n_of_primes (a * b) = {product_of_coefficients_with_max_n_of_primes}, ' \
           f'most primes found (n) = {most_primes_found}, big a = {big_a}, big b = {big_b}'


class Problem:

    @staticmethod
    @time_it
    def solution():

        """Euler discovered the remarkable quadratic formula:

        n² + n + 41

        It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
        However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41,
        41² + 41 + 41 is clearly divisible by 41.

        The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive
        values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479.

        Considering quadratics of the form:

        n² + an + b, where |a| < 1000 and |b| <= 1000

        where |n| is the modulus/absolute value of n
        e.g. |11| = 11 and |-4| = 4

        Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
        number of primes for consecutive values of n, starting with n=0.
        """

        # === == === Solution === == ===  #

        target = 1000
        return iterate_through_possibilities(target)


Problem.solution()
# Result : product_of_coefficients_with_max_n_of_primes (a * b) = -59231,
# most primes found (n) = 62, big a = -61, big b = 971
