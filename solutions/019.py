# -*- coding: utf-8 -*-
# Chuyển các chữ cái đầu tiên của mỗi từ trong một chuỗi thành chữ in hoa
# Tất cả các chữ cái còn lại của mỗi từ chuyển sang chữ thường.


def convert(string):
    words = string.split(' ')
    new_words = [word[0].upper() + word[1:].lower() for word in words]

    return ' '.join(new_words)


if __name__ == '__main__':
    input_string = raw_input('Enter some string: ')

    print convert(input_string)
