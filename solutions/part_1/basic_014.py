# -*- coding: utf-8 -*-
# Kiểm tra xem một số có phải là số nguyên tố hay không
# Một số được gọi là số nguyên tố nếu nó chỉ chia hết cho 1 và chính nó
# Bài tập này sẽ sử dụng thư viện 'math' của Python để tính căn bậc 2

import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True

    return False


if __name__ == '__main__':
    number = int(raw_input('Enter a number: '))

    if is_prime(number):
        print "'{}' is a prime number.".format(number)
    else:
        print "'{}' is not a prime number.".format(number)
