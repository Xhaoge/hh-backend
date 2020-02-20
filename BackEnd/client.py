# -*- coding: utf-8 -*-
# 此文件用于测试 客户端

import requests

def client_post_pic():
    api_url = "http://localhost:8082/hh/pic_add"
    file_path = 'F:/11.jpg'
    file_name = file_path.split("/")[-1]
    file = open(file_path, "rb")
    files = {"file":(file_name, file, "image/jpg")}
    r = requests.post(api_url, files=files)

if __name__ == "__main__":
    client_post_pic()