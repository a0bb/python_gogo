# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-04-06 15:05
import time


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))

##################
import multiprocessing
import time


def cpu_bound_01(number):
    print(sum(i * i for i in range(number)))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound_01, numbers)


def main_01():
    numbers = [10000000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")


if __name__ == '__main__':
    # main()
    print('-' * 100)

    main_01()

