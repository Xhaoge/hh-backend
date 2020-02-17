# !/usr/bin/env python
# -*- coding:utf-8 -*-  

import os
import yaml

class Config:

    def __init__(self):
        self.read_base()

    def read_base(self):
        basedir = os.path.dirname(__file__)
        filename = basedir + "\\base.yaml"
        print("filename: ",filename)
        with open(filename, 'r', encoding='utf-8') as f:
            yy = yaml.load(f.read(),Loader=yaml.Loader)
            print(yy)
            print("yy: mysql: ",yy["mysqlDB"])