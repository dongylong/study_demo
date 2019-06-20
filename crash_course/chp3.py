# coding: utf-8
list = ["tom", "jerry", "cat", "dog"]
print (list)
print (list[0])
print (list[0].title())
print ("最后一列表元素: " + list[-1])

# 3.2.1 修改元素
motorcycles = ["honda", "yamaha", "suzuki", "subaru"]
print (motorcycles)
motorcycles.append("ducati")
print (motorcycles)
motorcycles.insert(0, "BMW")
print (motorcycles)
# 临时排序
print ("sorted: ", sorted(motorcycles))
print (motorcycles)
motorcycles.reverse()
# list 反转
print ("reverse()", motorcycles)
print ("len()", len(motorcycles))
# 永久排序
motorcycles.sort()
print (motorcycles)
del motorcycles[1]
print (motorcycles)
last_owned = motorcycles.pop()
motorcycle_popup_n = motorcycles.pop(1)
print (last_owned)
print (motorcycle_popup_n)
print (motorcycles)

motorcycles.remove("suzuki")
print (motorcycles)
