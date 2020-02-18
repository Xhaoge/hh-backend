# !/usr/bin/env python
# -*- coding:utf-8 -*-  

import os
import time
import logging

class Mylog():

    def __init__(self):
        print("this is mylog __init__")


    def buildLog(self):
        self.log = logging
        myformat = '%(asctime)s--%(levelname)s--[%(funcName)s-line:%(lineno)d]---"message":%(message)s'
        timename = time.strftime("%Y-%m-%d-%I-%M-%S", time.localtime()) + "-HHLog"
       

        filename = r'%s%s' % ("E:\\Logging\\HH",timename)+'.txt'

        if not os.path.exists("E:\\Logging\\HH"):
            os.makedirs("E:\\Logging\\HH")

        self.log.basicConfig(
            # 设置告警级别为INFO
            # 自定义打印的格式
            # 将日志输出到指定的文件中
            # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟
            level=logging.INFO,
            format=myformat,
            datefmt='%Y-%m/%d-%H:%M:%S',
            filename=filename,
            filemode='a'
        )