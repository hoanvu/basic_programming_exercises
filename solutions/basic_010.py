# -*- coding: utf-8 -*-
# Tìm tất cả các từ trong một chuỗi có độ dài lớn hơn 'n'


# Return True if length of the given word is bigger than the
# given length, otherwise return False.
def is_longer(word, length):
    return True if len(word) > length else False


if __name__ == '__main__':
    input_string = raw_input("Enter a string: ")
    length = int(raw_input("Enter a length: "))

    words = input_string.split(' ')
    word_list = [word for word in words if is_longer(word, length)]

    print "All words have more than {} characters: {}".format(length, word_list)
