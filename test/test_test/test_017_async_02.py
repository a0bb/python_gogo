# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-04-06 20:51
import asyncio
import time


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    s = time.time()
    print('before await')
    task1 = asyncio.ensure_future(worker_1())
    print('awaited worker_1')
    task2 = asyncio.ensure_future(worker_2())
    print('awaited worker_2')
    await asyncio.gather(task1, task2)
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()