def multiplesOf3and5(number):
    Sum = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            Sum = Sum + i

    return Sum

print(multiplesOf3and5(10))
