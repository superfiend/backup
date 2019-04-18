import os
import re
from concurrent import futures

import requests
from bs4 import BeautifulSoup
from lxml.etree import HTML

from headers import Headers

"""
简化http请求中的headers中User-Agent以及Referer的操作, 以及添加了多线程的管理
"""


class HtmlUtil:

    # 初始化html请求的一些参数信息
    def __init__(self, max_workers=10):
        self.headers = Headers()
        self.timeout = None
        self.proxies = None
        self.__thread_pool_executor = futures.ThreadPoolExecutor(max_workers=max_workers)

    # 返回BeautifulSoup对象
    def get_soup(self, url, features='html.parser'):
        return BeautifulSoup(self.get_html(url), features)

    # 返回etree对象
    def get_tree(self, url):
        return HTML(self.get_html(url))

    # 通过html请求, 返回html页面的字符串形式
    def get_html(self, url, encoding='utf-8'):
        return self.get_html_content(url, self.headers.html_headers).decode(encoding)

    # 通过json请求, 返回html页面的字符串形式
    def get_json(self, url, encoding='utf-8'):
        return self.get_html_content(url, self.headers.json_headers).decode(encoding)

    # 通过html请求, 返回html页面的二进制形式
    def get_html_content(self, url, headers):
        headers['Referer'] = re.match('.*?//.*?/', url + '/').group()  # 添加Referer请求头
        return requests.get(url, headers=headers, timeout=self.timeout, proxies=self.proxies).content

    # 通过html请求头, 下载html页面
    def download_html(self, url, path, suffix=''):
        with open(HtmlUtil.__get_path(path, os.path.basename(url), suffix), 'wb') as f:
            f.write(self.get_html_content(url, self.headers.html_headers))

    # 通过json请求头, 下载html页面
    def download_json(self, url, path, suffix=''):
        with open(HtmlUtil.__get_path(path, os.path.basename(url), suffix), 'wb') as f:
            f.write(self.get_html_content(url, self.headers.html_headers))

    # 获取下载保存路径
    @staticmethod
    def __get_path(path, name, suffix):
        if not os.path.exists(path):
            os.makedirs(path)
        if not path.endswith('/'):
            path = path + '/'
        return path + name + suffix

    # 通过html请求头, 通过多线程, 下载html页面
    def download_html_by_thread(self, url, path, suffix=''):
        self.__thread_pool_executor.submit(self.download_html(url, path, suffix))

    # 通过json请求头, 通过多线程, 下载html页面
    def download_json_by_thread(self, url, path, suffix=''):
        self.__thread_pool_executor.submit(self.download_json(url, path, suffix))
