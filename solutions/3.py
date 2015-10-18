# -*- coding: utf-8 -*-
# Đảo ngược một chuỗi

# Bài tập này có vài cách giải, nhưng mình sẽ sử dụng vòng lặp for.
# Một số cách giải như bên dưới ('a' là chuỗi):
#       a[::-1]
#       "".join(reversed(a))

input_string = raw_input("Input a string: ")
output_string = ""

while len(input_string) > 0:
    output_string += input_string[-1]
    input_string = input_string[:-1]

print "Reversed string is: '{}'".format(output_string)
