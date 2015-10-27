# -*- coding: utf-8 -*-
# Tìm tất cả ước số chung của 2 số nguyên bất kì

from basic_017 import find_divisors
from basic_016 import find_common


def find_common_divisors(number1, number2):
    # Tìm tất cả ước số của 'number1' và 'number2'
    divisors_number1 = find_divisors(number1)
    divisors_number2 = find_divisors(number2)

    # Tìm tất cả nhân tử chung giữa 2 mảng ở trên i.e. ước số chung
    return find_common(divisors_number1, divisors_number2)


if __name__ == '__main__':
    number1 = int(raw_input("Enter number1: "))
    number2 = int(raw_input("Enter number2: "))

    print "All common divisors of {} and {} are: {}".format(
        number1,
        number2,
        find_common_divisors(number1, number2))
