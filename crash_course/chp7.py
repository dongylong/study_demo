# coding: utf-8
msg = input("tell me sth :")
print("sth :", msg)
print(msg >= 14)
cur = 15
while cur < 30:
    print(cur)
    cur += 1
    if cur % 3 == 0:
        continue
    elif cur % 2 == 1:
        print(cur)

    elif cur == 20:
        break
    else:
        print("else")

unconfirmed_users = ['alice', 'tom', 'jerry']
if 'jerry' in unconfirmed_users:
    unconfirmed_users.remove('jerry')
print(unconfirmed_users)

confirm_users = []
while unconfirmed_users:
    user = unconfirmed_users.pop()
    if user == 'tom':
        continue
    confirm_users.append(user)
print(confirm_users)
