import requests
import asyncio
import aiohttp
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent
import random
from pyquery import PyQuery as pq
import re

def get_page(url, options={}):
    ua = UserAgent()
    base_headers = {
        'User-Agent':  ua.random,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    headers = dict(base_headers, **options)
    print('Getting', url)
    try:
        r = requests.get(url, headers=headers)
        print('Getting result', url, r.status_code)
        if r.status_code == 200:
            return r.text
    except ConnectionError:
        print('Crawling Failed', url)
        return None

def crawl_ip181():
    start_url = 'http://www.ip181.com/'
    html = get_page(start_url)
    ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    # \s* 匹配空格，起到换行作用
    re_ip_adress = ip_adress.findall(html)
    for adress,port in re_ip_adress:
        result = adress + ':' + port
        # yield result.replace(' ', '')
        print(result.replace(' ', ''))
crawl_ip181()
# crawl_daili66()
# def crawl_data5u():
#     for i in ['gngn', 'gnpt']:
#         start_url = 'http://www.data5u.com/free/{}/index.shtml'.format(i)
#         html = get_page(start_url)
#         ip_adress = re.compile(
#                             ' <ul class="l2">\s*<span><li>(.*?)</li></span>\s*<span style="width: 100px;"><li class=".*">(.*?)</li></span>'
#             )
#         # \s * 匹配空格，起到换行作用
#         re_ip_adress = ip_adress.findall(html)
#         for adress, port in re_ip_adress:
#             result = adress + ':' + port
#             yield result.replace(' ', '')
            # print(result.replace(' ', ''))

# for aq in crawl_data5u():
#     count=0
#     count= count + 1
#     print(aq,count)
# crawl_data5u()
# for a in ("{}()".format(crawl_daili66())):
    # print(a)

