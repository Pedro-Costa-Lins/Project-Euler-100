#A palindromic number reads the same both ways. The largest palindrome made from the 
#product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
import math

def isPalindrome(number):
    digits = str(number)
    palin = True

    #Compares the first digit to the last, the second to the before last an so on.
    for i in range(1, math.floor( len( digits ) /2 ) + 1 ):
        if digits[-i] != digits[i-1]:
            #Declares 'Palin' = False if the number is not a Palindrome.
            palin = False
            break
    
    #Returns the 'palin' boolean.
    return palin

def biggestPalindromeUntil(number):
    nine = '9'
    until = ''
    Biggest = 1

    for i in range(number):
        until = until + nine
    ProductRange = int(until)

    for i in range(100, ProductRange):
        for j in range(i, ProductRange):
            if isPalindrome(i * j) and i * j > Biggest:
                Biggest = i * j
    
    return Biggest

print(biggestPalindromeUntil(3))

