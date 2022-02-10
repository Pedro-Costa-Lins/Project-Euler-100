from decorators import time_it


def sum_of_divisors(number):
    list_of_divisors = []
    for i in range(1, number//2 + 1):
        if number % i == 0:
            list_of_divisors.append(i)
    return sum(list_of_divisors)


def has_amicable(number):
    value = sum_of_divisors(number)
    if sum_of_divisors(value) == number and value != number:
        return value
    return False


class Problem:

    @time_it
    def solution(self, number=10_000):

        """Amicable numbers.
        Let d(n) be defined as the sum of proper divisors of n
        (numbers less than n which divide evenly into n).
        If d(a) = b and d(b) = a, where a ≠ b, then a and b are
        an amicable pair and each of a and b are called amicable numbers.

        For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
        20, 22, 44, 55 and 110; therefore d(220) = 284.
        The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

        Evaluate the sum of all the amicable numbers under 10000.
        """

        # === == === Solution === == ===  #

        list_of_amicable_numbers = []

        for number in range(1, 10_000):
            value = has_amicable(number=number)
            if value is not False and number not in list_of_amicable_numbers:
                list_of_amicable_numbers.append(value)
                list_of_amicable_numbers.append(number)

        return sum(list_of_amicable_numbers)


Problem.solution()
