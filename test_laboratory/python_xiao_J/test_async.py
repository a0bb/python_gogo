# -*- coding:utf-8 -*-
"""
@author: SHIHUA
@file: test_async.py
@time: 2019/11/26 19:00
"""
import asyncio
import aiohttp  ### 1
import time
import random


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print('Read {} from {}'.format(res.content_length, url))
            # async with open('./{}.pdf'.format(random.randint(0, 9)), 'wb') as fp:
            #     fp.write(res.content)


async def download_all(sites):
    tasks = [asyncio.ensure_future(download_one(site)) for site in sites]
    await asyncio.sleep(3)
    await asyncio.gather(*tasks)


def main():
    sites = [
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/f9f44cd90957/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606275',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/39d0491e5dcb/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606167',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/112eb8606525/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606243',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/b3064a255ef8/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606244',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/cb1c9c15897c/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606245',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/3f3bb86a3b3f/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606243',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/69b3fe76c1e2/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606245',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/41f59342f601/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/3a7eccdf1d14/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/03f003aa2208/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606247',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/c56a84319d3d/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/2b6e3c9c650e/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606247',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/230782db509b/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606247',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/e4df4815c53b/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/ce621868a695/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/31ce8fb1c7ba/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/13d1cd342f49/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/010ade1d4fb5/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'http://doc-static2.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/98f460db4fb6/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606248'
    ]
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(download_all(sites))
    finally:
        loop.close()

    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()