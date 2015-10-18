# -*- coding: utf-8 -*-
# Tìm từ dài nhất (một hoặc nhiều) trong một chuỗi

input_string = raw_input("Input a string: ")
words = {}      # 'words' là 1 dict, có key là từ và value là độ dài của từ đó
longest_words = []  # mảng kết quả, chứa những từ dài nhất
longest = 0     # chứa độ dài của từ dài nhất trong chuỗi

# Tách input_string thành một mảng gồm các từ
word_list = input_string.split()

# Với mỗi từ trong input_string, làm 2 việc:
# 1. thêm một cặp key/value vào words (key là từ đó, value là độ dài)
# 2. kiểm tra độ dài của mỗi từ và lưu vào biến 'longest' để lấy độ dài lớn nhất
for word in word_list:
    word_length = len(word)
    words[word] = word_length
    if longest < word_length:
        longest = word_length

# Kiểm tra tất cả các từ và chỉ lấy những từ dài nhất, có độ dài bằng 'longest'
for word in words:
    if words[word] == longest:
        longest_words.append(word)

# Vòng lặp for thứ 2 có thể được viết lại bằng một dòng
# sử dụng list comprehension như bên dưới. Tuy nhiên, với
# mục đích hướng dẫn cho các bạn mới bắt đầu, mình viết một
# vòng lặp for thông thường để dễ hiểu.

# longest_words = [word for word in words if words[word] == longest]

print "Longest words: {}".format(longest_words)
