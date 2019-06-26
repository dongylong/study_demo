# coding: utf-8
try:
    div = 5 / 3
    print(div)
except ZeroDivisionError:
    # print("can not divide by zero")
    pass
else:
    print("div:" + str(div))
