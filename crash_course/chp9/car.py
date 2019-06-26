# coding: utf-8
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        info = str(self.year) + ' ' + self.make + ' ' + self.model + '\n odometer_reading：' + str(self.odometer_reading)
        print("info: " + info)

    def update_odometer(self, num):
        if num > self.odometer_reading:
            self.odometer_reading = num
        else:
            print('you cant roll back anb odometer')

    def increment_odometer(self, num):
        self.odometer_reading += num


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_descriptive_name(self):
        info = str(self.year) + ' ' + self.make + ' ' + self.model + '\n odometer_reading：' + str(
            self.odometer_reading) + '\n battery_size：' + str(self.battery_size)
        print("info: " + info)


my_car = Car('audi', 'a6', 2018)
my_car.get_descriptive_name()
my_car.update_odometer(23)
my_car.get_descriptive_name()
my_tesla = ElectricCar('tesla', 'model s', 2016, 70)
my_tesla.get_descriptive_name()
