# -*- coding:utf-8 -*-
"""
@author: SHIHUA
@file: test_async_02.py
@time: 2019/11/28 08:49
"""

import asyncio
import random


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(2):
        await queue.put(i)
        print('{} put a val: {}'.format(id, i))
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()

    consumer_1 = asyncio.ensure_future(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.ensure_future(consumer(queue, 'consumer_2'))

    producer_1 = asyncio.ensure_future(producer(queue, 'producer_1'))
    producer_2 = asyncio.ensure_future(producer(queue, 'producer_2'))

    await asyncio.sleep(2)
    consumer_1.cancel()
    consumer_2.cancel()

    print(await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True))

if __name__ == '__main__':
    import time
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    end = time.time()
    print('during:{}'.format(end - start))
