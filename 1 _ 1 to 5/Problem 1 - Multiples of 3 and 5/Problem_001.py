class problem_1(problem):
    
    def solution(number=1000):

    """Multiples of 3 and 5.
    If we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9.

    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    # === == === Solution === == ===  #

        sum = 0
        for i in range(number):
            if not(i % 3) or not(i % 5):
                sum += i

        return sum
