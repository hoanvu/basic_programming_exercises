# -*- coding: utf-8 -*-
# Tính số dòng, số từ và chữ cái trong một file
# (không tính dấu cách và dòng trống) sử dụng exception handling

lowercases = "abcdefghijklmnopqrstuvwxyzáàảãạòóỏõọèéẻẽẹùúủũụừứửữựờớởỡợồốổỗộềễệếể"

number_of_lines = 0
number_of_words = 0
number_of_chars = 0

file_name = raw_input("Enter a file name: ")

try:
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()

            if line:
                # Đếm dòng
                number_of_lines += 1

                # Đếm từ
                number_of_words += len([word for word in line.split(' ')])

                # Đếm chữ cái
                number_of_chars += len([char for char in list(line) if char.lower() in lowercases])
except IOError:
    print "File '{}' doest not exist!".format(file_name)
else:
    print "Number of lines: {}".format(number_of_lines)
    print "Number of words: {}".format(number_of_words)
    print "Number of chars: {}".format(number_of_chars)
