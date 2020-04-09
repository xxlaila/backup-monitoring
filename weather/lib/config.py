#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 16:44
# @Author  : xxlaila
# @Site    : 
# @File    : config.py
# @Software: PyCharm

# 高德
KEYS="11dsadaekjgr8dysfky4whdnkasnjidgas"
# 天气
WE_URLS="https://restapi.amap.com/v3/weather/weatherInfo?"
# 城市
CI_URLS="https://restapi.amap.com/v3/config/district?"

# 城市值
city_s = ["重庆"]

# zabbix
# 3.4 APi (https://www.zabbix.com/documentation/3.4/zh/manual/api)
# ApiUrl = 'http://zabbix.ops.xxlaila.cn/zabbix/api_jsonrpc.php'

# 4.4 Api (https://www.zabbix.com/documentation/current/manual/api)
ApiUrl = 'http://zabbix.dev.xxlaila.cn/api_jsonrpc.php'
user = "Admin"
password = "zabbix"