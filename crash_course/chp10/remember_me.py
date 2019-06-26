# coding: utf-8
import json

filename = '/Users/dongyl/PycharmProjects/study_demo/remember_me.json'


def get_stored_username():
    try:
        with open(filename) as j_obj:
            names = json.load(j_obj)
    except FileNotFoundError:
        print("FileNotFoundError")
        return None
    else:
        print(names)
        return names


def greet_user(name):
    names = get_stored_username()
    if name in names:
        print("hello " + names + ", i remember you ")
    else:
        write_name(name)


def write_name(name):
    with open(filename, 'r+') as j_obj:
        json.dump(name, j_obj)
        print("hello " + name + ", i remember you next time")


my_name = "aa"
greet_user(my_name)
# write_name(my_name)
# print(name)
