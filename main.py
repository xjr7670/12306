#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from pprint import pprint

import pymysql
import requests
import re

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8967'
session = requests.Session()

class check_check(object):
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
            'Host': 'kyfw.12306.cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        self.session.headers.update(self.headers)

    def get_station_info(self):
        '''获取车站名称格式，并解析'''
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='test', charset='utf8')
        cur = conn.cursor()

        date = input('输入乘车日期：')
        from_station = input('输入出发站：')
        to_station = input('输入目的站：')

        with open('cn_station.html', encoding='utf-8') as fobj:
            stations = fobj.read()

        if from_station in stations and to_station in stations:
            sql = 'SELECT cname FROM station1 WHERE cn_name="%s" UNION SELECT cname FROM station1 WHERE cn_name="%s"' % (from_station, to_station)
            cur.execute(sql)
            rs = cur.fetchall()
            s = []
            for i in rs:
                s.append(i[0])    
            return (date, s[0], s[1])

    def check_rest_fee(self, date, from_station, to_station):
        '''输入日期、出发站及到站，查询余票信息'''

        request_url = "https://kyfw.12306.cn/otn/leftTicket/queryT?" \
                      "leftTicketDTO.train_date=%s" \
                      "&leftTicketDTO.from_station=%s" \
                      "&leftTicketDTO.to_station=%s" \
                      "&purpose_codes=ADULT" % (date, from_station, to_station)
        print(request_url)
        r = self.session.get(request_url, verify=False)
        return r.text

if __name__ == '__main__':
    c = check_check()
    date, from_station, to_station = c.get_station_info()
    print(date, from_station, to_station)
    piao = c.check_rest_fee(date, from_station, to_station)
    pprint(piao)
