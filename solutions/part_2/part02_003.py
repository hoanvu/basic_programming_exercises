# -*- coding: utf-8 -*-
# Tính số dòng, số từ và chữ cái trong một file, không tính dấu cách và dòng trống
# Lưu ý là nếu bạn đếm các chữ cái trong file có kí tự như tiếng việt có dấu, kết quả trả
# về có thể sẽ hơi khác do Python phân tích kí tự đặc biệt hay có dấu thành nhiều kí tự khác nhau

number_of_lines = 0
number_of_words = 0
number_of_chars = 0

lowercases = 'abcdefghijklmnopqrstuvwxyzáàảãạòóỏõọèéẻẽẹùúủũụừứửữựờớởỡợồốổỗộềễệếể'

file_name = raw_input("Input a file name: ")
with open(file_name, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()

        if line:
            # Đếm dòng
            number_of_lines += 1

            # Đếm từ
            number_of_words += len(line.split(' '))

            # Đếm chữ cái
            number_of_chars += len(
                [char for char in list(line) if char.lower() in lowercases])

print number_of_lines
print number_of_words
print number_of_chars
