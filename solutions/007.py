# -*- coding: utf-8 -*-
# Tính tổng, tích và trung bình của các số trong một mảng


def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


def average(numbers):
    total = sum(numbers)

    return float(total) / len(numbers)


def multiply(numbers):
    mul = 1
    for number in numbers:
        mul *= number

    return mul


if __name__ == '__main__':
    input_array = [3, 231, 123, -65, .56, -6.43]

    print "Input array: {}".format(input_array)
    print "Sum: {}".format(sum(input_array))
    print "Average: {}".format(round(average(input_array), 3))
    print "Multiply: {}".format(multiply(input_array))
