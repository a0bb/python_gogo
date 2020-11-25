# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-01-29 17:28

import ujson


params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('../../geekbang/output_file/io_out.json', 'w') as fp:
    out_str = ujson.dump(params, fp)
print(f'{type(out_str)}\n{out_str}')

with open('../../geekbang/output_file/io_out.json', 'r') as fp:
    in_dct = ujson.load(fp)
print(f'{type(in_dct)}\n{in_dct}')