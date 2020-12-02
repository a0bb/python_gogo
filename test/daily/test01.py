
print(bool == int)
print(isinstance(True, int))
print(isinstance(False, int))

print('*' * 100)

my_list = [1, 0, -1, True, False, None, 'str']

for item in my_list:
    if isinstance(item, int):
        print(item)

print('*' * 100)

# current
for item in my_list:
    if not isinstance(item, bool) and isinstance(item, int):
        print(item)

