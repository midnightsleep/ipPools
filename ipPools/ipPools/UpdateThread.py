# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-02-10 10:43:08
# @Last Modified by:   Marte
# @Last Modified time: 2017-02-10 10:43:23

import threading
import ThreadValidator
import time
from Sqlhelper import *
import ThreadStatus
import logging
import logging.config


class UpdateThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.t = ThreadValidator.ThreadValidator()
        self.update_time = config.UPDATA_TIME * 60
        self.sqlhelper = Sqlhelper()
        logging.config.fileConfig("log/logger.conf")
        self.logger = logging.getLogger("UpdateThread")

    def run(self):
        # 循环执行
        while True:
            self.logger.info("ThreadStatus.isUpdateThread:"+ThreadStatus.isUpdateThread.__str__())
            # 停止一段时间，默认30分钟
            time.sleep(self.update_time)
            if (ThreadStatus.isUpdateThread == False):
                # 获取所有的代理池中的所有代理
                proxylist = self.sqlhelper.getAllProxys()
                # 验证数据库的代理的线程开启
                ThreadStatus.isUpdateThread = True
                self.t.validatesql(proxylist)