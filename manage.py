#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from pprint import pprint

from Flask import flask
from flask_script import Manager, Shell
import pymysql
import requests
import re

if __name__ == '__main__':
    c = check_check()
    date, from_station, to_station = c.get_station_info()
    print(date, from_station, to_station)
    piao = c.check_rest_fee(date, from_station, to_station)
    pprint(piao)
