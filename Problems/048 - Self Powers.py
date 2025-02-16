from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution(number=1000):

        """ Self Powers
        The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

        Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
        """

        # === == === Solution === == ===  #

        bigArray = []

        for i in range(1, 1 + int(number)):
            bigArray.append(i ** i)
    
        return str(sum(bigArray))[-10:]


Problem.solution() # Result: 9110846700
