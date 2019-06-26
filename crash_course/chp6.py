# coding: utf-8
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['color'] = 'yellow'
print(alien_0['color'])
print(alien_0)
del alien_0['color']
print(alien_0)
user = {
    'name': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user.items():
    print("key: " + key, " value: " + value)

for key in user.keys():
    print("key: " + key)
print("----------------")
for key in sorted(user.keys()):
    print("key: " + key)
