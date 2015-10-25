# -*- coding: utf-8 -*-
# In biểu đồ: nhập một mảng bất kì và in ra biểu đồ hàng ngang
# với mỗi hàng có độ dài tương ứng với một phần tử của mảng.
# VD: với mảng nhập vào như sau: [9, 2, 5], thì chương trình sẽ phải in ra như sau:
#   *********
#   **
#   *****


def histogram(array):
    histo = ""
    for number in array:
        histo += '*' * number
        histo += '\n'

    return histo


if __name__ == '__main__':
    input_array = [23, 3, 10, 15, 2, 20, 15]
    print "Input array: {}".format(input_array)
    print "Histogram:"
    print histogram(input_array)
