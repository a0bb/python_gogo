# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-03-15 13:53

# 最后，再给你留一道思考题。既然你能通过继承一个类，来获得父类的函数和属性，那么你能继承两个吗？
# 答案自是能的，这就叫做多重继承。那么问题来了。我们使用单一继承的时候，构造函数的执行顺序很好确定，即子类 -> 父类 -> 爷类 ->… 的链式关系。
# 不过，多重继承的时候呢？比如下面这个例子。
# --->B - --
# A -    -->D
# --->C - --
# 这种继承方式，叫做菱形继承，BC 继承了 A，然后 D 继承了 BC，创造一个 D 的对象。
# 那么，构造函数调用顺序又是怎样的呢？


class A:
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

D()