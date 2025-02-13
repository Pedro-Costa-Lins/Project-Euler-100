from decorators import time_it

def check_abundant(number):
    list_of_divisors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            list_of_divisors.append(i)
    if sum(list_of_divisors) > number:
        return True
    else:
        return False


def list_abundants(target_limit):
    list_of_abundants = []
    for i in range(1, target_limit):
        if check_abundant(i):
            list_of_abundants.append(i)
    print(f'size of list_of_abundants: {list_of_abundants.__sizeof__()}')
    return list_of_abundants


def list_all_sums_of_bundants(list_of_abundants):
    list_of_all_sums_of_bundants = []
    for i in list_of_abundants:
        for j in list_of_abundants:
            list_of_all_sums_of_bundants.append(i+j)

    return [*set(list_of_all_sums_of_bundants)]

def compare_lists(list_of_abundants, target_limit):
    list_of_all_the_positive_integers_which_cannot_be_written_as_the_sum_of_two_abundant_numbers = []
    list_of_all_sums_of_bundants = list_all_sums_of_bundants(list_of_abundants)
    for i in range(1, target_limit):
        if i not in list_of_all_sums_of_bundants:
            list_of_all_the_positive_integers_which_cannot_be_written_as_the_sum_of_two_abundant_numbers.append(i)
    return list_of_all_the_positive_integers_which_cannot_be_written_as_the_sum_of_two_abundant_numbers


class Problem:

    @time_it
    def solution(self):

        """ A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
        For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is
        a perfect number.

        A number n is called deficient if the sum of its proper divisors is less than and it is called abundant if this
        sum exceeds n.

        As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
        sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than
        28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further
        by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
        numbers is less than this limit.

        Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

        # === == === Solution === == ===  #

        target_limit = 28123
        list_of_abundants = list_abundants(target_limit)
        return sum(compare_lists(list_of_abundants, target_limit))


Problem.solution()  # Result: 4179871
