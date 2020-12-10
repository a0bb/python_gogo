"""
1.数组的插入、删除、按照下标随机访问操作；
2.数组中的数据类型是Int
"""
from typing import Any


class Array:

    def __init__(self):
        self.__data = []

    def insert(self, index: int, value: Any) -> bool:
        self.__data.index(index, value)
        return True

    def delete_from_index(self, index: int) -> bool:
        if index > len(self.__data) or index < 0:
            return False
        self.__data.pop(index)
        return True

    def delete_from_value(self, value: Any) -> bool:
        self.__data.remove(value)
        return True

    def find(self, index: int) -> Any:
        if index > len(self.__data) or index < 0:
            return False

    def append(self, value: Any) -> bool:
        self.__data.append(value)
        return True

    def find_all(self) -> list:
        return self.__data
