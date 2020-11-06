# -*- coding:utf-8 -*-
"""
@author: SHIHUA
@file: test_async_cancel.py
@time: 2019/11/28 10:17
"""
import asyncio


async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    # Create a "cancel_me" Task
    task = asyncio.ensure_future(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(10)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()