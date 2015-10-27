# -*- coding: utf-8 -*-
# Tìm số lớn nhất và nhỏ nhất trong mảng

# Python có hỗ trợ hàm max() và min() cho phép chúng ta tìm số
# lớn nhất và nhỏ nhất tương ứng của một mảng. Tuy nhiên do mục đích là
# học và nắm các cấu trúc cơ bản nên chúng ta sẽ không dùng hai hàm này.


def max(numbers):
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number

    return max


def min(numbers):
    min = numbers[0]
    for number in numbers:
        if min > number:
            min = number

    return min


if __name__ == '__main__':
    input_array = [123, 32, 2, -12.5, 9, 999, -4032, 321]

    print "Input array: {}".format(input_array)
    print "Biggest number: {}".format(max(input_array))
    print "Smallest number: {}".format(min(input_array))
