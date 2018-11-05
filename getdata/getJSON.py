#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import conf.header as header
import conf.hqUrl as hqUrl
import json

#发送请求并获取数据的json串
def getJSON(StockListName,StockListUrl):
    req = requests.get(StockListUrl,headers = header.send_headers)
    print(StockListName)
    result = req.text
    print(result)

#获取股市行情信息,如沪深一览、龙虎榜、创业板
def getStockList():
    for StockListName,StockListUrl in hqUrl.dict.items():
        getJSON(StockListName,StockListUrl)



