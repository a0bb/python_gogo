"""
这种继承方式，叫做菱形继承，BC 继承了 A，然后 D 继承了 BC，创造一个 D 的对象。那么，构造函数调用顺序又是怎样的呢？
"""


class A():
    def __init__(self):
        print('enter A')
        print('lever A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('lever B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('lever C')



class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('lever D')


D()


