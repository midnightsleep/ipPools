# -*- coding: utf-8 -*-
# @Author: Wang
# @Date:   2017-02-10 10:40:08
# @Last Modified by:   Wang
# @Last Modified time: 2017-02-10 10:40:44

import requests
import re
from Sqlhelper import *
import logging
import logging.config


class Ip66Crawler(object):
    def __init__(self):
        self.url = "http://www.66ip.cn/nmtq.php?getnum=5500&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip"
        logging.config.fileConfig('log/logger.conf')
        self.logger = logging.getLogger('Ip66Crawler')

    def runCrawler(self):
        l = []
        r = requests.get(self.url, headers=config.HEADER)
        html = r.text
        reip = re.compile(r'(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}')
        for proxy in reip.findall(html):
            proxy = proxy.encode('utf-8')
            l.append(proxy)
        self.logger.info("66Ip proxy size is " + len(l).__str__())
        # 返回该爬虫爬取的list
        return l