# -*- coding: utf-8 -*-
# In hoa một chuỗi không dùng hàm upper()


UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LETTERS = dict(zip(list(LOWERCASE_LETTERS), list(UPPERCASE_LETTERS)))

input_string = raw_input("Enter a string: ")
output_string = ""

for char in input_string:
    if char in LOWERCASE_LETTERS:
        output_string += LETTERS[char]
    else:
        output_string += char

print "Uppercase string: {}".format(output_string)
