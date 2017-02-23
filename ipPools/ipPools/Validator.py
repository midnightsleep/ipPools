# -*- coding: utf-8 -*-
# @Author: wang
# @Date:   2017-02-10 10:40:08
# @Last Modified by:   Wang
# @Last Modified time: 2017-02-10 10:40:44

import requests
from Sqlhelper import *
import logging
import logging.config


class Validator(object):
    def __init__(self):
        self.validate_url = config.VOLIDATE_URL
        self.protocol = config.PROTOCOL
        self.timeout = config.TIME_OUT
        self.sqlhelper = Sqlhelper()
        logging.config.fileConfig('log/logger.conf')
        self.logger = logging.getLogger('Validator')

        # print self.validate_url
        # print self.protocol
        # print self.timeout

    def validate(self, proxy):
        '''
        验证代理是否可用
        :param proxy:
        :return:true or false
        '''
        np = self.protocol+"://"+proxy
        proxies = {self.protocol: np}
        status = 0
        try:
            r = requests.get(self.validate_url, proxies=proxies, timeout=self.timeout)
            status = r.status_code
        except Exception, e:
            self.logger.error(e.message)
            return status == 200
        return status == 200

    def valInsertProxytoSql(self, proxy):
        '''
        如果代理可用，插入到数据库中
        :param proxy:
        :return:true or false
        '''
        if (self.validate(proxy)):
            self.logger.info(proxy + u"有效")
            self.sqlhelper.insertProxy(proxy)
        else:
            self.logger.warning(proxy + u"无效")

    def valDelProxyfromSql(self, proxy):
        '''
        如果代理不可用，从数据库中删除
        :param proxy:
        :return:true or false
        '''
        if (not self.validate(proxy)):
            self.sqlhelper.deleteProxy(proxy)