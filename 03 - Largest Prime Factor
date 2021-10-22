import math

def largestPrimeFactor(number):
    factors = []
    Largest = None
    Prime   = True

    #- This part will try to find the factors by dividing the given number to an iteration
    # and appending the result in a list. This list will be created in decreasing order.
    for i in range(3, 100000000):
        if number % i == 0:
            factors.append(int(number/i))

    #- Test to find the first prime number, and it will by the order of the biggest prime.
    for i in factors:
        Prime = True
        for j in range(2, int(i)):
            if i % j == 0:
                Prime = False
                break
    #- Ends the code imediatly returning the biggest prime factor
        if Prime:
            return i
    #- Since the code wont test for '2' and '1', '2' will be the default answer or '1' if odd.
    if int(str(number)[-1]) % 2 == 0:
        return 2
    else:
        return 1

print(largestPrimeFactor(3));
