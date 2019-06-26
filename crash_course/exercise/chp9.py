# coding: utf-8
from collections import OrderedDict
from random import randint


class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        i = 0
        while (i < 10):
            self.sides = randint(1, 6)
            print("i:" + str(i) + ' ' + ' random: ' + str(self.sides))
            i += 1;


my_die = Die()
my_die.roll_die()
#
# # 9.1
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def open_restaurant(self):
#         print("Restaurant is opening")
#
#     def describe_restaurant(self):
#         info = "restaurant_name:" + self.restaurant_name + "\n cuisine_type: " + self.cuisine_type + "\n number_served: " + str(
#             self.number_served)
#         print("info :" + info)
#
#     def set_number_served(self, num):
#         self.number_served = num
#         print("number_served :" + str(self.number_served))
#
#     def increment_number_served(self, num):
#         self.number_served += num
#         self.describe_restaurant
#
#
# # 9.2
# my_restaurant = Restaurant("quick", "fast")
# my_restaurant.open_restaurant()
# my_restaurant.describe_restaurant()
# # 9.4
# my_restaurant.set_number_served(5)
# my_restaurant.describe_restaurant()
#
#
# # 9.3
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(
#             "first_name:" + self.first_name + "\n last_name:" + self.last_name + "\nlogin_attempts" + str(
#                 self.login_attempts))
#
#     def greet_user(self):
#         print("hello ! " + self.first_name + " " + self.last_name)
#
#     def increment_login_attempts(self, num):
#         self.login_attempts += num
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# my_user = User("paul", "Gorge")
# my_user.describe_user()
# my_user.greet_user()
# my_user.first_name = "cris"
# my_user.describe_user()
# my_user.greet_user()
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = [
#             'can add post',
#             'can delete post',
#             'can ban user',
#         ]
#
#     def show_privileges(self):
#         print("privilege:" + str(self.privileges))
#
#
# admin = Admin('ad', 'ministrator')
# admin.show_privileges()
