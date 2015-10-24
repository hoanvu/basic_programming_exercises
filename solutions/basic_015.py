# -*- coding: utf-8 -*-
# Tìm số nguyên tố thứ n với n là do người dùng nhập

from basic_014 import is_prime  # use function already in basic_014.py


# Generator to get all prime numbers
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


# Get prime number at position 'n'
def get_nth_prime(n):
    count = 0

    for prime in get_primes(2):
        count += 1

        if count == n:
            return prime


if __name__ == '__main__':
    number = int(raw_input("Enter an integer number: "))
    print "{}th prime number is '{}'".format(number, get_nth_prime(number))
