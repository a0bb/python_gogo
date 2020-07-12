# -*- coding:utf-8 -*-
"""
@author: SHIHUA
@file: test_threading.py
@time: 2019/11/27 11:46
"""

import concurrent.futures
import requests
import time
import random


def download_one(url):
    with requests.get(url) as r:
    #     with open('./{}.pdf'.format(random.randint(1,10)), 'wb') as fp:
    #         fp.write(r.content)
        print('Read {} from {}'.format(len(r.content), url))


def download_all(sites):
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, sites)


def main():
    sites = [
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/f9f44cd90957/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606275',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/39d0491e5dcb/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606167',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/112eb8606525/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606243',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/b3064a255ef8/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606244',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/cb1c9c15897c/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606245',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/3f3bb86a3b3f/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606243',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/69b3fe76c1e2/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606245',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/41f59342f601/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/3a7eccdf1d14/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/03f003aa2208/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606247',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/c56a84319d3d/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/2b6e3c9c650e/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606247',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/230782db509b/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606247',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/e4df4815c53b/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606246',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/ce621868a695/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/31ce8fb1c7ba/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/13d1cd342f49/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/010ade1d4fb5/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606249',
        'https://doc-static.ai.fltrp.com/sigma/collection/err_exercise/f0a0914623/98f460db4fb6/Test%20for%20EIM%20Level%201%20Unit%206%EF%BC%88%E5%B8%88%E5%A4%A7%E9%99%84%E5%A4%96%20%E5%88%9D%E4%BA%8C%E5%B9%B4%E7%BA%A7%EF%BC%89%E9%94%99%E9%A2%98%E6%9C%AC.pdf?timestamp=1570606248'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
