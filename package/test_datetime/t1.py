import time
from datetime import datetime, timedelta


case1 = datetime.now()
print(f'case1: {case1, type(case1)}')
print(f'case1-1: {case1.year, case1.month, case1.day}')

case2 = datetime.now().strftime('%Y%m%d%H%M%S%f')
# strftime格式符 -> https://www.cnblogs.com/fwl8888/p/9635505.html
print(f'case2: {case2, type(case2)}')

case3 = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(f'case3: {case3, type(case3)}')

case4 = datetime.utcnow()
print(f'case4: {case4}')

case5 = datetime.fromtimestamp(1607615027)
print(f'case5: {case5}')

case6 = case1 + timedelta(days=1)
# 该函数表示两个时间的间隔
# case1为datetime类型
print(f'type(timedelta(days=1))-> {type(timedelta(days=1))}')
print(f'case6: {case6}')

print('*' * 100)


# 字符串时间转时间戳
def time2stamp(t):
    time_array = time.strptime(t, '%Y-%m-%d %H:%M:%S')
    print(type(time_array), time_array)
    timestamp = time.mktime(time_array)
    return timestamp


# 当前时间转时间戳
def get_now_stamp():
    now_time = datetime.now()
    return time.mktime(now_time.timetuple())


# 时间戳转时间
def stamp2time(timestamp):
    return datetime.fromtimestamp(timestamp)


if __name__ == '__main__':
    print(time2stamp('2020-12-10 23:34:30'))
    print(get_now_stamp())
    print(stamp2time(1607614470))
