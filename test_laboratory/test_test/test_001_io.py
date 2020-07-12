# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: test_test 14:45

"""
1、读取文件 in.txt；
2、去除所有标点符号和换行符，
3、并把所有大写变成小写；
4、合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
5、将结果按行输出到文件 out.txt。
"""
import re


def parse(text):
    # 使用正则表达式去符号和换行符
    text = re.sub(r'[^\w ]', ' ', text)

    # 转为小写
    text = text.lower()

    # 生成所有单词的列表
    word_list = ' '.join(text)

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频字典
    word_num = {}
    for w in word_list:
        if w not in word_num:
            word_num[w] = 0
        word_num[w] += 1

    # 按照词频排序
    word_sorted = sorted(word_num.items(), key=lambda x: x[1], reverse=True)

    # 返回
    return word_sorted


# word_num = {
#     'i': 3,
#     'love': 4,
#     'you': 5
# }
# print(type(word_num.items()))