import re
from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution():

        """Names scores
        Using names.txt (right click and 'Save Link/Target As...'),
        a 46K text file containing over five-thousand first names,
        begin by sorting it into alphabetical order.
        Then working out the alphabetical value for each name,
        multiply this value by its alphabetical position in the
        list to obtain a name score.

        For example, when the list is sorted into alphabetical order,
        COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
        name in the list. So, COLIN would obtain a score of 938 × 53
        = 49714.

        What is the total of all the name scores in the file?
        """

        # === == === Solution === == ===  #

        # in order to sort, first find and separate.
        pattern = r'([a-zA-Z]+)'
        with open('names.txt', 'r') as file:
            name_list = re.findall(pattern, file.read())

        names = list(name_list)

        return "In progress, not finished by this dumbass!"


Problem.solution()
