""" Largest Palindrome
A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math


def isPalindrome(number):
    
    digits = str(number)

    #Compares the first digit to the last, the second to the before last an so on.
    for i in range(1, math.floor( len( digits ) /2 ) + 1 ):
        if digits[-i] != digits[i-1]:
            return False

    return True


def biggest_palindrome_with_n_digits(number):
    
    #Setting of the range expected.
    nine = 0.99999999999999 
    ProductRange = int(math.ceil(nine * 10 ** number))
    
    Biggest = 1

    for i in range(int(ProductRange / 10), ProductRange):
        for j in range(i, ProductRange):
            if isPalindrome(i*j) and i*j > Biggest:
                Biggest = i*j

    return Biggest

print(biggest_palindrome_with_n_digits(3))
