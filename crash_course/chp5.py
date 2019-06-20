# coding: utf-8
#cars = []
cars = ['audi', 'bwm', 'honda', 'subaru', 'toyota']
age = 11
if cars:
    for car in cars:
        if car == 'bwm' and age >= 1:
            print (car.upper())
        else:
            print (car.title())
else:
    print ("cars empty")
print ("--------------")
for car in cars:
    if car != 'bwm' or age == 1:
        print (car.upper())
    else:
        print (car.title())
if 'bwm' in cars:
    print ('bwm in cars')
else:
    print ('bwm not in cars')
if 'bwm' not in cars:
    print ('bwm in cars')
else:
    print ('bwm not in cars')

can_edit = False
game_active = True

if age == 1:
    print ("if")
elif age == 2:
    print ("elif")
else:
    print ("else")
