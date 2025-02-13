from decorators import time_it


def collatz_sequence(n):
    collatz = 1
    not_finished = True

    while not_finished:
        if n == 1:
            not_finished = False
        elif n % 2 == 0:  # Even
            n /= 2
        else:             # Odd
            n = 3*n + 1

        collatz += 1

    return collatz


class Problem:

    @time_it
    def solution(n=1_000_000):

        """ Longest Collatz sequence
        The following iterative sequence is defined for the set of positive integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

        Using the rule above and starting with 13, we generate the following sequence:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
        Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?

        NOTE: Once the chain starts the terms are allowed to go above one million.
        """

        # === == === Solution === == ===  #

        longest_collatz = 0
        longest_collatz_starting_number = None

        for i in range(1, n+1):
            current_collatz = collatz_sequence(i)
            if current_collatz > longest_collatz:
                longest_collatz = current_collatz
                longest_collatz_starting_number = i

        return longest_collatz, longest_collatz_starting_number


Problem.solution()  # Result: (526, 837799)
