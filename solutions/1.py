# -*- coding: utf-8 -*-
# Tính độ dài của một chuỗi không sử dụng hàm len()

input_string = raw_input("Enter any string: ")

length = 0  # Store string's length

for char in input_string:
    length += 1

print "String '{0}' has {1} characters.".format(input_string, length)
