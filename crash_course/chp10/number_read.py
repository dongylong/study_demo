# coding: utf-8
import json

filename = 'xxx.txt'

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
