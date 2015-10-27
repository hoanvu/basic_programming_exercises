# -*- coding: utf-8 -*-
# Kiếm tra xem một chuỗi có phải là một pangram hay không
# Một chuỗi được gọi là một pangram nếu nó chứa tất cả chữ cái trong bảng chữ cái


def is_pangram(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for character in alphabets:
        if character not in string.lower():
            return False
    return True


if __name__ == '__main__':
    string = raw_input("Enter a string: ")
    if is_pangram(string):
        print "Input string is a pangram!"
    else:
        print "Input string is not a pangram!"
