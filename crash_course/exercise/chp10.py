# coding: utf-8


# 10-11
import json

filename = '/Users/dongyl/PycharmProjects/study_demo/remember_me.json'


def save_number(num):
    with open(filename, 'w') as j_file:
        json.dump(num, j_file)
        print("num saved")


def get_number(num):
    # try:
    #
    # except :
    #     print("error")
    # else:
    with open(filename) as j_file:
        nums = json.load(j_file)
        print("num saved", str(nums))
        if num == nums:
            print("hello again")
        else:
            save_number(num)
get_number(123)