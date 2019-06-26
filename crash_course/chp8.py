# coding: utf-8
import pizza
import pizza as p
# from pizza import make_pizza

# 不建议
# from pizza import *
# pizza.make_pizza
# p.make_pizza()
# make_pizza()


def user_car():
    print("hello user,car")


def user_car(user_name='admin', car_name='audi'):
    print("hello1 user_name:" + user_name + " car_name: " + car_name)
    return user_name + " drive " + car_name


# def user_car(user_name, car_name):
#     print ("hello2 user_name:" + user_name + " car_name: " + car_name)


# user_car(user_name='jim')
xx = user_car(user_name='jim', car_name='bmw')
print(xx)
x = user_car('jim')
print(x)


def get_formatted_name():
    print("hello user,car")


# def get_formatted_name(first_name, last_name):
#     return first_name + "  " + last_name


def get_formatted_name(first_name, last_name, middle_name=''):
    return first_name + "  " + middle_name + " " + last_name


# def user_car(user_name, car_name):
#     print ("hello2 user_name:" + user_name + " car_name: " + car_name)


# user_car(user_name='jim')
xx = get_formatted_name('jim', 'paul')
print(xx)
x = get_formatted_name('jim', 'carter', 'paul')
print(x)
