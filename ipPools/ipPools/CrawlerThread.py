# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-02-10 10:43:08
# @Last Modified by:   Marte
# @Last Modified time: 2017-02-10 10:43:23

import Ip66Crawler
import XiciIpCrawler
import threading
import ThreadValidator
import config
import time


class CrawlerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.t = ThreadValidator.ThreadValidator()
        self.crawler_time = config.CRAWLER_TIME

    def run(self):
        # 循环执行
        while True:
            # 启动xici爬虫
            xici = XiciIpCrawler.XiciIpCrawler()
            list_xici = xici.runCrawler()
            # 启动66ip爬虫
            ip66 = Ip66Crawler.Ip66Crawler()
            list_ip66 = ip66.runCrawler()
            # 将两个网站采集到的代理合并成一个list
            list_all = list(set(list_xici).union(set(list_ip66)))
            self.t.validatelist(list_all)
            # 停止一段时间，默认两小时
            time.sleep(self.crawler_time)