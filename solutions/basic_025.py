# -*- coding: utf-8 -*-
# Tính tần suất xuất hiện của mỗi chữ cái trong một chuỗi (không tính dấu cách)
# Kết quả trả về là một dict với mỗi cặp key/value là một chữ cái và
# tần suất xuất hiện của nó.


def get_char_frequency(string, character):
    '''Calculate the frequency of each character in a string'''
    count = 0
    for char in string:
        if char == character:
            count += 1

    return count


if __name__ == '__main__':
    string = raw_input("Enter a string: ")
    char_set = set(string)
    char_set = set([char for char in char_set if char != ' '])

    char_frequency = {char: get_char_frequency(string, char) for char in char_set}

    print "List of characters and their frequencies:"
    for char, frequency in char_frequency.items():
        print "     {} - {}".format(char, frequency)
