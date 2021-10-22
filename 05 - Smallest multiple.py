#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#20, 19, 18, 17, 16, 15, 14, 13, 12, 11 <- only numbers to worry about

## Requiriments ##
# (Throught iterations of an even number it is resolved) Should be even
# (Throught iterations of 20 it is resolved) Should finish with 20, 40, 60, 80 or 00


def smallMultiple():
    NotFound  = True
    Iteration = 20
    NotOne    = False
    i = 0

    while NotFound:
        NotOne = False
        i = i + Iteration
        for j in range(11, 20): #If the number 'i' is not multiple of any number, it's ruled out. 
            if i % j != 0:
                NotOne = True
                break
        if NotOne:
            continue
        else:
            return i #Since it is in ascending order, the first found is the smallest.

print(smallMultiple())