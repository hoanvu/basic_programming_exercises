# -*- coding: utf-8 -*-
# Cắt bớt một chuỗi nếu chuỗi lớn hơn một độ dài bất kì do người dùng nhập


def slice(string, length):
    # Nếu số nguyên được nhập lớn hơn độ dài của chuỗi, trả về chuỗi đó
    if length > len(string):
        return string
    else:
        index = 0   # luôn cắt từ kí tự đầu tiên của chuỗi
        slice_string = ""
        while index < length:
            slice_string += string[index]
            index += 1

        return slice_string


if __name__ == "__main__":
    input_string = raw_input("Input a string: ")
    length = int(raw_input("Input the length to slice: "))

    print slice(input_string, length)
