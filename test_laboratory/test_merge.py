# -* -coding:utf-8 -*-
# @Time: 2020-06-22 22:55
# @Author: ShiHua
# @file: test_merge.py


def merge(obj, other, *args):
    if not args:
        if not isinstance(other, dict) or not isinstance(obj, dict):
            return other
        res = {}
        for k in obj.keys() | other.keys():
            if k not in obj:
                res[k] = other[k]
            elif k not in other:
                res[k] = obj[k]
            else:
                res[k] = merge(obj[k], other[k])
        return res

    res = merge(obj, other)
    for arg in args:
        res = merge(res, arg)
    return res
