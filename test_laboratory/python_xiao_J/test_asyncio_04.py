# -*- coding:utf-8 -*-
"""
@author: SHIHUA
@file: test_asyncio_04.py
@time: 2019/11/28 13:20
"""
import asyncio
import time


async def func01():
    print('func01 start...')
    await asyncio.sleep(2)
    print('func01 end...')


async def func02():
    print('func02 start...')
    await asyncio.sleep(3)
    print('func02 end ...')


async def main():
    task01 = asyncio.ensure_future(func01())
    task02 = asyncio.ensure_future(func02())
    await asyncio.gather(task01, task02, return_exceptions=True)


if __name__ == '__main__':
    s = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    e = time.time()

    print(f'during...{e - s}')