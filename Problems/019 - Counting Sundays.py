from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution():

        """ Counting Sundays
        You are given the following information, but you may prefer to do some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.

        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
        How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
        """

        # === == === Solution === == ===  #

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Jan 1 1901 was a Tuesday

        counter = 0
        day_value = 3  # Represents Tuesday

        for _ in range(1901, 2001):
            for i in range(len(months)):

                if _ % 4 == 0 and months[i] == 1:
                    day_value = (months[i] + 1 - (7 - day_value)) % 7
                else:
                    day_value = (months[i] - (7 - day_value)) % 7

                if day_value == 1:
                    counter += 1

        return counter


Problem.solution()  # Result: 171
