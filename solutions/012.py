# -*- coding: utf-8 -*-
# Kiểm tra xem một chuỗi có phải là palindrome hay không
# Một chuỗi được gọi là palindrome nếu đọc ngược hoặc xuôi đều giống nhau.
# Ví dụ: 'radar', 'SOS', ...


def is_palindrome(string):
    reversed_string = ''.join(reversed(string))

    return True if reversed_string == string else False


if __name__ == '__main__':
    input_string = raw_input('Enter a string: ')

    if is_palindrome(input_string):
        print "'{}' is a palindrome.".format(input_string)
    else:
        print "'{}' is not a palindrome.".format(input_string)
