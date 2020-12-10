import time
from datetime import datetime, timedelta


case1 = datetime.now()
print(f'case1: {case1}')
print(f'case1-1: {case1.year, case1.month, case1.day}')

case2 = datetime.now().strftime('%Y%m%d%H%M%S%f')
print(f'case2: {case2}')

case3 = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'case3: {case3}')

case4 = datetime.utcnow()
print(f'case4: {case4}')

case5 = datetime.fromtimestamp(1607615027)
print(f'case5: {case5}')

case6 = timedelta()
print(f'case6: {case6}')


# 字符串时间转时间戳
t = '2020-12-10 23:34:30'
time_array = time.strptime(t, '%Y-%m-%d %H:%M:%S')
print(time_array)
timestamp = time.mktime(time_array)
print(timestamp)

# 当前时间转时间戳
now_time = datetime.now()
print(type(now_time), now_time)
print(time.mktime(now_time.timetuple()))

# 时间戳转时间
timestamp = 1607614470
print(datetime.fromtimestamp(timestamp))

