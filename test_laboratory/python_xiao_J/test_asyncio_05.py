import asyncio
import aiohttp
import time


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(urls):
    # task 合并之心
    tasks = [asyncio.ensure_future(download(site)) for site in urls]
    await asyncio.gather(*tasks)
    # 循环await
    # for url in urls:
    #     await download(url)


def main():
    urls = [
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif',
        'http://sigma-stable-img.oss-cn-shanghai.aliyuncs.com/founder_dev/%E5%8F%B3%E8%BE%B9%E6%A0%8F.tif'
    ]
    start = time.time()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(download_all(urls))
    finally:
        loop.close()
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
