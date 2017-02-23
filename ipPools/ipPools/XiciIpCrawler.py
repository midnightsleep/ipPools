# -*- coding: utf-8 -*-
# @Author: Wang
# @Date:   2017-02-10 10:40:08
# @Last Modified by:   Wang
# @Last Modified time: 2017-02-10 10:40:44

import requests
from bs4 import BeautifulSoup
from Sqlhelper import *
import logging
import logging.config


class XiciIpCrawler(object):

    def __init__(self):
        self.url = "http://www.xicidaili.com/nn/"
        logging.config.fileConfig("log/logger.conf")
        self.logger = logging.getLogger("XiciIpCrawler")

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
        self.logger.info("xici proxy size is " + len(l).__str__())
        # 返回该爬虫爬取的list
        return l