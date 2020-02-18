# !/usr/bin/env python
# -*- coding:utf-8 -*-  

from http.service import BaseHTTPRequestHandler, HTTPServer

class SearchService(BaseHTTPRequestHandler):

    def __init__(self):
        print("this is search init.....")

    def do_Head(self):
        self.send_respoonse(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()