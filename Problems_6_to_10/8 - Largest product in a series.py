from super import Problem

Number = '7316717653133062491922511967442657474235534919493496983520312774\
          5063262395783180169848018694788518438586156078911294949545950173\
          7958331952853208805511125406987471585238630507156932909632952274\
          4304355766896648950445244523161731856403098711121722383113622298\
          9342338030813533627661428280644448664523874930358907296290491560\
          4407723907138105158593079608667017242712188399879790879227492190\
          1699720888093776657273330010533678812202354218097512545405947522\
          4352584907711670556013604839586446706324415722155397536978179778\
          4617406495514929086256932197846862248283972241375657056057490261\
          4079729686524145351004748216637048440319989000889524345065854122\
          7588666881164271714799244429282308634656748139191231628245861786\
          6458359124566529476545682848912883142607690042242190226710556263\
          2111110937054421750694165896040807198403850962455444362981230987\
          8799272442849091888458015616609791913387549920052406368991256071\
          7606058861164671094050775410022569831552000559357297257163626956\
          1882670428252483600823257530420752963450'


class Problem008(Problem):

    def solution(self, adjacent=13, number=Number):
        """ Largest product in a series
        The four adjacent digits in the 1000-digit number that have the
        greatest product are:

         9 × 9 × 8 × 9 = 5832.

        Find the thirteen adjacent digits in the 1000-digit number that
        have the greatest product. What is the value of this product?
        """

        # Thoughts:
        #   Fun fact: '69' is the biggest sequence of adjacent numbers that the
        #   product isn't 0.
        #   'print(largestProduct(69))' gives:
        #   2412446685431734624320887406251212800000000.

        # === == === Solution === == ===  #

        product = 1
        biggest_product = 0

        for i in range(len(number) - adjacent):
            product = 1

            for j in range(adjacent):
                product = product * int(number[i+j])

            if product > biggest_product:
                biggest_product = product

        return biggest_product

