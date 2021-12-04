""" Number letter counts
If the numbers 1 - 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.

For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.
"""
import numpy as np


def last_digit_name(last_digit):
    dictionary = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    return dictionary[last_digit]


def before_last_is_1(last_digit):
    dictionary = {
        0: 'ten',
        1: 'eleven',
        2: 'twelve',
        3: 'thirteen',
        4: 'fourteen',
        5: 'fifteen',
        6: 'sixteen',
        7: 'seventeen',
        8: 'eighteen',
        9: 'nineteen'
    }
    return dictionary[last_digit]


def before_last_is_2_or_bigger(before_last_digit):
    dictionary = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }
    return dictionary[before_last_digit]


def size_is_3_or_bigger(hundred_house_digit, something_after=False):
    dictionary = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    additional = 'hundred'
    if something_after:
        additional = additional + 'and'

    return dictionary[hundred_house_digit] + additional


def number_name_giver(number):
    give_back = []

    for _ in reversed(range(len(str(number)))):
        if len(str(number)) == 0:
            break

        elif len(str(number)) == 1 and number == 0:
            break

        elif len(str(number)) == 1:
            give_back.append(last_digit_name(last_digit=number))
            break

        elif len(str(number)) == 2 and int(str(number)[0]) == 0:
            number = int(str(number)[1])

        elif len(str(number)) == 2 and int(str(number)[0]) == 1:
            give_back.append(before_last_is_1(last_digit=int(str(number)[1])))
            break

        elif len(str(number)) == 2 and int(str(number)[0]) >= 2:
            give_back.append(before_last_is_2_or_bigger(before_last_digit=int(str(number)[0])))
            if str(number)[-1] == '0':
                break
            number = int(str(number)[1])

        elif len(str(number)) == 3:
            after = True
            if number % 100 == 0:
                after = False

            give_back.append(size_is_3_or_bigger(hundred_house_digit=int(str(number)[0]), something_after=after))
            number = int(str(number)[1:])

        elif len(str(number)) == 4:
            give_back.append('onethousand')
            number = int(str(number)[1:])

    return give_back


def iterator_and_accounting_until(number):
    final_list = []
    for i in range(1, number+1):
        final_list = final_list + number_name_giver(i)

    return len(''.join(final_list))


Number = 1000
print(iterator_and_accounting_until(number=Number))
