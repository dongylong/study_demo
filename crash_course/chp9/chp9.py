# coding: utf-8
from crash_course.chp9.car import Car,ElectricCar


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print (self.name.title() + " is now sitting.")

    def roll_over(self):
        print (self.name.title() + " rolled over!")


my_dog = Dog("wililie", 6)
print ("my_dog:" + str(my_dog))
print ("my_dog's name :" + my_dog.name)
print ("my_dog's age :" + str(my_dog.age))
my_dog.sit()
my_dog.roll_over()
my_car=Car('audi','Q7',2018)
my_car.get_descriptive_name()
my_el_car=ElectricCar('audi','Q7',2018,80)
my_el_car.get_descriptive_name()