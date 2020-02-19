# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
# from . import db
from .models import getUsers

search_info = Blueprint('search',__name__)

@search_info.route("/search_get", methods=["GET"])
def index():
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1


@search_info.route("/search_post", methods=["POST"])
def search_hello():
    rr = getUsers()
    print(rr)
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh



# @search_info.route('/index', methods=['GET'])
# def send_store():
#     '''
#     SXT
#     店铺信息api，
#     餐馆图像存储在'/static/images/store_img/'目录下
#     20180625 pro:数据库构建不完整
#     '''
#     store_data_temp = []
#     for store_info1 in Store.query.order_by(Store.id):
#         store_data1 = {
#             'icon': '/static/image/store_img/' + store_info1.storeName + '/LOGO.jpg',
#             'storeName': store_info1.storeName,
#             'storeID': store_info1.id,
#             'starRating': store_info1.rating,
#             'price': store_info1.price,
#             'monthlySell': store_info1.monthlySale,
#             'distance': store_info1.distance,
#             'isDiscount': store_info1.isDiscount,
#             'DiscountNumber': store_info1.discountNumber,
#             'isAppOffer': store_info1.isAppOffer
#         }
#         store_data_temp.append(store_data1)
#     store_data = {
#         'listStoreData':store_data_temp
#     }
#     json_store_data = jsonify(store_data)
#     return json_store_data
