# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-02-10 10:43:08
# @Last Modified by:   Marte
# @Last Modified time: 2017-02-10 10:43:23

import sqlite3
import config


class Sqlhelper(object):
    tableName = config.DB_CONFIG['table']
    dbPath = config.DB_CONFIG['dbPath']

    def __init__(self):
        # 连接数据库
        self.con = sqlite3.connect(self.dbPath, check_same_thread = False)
        # self.con.text_factory = str
        self.cursor = self.con.cursor()
        # 创建表结构
        self.createTable()

    def createTable(self):
        '''
        创建一个代理表
        :return:
        '''
        create_tb_sql = "CREATE TABLE IF NOT EXISTS "+self.tableName+"(id integer PRIMARY KEY autoincrement, proxy varchar(25) UNIQUE)"
        self.cursor.execute(create_tb_sql)
        self.con.commit()

    def getAllProxys(self):
        '''
        获取所有的代理,以list的形式返回
        :return:
        '''
        list1 = []
        get_proxies_sql = "SELECT proxy FROM "+self.tableName
        self.cursor.execute(get_proxies_sql)
        for tubproxy in self.cursor.fetchall():
            proxy = tubproxy[0].encode('utf-8')
            list1.append(proxy)
        return list1

    def getProxy(self):
        '''
        随机返回1个代理
        :return:
        '''
        get_proxy_sql = "SELECT proxy FROM "+self.tableName+" ORDER BY RANDOM() limit 1"
        self.cursor.execute(get_proxy_sql)
        return self.cursor.fetchall()[0]

    def insertProxy(self, proxy):
        '''
        添加代理到数据库中
        :param proxy: 代理
        :return:
        '''
        try:
            self.cursor.execute('INSERT INTO '+self.tableName+' VALUES (null,?)', (proxy,))
        except Exception, e:
            print e.message
        self.con.commit()

    def getCount(self):
        '''
        获取代理池中代理的数量
        :return:
        '''
        self.cursor.execute('SELECT * FROM '+self.tableName)
        return len(self.cursor.fetchall())

    def getProxyCount(self, proxy):
        '''
        获取代理池中代理的数量
        :return:
        '''
        self.cursor.execute("SELECT * FROM "+self.tableName+" WHERE proxy= '%s'" % proxy)
        return len(self.cursor.fetchall())

    def deleteProxy(self, proxy):
        '''
        从数据库中删除失效的代理
        :param proxy:
        :return:
        '''
        del_proxy_sql = "DELETE FROM "+self.tableName+" WHERE proxy= '%s'" % proxy
        try:
            self.cursor.execute(del_proxy_sql)
        except Exception, e:
            print e.message
            return False
        self.con.commit()
        return True

    def closeDb(self):
        '''
        关闭数据库连接
        :return:
        '''
        self.cursor.close()
        self.con.close()