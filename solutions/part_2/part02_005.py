# -*- coding: utf-8 -*-
# Yêu cầu user nhập vào 2 số và tính tổng của chúng
# Dùng exception handling để kiểm tra người dùng nhập vào có phải số hay không


try:
    number1 = float(raw_input("Input first number: "))
    number2 = float(raw_input("Input second number: "))
    print "Sum: {}".format(number1 + number2)
except ValueError:
    print "You didn't enter a number!"
