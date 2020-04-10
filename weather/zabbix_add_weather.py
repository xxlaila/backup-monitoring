#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 11:21
# @Author  : xxlaila
# @Site    : 
# @File    : zabbix_add_weather.py
# @Software: PyCharm

import requests, json
from lib import config
from city_info import array_city

header = {"Content-Type": "application/json"}

def gettoken():
    data = {"jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": config.user,
                    "password": config.password
                },
                "id": 1,
                "auth": None
            }
    auth=requests.post(url=config.ApiUrl,headers=header,json=data)
    return json.loads(auth.content)["result"]

def get_host(auth):
    """
    获取的主机id, interface
    :param auth:
    :return:
    """
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]

        },
        "auth": auth,
        "id": 2
    }
    gethost = requests.post(url=config.ApiUrl, headers=header, json=data)
    # 在多主机里面，选择返回结果的第一台服务器，
    JsonDatas = json.loads(gethost.content)['result'][0]
    hostid = JsonDatas['hostid']
    interface =  JsonDatas['interfaces'][0]['interfaceid']

    # print(hostid, interface)
    return hostid, interface


def createhttpitem(auth):
    hosts_id, interface_id = get_host(auth)
    for dic in city:
        data={
        "jsonrpc": "2.0",
        "method": "item.create",
        "params": {
            "url":"https://restapi.amap.com/v3/weather/weatherInfo?",
            "query_fields": [
                {
                    "city":"%s" % dic['adcode']
                },
                {
                    "key": config.KEYS
                }
            ],
            "interfaceid": "%s" % interface_id,
            "type":"19",
            "hostid": hosts_id,
            "delay":"5m",
            "key_":"%s" % dic['names'],
            "name":"%s" % dic['names'],
            "value_type":"1",
            "output_format":"0",
            "timeout":"3s"

        },
        "auth": auth,
        "id": 1
        }
        httpagents=requests.post(url=config.ApiUrl,headers=header,json=data)
        # print(json.loads(httpagents.content))
        httpagent=json.loads(httpagents.content)['result']['itemids'][0]
        print(httpagent)
        data={
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
            "hostid": hosts_id,
            "name": "%s-weather" % dic['names'],
            "key_": "%s-weather" % dic['names'],
            "type": "18",
            "master_itemid": httpagent,
            "value_type": "1",
            "preprocessing": [
                {
                    "type": "12",
                    "params": "$.lives.[0].weather",
                    "error_handler": "1",
                    "error_handler_params": ""
                }
            ]
            },
            "auth": auth,
            "id": 1
        }
        dependqw=requests.post(url=config.ApiUrl,headers=header,json=data)
        print(dependqw.content)
        data={
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
            "hostid": hosts_id,
            "name": "%s-windpower" % dic['names'],
            "key_": "%s-windpower" % dic['names'],
            "type": "18",
            "master_itemid": httpagent,
            "value_type": "1",
            "preprocessing": [
                {
                    "type": "12",
                    "params": "$.lives.[0].windpower",
                    "error_handler": "1",
                    "error_handler_params": ""
                }
            ]
            },
            "auth": auth,
            "id": 1
        }
        dependfl=requests.post(url=config.ApiUrl,headers=header,json=data)
        data={
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
            "hostid": hosts_id,
            "name": "%s-temperature" % dic['names'],
            "key_": "%s-temperature" % dic['names'],
            "type": "18",
            "master_itemid": httpagent,
            "value_type": "3",
            "preprocessing": [
                {
                    "type": "12",
                    "params": "$.lives.[0].temperature",
                    "error_handler": "1",
                    "error_handler_params": ""
                }
            ]
            },
            "auth": auth,
            "id": 1
        }
        dependqw=requests.post(url=config.ApiUrl,headers=header,json=data)
        data={
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
            "hostid": hosts_id,
            "name": "%s-winddirection" % dic['names'],
            "key_": "%s-winddirection" % dic['names'],
            "type": "18",
            "master_itemid": httpagent,
            "value_type": "1",
            "preprocessing": [
                {
                    "type": "12",
                    "params": "$.lives.[0].winddirection",
                    "error_handler": "1",
                    "error_handler_params": ""
                }
            ]
            },
            "auth": auth,
            "id": 1
        }
        dependfx=requests.post(url=config.ApiUrl,headers=header,json=data)
        data={
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": {
            "hostid": hosts_id,
            "name": "%s-humidity" % dic['names'],
            "key_": "%s-humidity" % dic['names'],
            "type": "18",
            "master_itemid": httpagent,
            "value_type": "0",
            "preprocessing": [
                {
                    "type": "12",
                    "params": "$.lives.[0].humidity",
                    "error_handler": "1",
                    "error_handler_params": ""
                }
            ]
            },
            "auth": auth,
            "id": 1
        }
        dependsd=requests.post(url=config.ApiUrl,headers=header,json=data)
        data={
        "jsonrpc": "2.0",
        "method": "trigger.create",
        "params": [
            {
                "description": "%s温度有点高" % dic['name'],
                "expression": "{Zabbix server:%s-temperature.last()}>30" % dic['names'],
                "opdata": "当前气温:{ITEM.LASTVALUE}",
                "priority": 3,
                "manual_close": 1
            },
            {
                "description": "%s温度有点低" % dic['name'],
                "expression": "{Zabbix server:%s-temperature.last()}<13" % dic['names'],
                "opdata": "当前气温:{ITEM.LASTVALUE}",
                "priority": 3,
                "manual_close": 1
            }
        ],
        "auth": auth,
        "id": 1
        }
        triggercreate=requests.post(url=config.ApiUrl,headers=header,json=data)
        print(json.loads(triggercreate.content))
    return json.loads(dependqw.content)

if __name__ == '__main__':
    city = array_city()
    auth=gettoken()
    createhttpitem(auth)
