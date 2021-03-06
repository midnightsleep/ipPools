# -*- coding: utf-8 -*-
# @Author: wang
# @Date:   2017-02-10 10:40:08
# @Last Modified by:   Wang
# @Last Modified time: 2017-02-10 10:40:44
import threadpool
import Validator
from Sqlhelper import *
import ThreadStatus


class ThreadValidator(object):
    def __init__(self):
        self.thread_num = config.VOLIDATE_NUM
        self.v = Validator.Validator()

    def validatelist(self, list):
        '''
        使用线程池验证爬虫采集代理是否可用，可用则添加到数据库中
        :param list:
        :return:
        '''
        thread_num = config.VOLIDATE_NUM
        pool = threadpool.ThreadPool(thread_num)
        requests = threadpool.makeRequests(self.v.valInsertProxytoSql, list)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        # 验证采集的代理的线程结束
        ThreadStatus.isCrawlerThread = False

    def validatesql(self, list):
        '''
        使用线程池验证数据库中的代理是否可用，不可用则从数据库中删除
        :return:
        '''
        thread_num = config.VOLIDATE_NUM
        pool = threadpool.ThreadPool(thread_num)
        requests = threadpool.makeRequests(self.v.valDelProxyfromSql, list)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        # 验证数据库里的代理的线程结束
        ThreadStatus.isUpdateThread = False