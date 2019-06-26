# coding: utf-8
import json

filename = 'xxx.txt'

numbers = [2, 3, 5, 9, 11, 65]
with open(filename, 'r+') as f_obj:
    json.dump(numbers, f_obj)
