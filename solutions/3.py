# -*- coding: utf-8 -*-
# Đảo ngược một chuỗi

# Bài tập này có vài cách giải, nhưng mình sẽ sử dụng vòng lặp for.
# Một số cách giải như bên dưới ('a' là chuỗi):
#       a[::-1]
#       "".join(reversed(a))

input_string = raw_input("Input a string: ")
output_string = ""

# Tiếp tục cho tới khi nào input_string không còn kí tự nào
while len(input_string) > 0:
    # Thêm kí tự cuối cùng của input_string vào output_string
    output_string += input_string[-1]
    # Xóa kí tự cuối cùng trong input_string
    input_string = input_string[:-1]

print "Reversed string is: '{}'".format(output_string)
