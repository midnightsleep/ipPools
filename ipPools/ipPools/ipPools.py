# -*- coding: utf-8 -*-
# @Author: Wang
# @Date:   2017-02-10 10:40:08
# @Last Modified by:   Wang
# @Last Modified time: 2017-02-10 10:40:44
from flask import Flask, jsonify

from Sqlhelper import *
import CrawlerThread
import UpdateThread


app = Flask(__name__)

sqlhelper = Sqlhelper()

@app.route('/')
def index():
    return '<h1>Hello wang!</h1>'


@app.route('/api/proxies')
def getAll():
    list1 = sqlhelper.getAllProxys()
    return list1.__str__()


@app.route('/api/proxy')
def getProxy():
    proxy = sqlhelper.getProxy()
    return proxy
    # return jsonify({'tasks': tasks})


@app.route('/api/count')
def getCount():
    list1 = sqlhelper.getAllProxys()
    return len(list1).__str__()
    # return jsonify({'tasks': tasks})

port = config.API_PORT


if __name__ == '__main__':
    # 检测代理的线程
    updatethread = UpdateThread.UpdateThread()
    # 开启检测线程
    updatethread .start()
    # 采集线程
    crawlerthread = CrawlerThread.CrawlerThread()
    # 开启采集线程
    crawlerthread.start()
    app.run(host='0.0.0.0', port=port)