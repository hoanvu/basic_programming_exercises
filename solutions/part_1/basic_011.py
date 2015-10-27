# -*- coding: utf-8 -*-
# Tìm tất cả các số trong một mảng lớn hơn 'n'


def is_bigger(number, limit):
    return True if number > limit else False


if __name__ == '__main__':
    input_array = [3, 32, -90, 434.2, 10, 12345, 66, -96.3]
    print "Input array: {}".format(input_array)

    limit = float(raw_input("Input a limit: "))
    output_array = []

    for number in input_array:
        if is_bigger(number, limit):
            output_array.append(number)

    print "All numbers bigger than {} are: {}".format(limit, output_array)
