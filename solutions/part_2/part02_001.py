# -*- coding: utf-8 -*-
# Đọc một file và in nội dung ra màn hình


file_name = raw_input("Input file name (or path to file) to read: ")
print "File {}'s content: \n".format(file_name)

with open(file_name, 'r') as f:
    print f.read()
