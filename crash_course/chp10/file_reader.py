# coding: utf-8
filename = '/Users/dongyl/PycharmProjects/study_demo/remember_me.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())
