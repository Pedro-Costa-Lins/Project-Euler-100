from decorators import time_it
import re

list_of_permutations = []


def Permutation(chars, size):
    # The original code was made by ankush_953 and cleaned up to by more pythonic by glubs9

    if size == 1:
        per = ''
        for i in chars:
            per = per + ''.join(str(i))
        list_of_permutations.append(per)
        return

    for i in range(size):
        Permutation(chars, size - 1)

        if size & 1:
            chars[0], chars[size - 1] = chars[size - 1], chars[0]
        else:
            chars[i], chars[size - 1] = chars[size - 1], chars[i]


def sorted_nicely(list_of_perms):
    # By Mark Byers on stackOverflow
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list_of_perms, key=alphanum_key)


class Problem:

    @staticmethod
    @time_it
    def solution(number=1_000_000):
        """ A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
        digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
        lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

        What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
        """

        # === == === Solution === == ===  #

        chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Permutation(chars, len(chars))

        return sorted_nicely(list_of_permutations)[number - 1]


Problem.solution()  # Result: 2783915460
