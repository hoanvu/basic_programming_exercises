# -*- coding: utf-8 -*-
# Sinh chuỗi Fibonacci


def fibonacci(number):
    # Initialize chuỗi Fibonacci với 2 phần tử đầu tiên
    fib = [1, 1]
    index = 3

    # Chuỗi Fibonacci với 1 phần tử
    if number == 1:
        return fib[:1]
    # Chuỗi Fibonacci với 2 phần tử
    elif number == 2:
        return fib
    else:
        while index <= number:
            # Số tiếp theo là tổng của 2 số đứng liền sau nó
            fib.append(fib[-1] + fib[-2])
            index += 1

    return fib


if __name__ == "__main__":
    number = int(raw_input("Input a number to generate fibonacci: "))
    print "Chuỗi Fibonacci: {}".format(fibonacci(number))
