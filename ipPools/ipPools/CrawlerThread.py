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
import ThreadStatus
import logging
import logging.config


class CrawlerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.t = ThreadValidator.ThreadValidator()
        self.crawler_time = config.CRAWLER_TIME
        logging.config.fileConfig("log/logger.conf")
        self.logger = logging.getLogger("CrawlerThread")

    def run(self):
        # 循环执行
        while True:
            self.logger.info("ThreadStatus.isCrawlerThread:"+ThreadStatus.isCrawlerThread.__str__())
            if (ThreadStatus.isCrawlerThread == False):
                # 启动xici爬虫
                xici = XiciIpCrawler.XiciIpCrawler()
                list_xici = xici.runCrawler()
                # 启动66ip爬虫
                ip66 = Ip66Crawler.Ip66Crawler()
                list_ip66 = ip66.runCrawler()
                # 将两个网站采集到的代理合并成一个list
                list_all = list(set(list_xici).union(set(list_ip66)))
                # 验证采集的代理的线程开启
                ThreadStatus.isCrawlerThread = True
                self.t.validatelist(list_all)

            # 停止一段时间，默认10分钟
            time.sleep(self.crawler_time)