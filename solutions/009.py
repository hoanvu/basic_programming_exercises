# -*- coding: utf-8 -*-
# Kiểm tra chữ cái được nhập vào có phải là nguyên âm hay không
# Những chữ cái sau được gọi là nguyên âm: 'a', 'e', 'i', 'o', 'u'

# All vowels:
VOWELS = 'aeiuo'


def is_vowel(char):
    return True if char in VOWELS else False


if __name__ == '__main__':
    input_char = raw_input("Enter a character to check: ")

    if is_vowel(input_char):
        print "'{}' is a vowel.".format(input_char)
    else:
        print "'{}' is not a vowel.".format(input_char)
