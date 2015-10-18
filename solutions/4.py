# -*- coding: utf-8 -*-
# Đảo ngược một mảng

# Cũng như bài tập số 3, có nhiều cách để đảo ngược một mảng,
# nhưng cách giải sẽ tập trung sử dụng vòng lặp

input_array = [1, 2, "orange", 4, "apple", 6, -1.3]
output_array = []

print "Input array: {}".format(input_array)

# Tiếp tục cho tới khi nào input_array vẫn còn item
while len(input_array) > 0:
    # Thêm item cuối cùng của input_array vào output_array
    output_array.append(input_array[-1])
    # Xóa item cuối cùng khỏi input_array
    input_array = input_array[:-1]


print "Reversed array: {}".format(output_array)
