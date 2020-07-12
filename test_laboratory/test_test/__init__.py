# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: test_test 14:44

import hashlib

s = hashlib.sha1('sdddddd'.encode('utf-8')).hexdigest()
print(s)