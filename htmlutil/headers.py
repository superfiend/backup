import random


class Headers:

    # 初始化http请求头信息
    def __init__(self):
        self.__user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/73.0.3683.86 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50']
        self.headers = {}

    # 添加http请求头信息
    def append(self, header: dict):
        if header is not None:
            self.headers = dict(self.headers, **header)

    # 返回html的请求头
    @property
    def html_headers(self):
        if self.headers.__contains__('X-Requested-With'):
            self.headers.pop('X-Requested-With')
        if self.headers.__contains__('X-Request'):
            self.headers.pop('X-Request')
        self.headers['User-Agent'] = random.choice(self.__user_agents)
        self.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        return self.headers

    # 返回json的请求头
    @property
    def json_headers(self):
        self.headers['Accept'] = 'application/json'
        self.headers['X-Requested-With'] = 'XMLHttpRequest'
        self.headers['X-Request'] = 'JSON'
        self.headers['User-Agent'] = random.choice(self.__user_agents)
        return self.headers
