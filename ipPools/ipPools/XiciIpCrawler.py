# -*- coding: utf-8 -*-
# @Author: Wang
# @Date:   2017-02-10 10:40:08
# @Last Modified by:   Wang
# @Last Modified time: 2017-02-10 10:40:44

import requests
from bs4 import BeautifulSoup
from Sqlhelper import *


class XiciIpCrawler(object):

    def __init__(self):
        self.url = "http://www.xicidaili.com/nn/"

    def runCrawler(self):
        l = []
        r = requests.get(self.url, headers=config.HEADER)
        html = r.text
        soup = BeautifulSoup(html)
        ipLists = soup.select("tr.odd > td")

        for i in range(1, len(ipLists), 10):
            ip = ipLists[i].get_text()
            port = ipLists[i+1].get_text()
            proxy = ip+":"+port
            proxy = proxy.encode('utf-8')
            # print proxy
            l.append(proxy)
        print l
        print "xici crawler over!"
        # 返回该爬虫爬取的list
        return l