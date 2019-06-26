# coding: utf-8
filename = 'programming.txt'
#open(filename,'w')
# w r
# a 附加
# r+:读写
with open(filename,'w') as file_object:
    file_object.write("hello python\n")
    file_object.write("hello python again\n")