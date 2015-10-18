# -*- coding: utf-8 -*-
# Tính độ dài của một mảng không sử dụng hàm len()

input_array = [1, 2, 3, 4, 5, 6, 7, 10, 12]

length = 0  # Store array's length

for element in input_array:
    length += 1

print "Input array: {}".format(input_array)
print "Length: {}".format(length)
