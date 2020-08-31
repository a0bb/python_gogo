
""" 从任意长度的可迭代对象中分解元素 """

case1 = ('2020-08-10', '192.168.0.177', 'log1', 'log2', 'log3')
date, ip, *logs = case1
print(f'case1 res -> {date}; {ip}; {logs}')

# 边界情况，没有log
case2 = ['2020-08-10', '192.168.0.88']
date, ip, *logs = case2
print(f'case2 res -> {date}; {ip}; {logs}')

# 使用split对截断字符串后再进行分解也是经常可以用到的技巧
case3 = '2020-08-10;192.168.0.177;log1;log2;log3'
date, ip, *logs = case3.split(';')
print(f'case3 res -> {date}; {ip}; {logs}')


# 举例：对学生成绩的列表去掉最低分与最高分，求平均值
# 从下例也可以看出，不需要的变量也可以使用‘_‘来占位
def avg_score(scores):
    _scores = sorted(scores, reverse=False)
    _, *score, _ = _scores
    return sum(*score) / len(score)


