# coding: utf-8
motorcycles = ["honda", "yamaha", "suzuki", "subaru", "ducati", "BMW"]
for motorcycle in motorcycles:
    print(motorcycle + " is arriving")
    print(motorcycle + " stoped")
print(str(motorcycles) + " is arriving and stoped")
# 4.3 创建数字列表
digits = range(1, 15)
print digits
print (min(digits))
print (max(digits))
print (sum(digits))
# 从2 开始 每次加3，直至超过11 为止
xxx = range(2, 11, 3)
print xxx
print list(digits)
for digit in digits:
    print digit
# 4.3.4 列表解析
squares = [value ** 2 for value in range(1, 11)]
print (squares)
# 4.4 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players[0:3])
print (players[1:4])
print (players[:4])
print (players[-3:])
# 4.4.5 复制列表
my_players = players[:]
print (my_players)
#4.5 元祖
dimensions = (200,50)
print (dimensions[0])
dimensions = (400,500)
print (dimensions[0])