# -*- coding: utf-8 -*-
# Tính giai thừa
# n! = n * (n - 1) * (n - 2) * ...


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(raw_input("Input an integer: "))
    print "Factorial of '{}' is: {}".format(number, factorial(number))
