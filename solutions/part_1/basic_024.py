# -*- coding: utf-8 -*-
# Tính độ dài của mỗi từ trong một chuỗi
# Kết quả trả về là một dict với mỗi cặp key/value là một từ
# với độ dài tương ứng của nó


def get_word_length(string):
    words = string.split(' ')
    word_length = {word: len(word) for word in words}

    return word_length


if __name__ == '__main__':
    string = raw_input("Enter a string: ")
    word_length = get_word_length(string)

    print "List of words and their length:"
    for word, length in word_length.items():
        print "     {} - {}".format(word, length)
