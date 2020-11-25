import re


re1 = r'^[a-z0-9_-]{3,15}$'
s1 = 'john_doe'
s2 = 'jo'
p1 = re.findall(re1, s1)
p2 = re.findall(re1, s2)
print(f're1: {p1}\n{p2}')


re2 = r'the'
s1 = 'The fat cat sat on the mat.'
p1 = re.findall(re2, s1)
print(f're2: {p1}')

# . 点运算符
re3 = r'.ar'
s1 = 'The car parked in the garage.'
p1 = re.findall(re1, s1)
print(f're3: {p1}')

# [] 字符集
re4 = r'[Tt]he'
s1 = 'The car parked in the garage.'
p1 = re.findall(re4, s1)
print(f're4: {p1}')

re5 = r'ar[.!]'
s1 = 'A garage is a good place to park a car. your car!'
p1 = re.findall(re5, s1)
print(f're5: {p1}')
# 否定字符集
re6 = r'[^c]ar'
s1 = 'The car parked in the garage.'
p1 = re.findall(re6, s1)
print(f're6: {p1}')

# 重复次数 *
# 所有以小写字母开头的字符串
re7 = r'[a-z]*'
s1 = 'The car parked in the garage #21.'
p1 = re.findall(re7, s1)
print(f're7: {p1}')

re8 = r'\s*cat*\s'
s1 = 'The fat cat sat on the concatenation.'
p1 = re.findall(re8, s1)
print(f're8: {p1}')


# 重复次数 +
re9 = r'c.+t'
s1 = 'The fat cat sat on the mat.'
p1 = re.findall(re9, s1)
print(f're9: {p1}')

re10 = r'[T]?he'
s1 = 'The car is parked in the garage.'
p1 = re.findall(re10, s1)
print(f're10: {p1}')


# {}
re11 = r'[0-9]{2,3}'
s1 = 'The number was 9.9997 but we rounded it off to 10.0.'
p1 = re.findall(re11, s1)
print(f're11: {p1}')

re12 = r'[0-9]{2,}'
s1 = 'The number was 9.9997 but we rounded it off to 10.0.'
p1 = re.findall(re12, s1)
print(f're12: {p1}')

re13 = r'[0-9]{3}'
s1 = 'The number was 9.9997 but we rounded it off to 10.0.'
p1 = re.findall(re13, s1)
print(f're13: {p1}')


# (...)特征标群
# TODO 怎么精准匹配所有的匹配项
re14 = r'(c|p|g)ar'
s1 = 'The car is parked in the garage.'
p1 = re.findall(re14, s1)
p2 = re.search(re14, s1).group()
print(f're14: {p1}\n{p2}')


# | 运算符  TODO
re15 = r'(T|t)he|car'
s1 = 'The car is parked in the garage.'
p1 = re.findall(re15, s1)
print(f're15: {p1}')


# 转码特殊字符 \

# 锚点 ^
# TODO
re16 = r'^(T|t)he'
s1 = 'The car is parked in the garage.'
p1 = re.search(re16, s1).group()
print(f're16: {p1}')




