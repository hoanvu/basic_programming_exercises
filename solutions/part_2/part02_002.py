# -*- coding: utf-8 -*-
# Đọc một file và dùng exception handling để in lỗi tương ứng nếu file đó không tồn tại


file_name = raw_input("Enter a file name (or path) to read: ")

print "File '{}' contents: \n".format(file_name)

try:
    with open(file_name, 'r') as f:
        print f.read()
except IOError:
    print "File '{}' does not exist!".format(file_name)
