# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-02-10 10:43:08
# @Last Modified by:   Marte
# @Last Modified time: 2017-02-10 10:43:23

import threading
import ThreadValidator
import time
from Sqlhelper import *


class UpdateThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.t = ThreadValidator.ThreadValidator()
        self.update_time = config.UPDATA_TIME * 60
        self.sqlhelper = Sqlhelper()

    def run(self):
        # 循环执行
        while True:
            # 停止一段时间，默认30分钟
            time.sleep(self.update_time)
            # 获取所有的代理池中的所有代理
            list = self.sqlhelper.getAllProxys()
            self.t.validatesql(list)