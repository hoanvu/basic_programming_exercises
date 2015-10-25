# -*- coding: utf-8 -*-
# Tìm tất cả ước số của một số nguyên bất kì


def find_divisors(number):
    divisors = []
    divisors.append(1)  # 1 is the divisor of all numbers
    count = 2

    while count < number - 1:
        if number % count == 0:
            divisors.append(count)

        count += 1

    divisors.append(number)  # each number is the divisor of itself

    return divisors


if __name__ == '__main__':
    number = int(raw_input("Enter a number: "))
    print "All divisors of {} are: {}".format(number, find_divisors(number))
