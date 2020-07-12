# -*- coding:utf-8 -*-
#
# @author: shihua
# 
# @time: 2020-04-06 20:20
import time


# def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))
#
#
# def main(urls):
#     for url in urls:
#         crawl_page(url)
#
#
# if __name__ == '__main__':
#     main(['url_1', 'url_2', 'url_3', 'url_4'])

import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.ensure_future(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    m = main(['url_1', 'url_2', 'url_3', 'url_4'])

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(m)
    finally:
        loop.close()