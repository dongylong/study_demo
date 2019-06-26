# coding: utf-8
from crash_course.chp9.car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_descriptive_name(self):
        info = str(self.year) + ' ' + self.make + ' ' + self.model + '\n odometer_reading：' + str(
            self.odometer_reading) + '\n battery_size：' + str(self.battery_size)
        print("info: " + info)

my_tesla = ElectricCar('tesla', 'model s', 2016, 70)
my_tesla.get_descriptive_name()
