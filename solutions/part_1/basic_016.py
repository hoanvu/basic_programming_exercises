# -*- coding: utf-8 -*-
# Tìm tất cả các nhân tử chung của hai mảng


def find_common(a, b):
    common = []
    for element in a:
        if element in b:
            common.append(element)

    return common


if __name__ == '__main__':
    a = [1, 2, 3, 4, 6, 12, 32, 111, -3]
    b = [-3, -4, 5, 6, 32, 321, 222]

    print "First array: {}".format(a)
    print "Second array: {}".format(b)

    print "Elements in both arrays: {}".format(find_common(a, b))
