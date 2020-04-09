#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 13:41
# @Author  : xxlaila
# @Site    : 
# @File    : city_info.py
# @Software: PyCharm

import requests, json
from lib import config
import pypinyin


header = {"Content-Type":"application/json"}

def province_view():
    """
    获取一级城市，keywords 为空，获取全国的34个主要城市，获取指定城市设置为1，
    :return: province_result
    """
    province_result = []

    for city in config.city_s:
        # 获取全国城市
        city_url_result = '{}key={}&keywords=&subdistrict=1&extensions=base'.format(config.CI_URLS, config.KEYS)
        # 获取指定城市
        #city_url_result = '{}key={}&keywords={}&subdistrict=1&extensions=base'.format(config.CI_URLS, config.KEYS,city)
        gethost = requests.get(city_url_result, headers=header)
        JsonDatas = json.loads(gethost.content)
        city_as = JsonDatas["districts"][0]['districts']
        for city_a in city_as:
            province_result.append({
                "name": city_a['name'],
                "adcode": city_a['adcode'],
                "center": city_a['center']
            })
    # print(province_result)
    return province_result

def array_city():
    """
    对获取的城市状态进行序列化，
    :return:
    """
    s_city = []
    z_city = []

    array_datas = province_view()
    for array_data in array_datas:
        names = array_data['name']
        # print(array_data)
        s = ''
        if "山西省" not in names:
            for i in pypinyin.pinyin(names, style=pypinyin.NORMAL):

                s += ''.join(i)
            z_city.append( {
                "names": s,
                "name": array_data['name'],
                "adcode": array_data['adcode'],
                "center": array_data['center']
            })

        else:
            s_adcode = array_data['adcode']
            s_pinyin = "sanxisheng"
            s_city.append({
                "names": s_pinyin,
                "name": array_data['name'],
                "adcode": s_adcode,
                "center": array_data['center']

            })

    # print(z_city + s_city)
    return z_city + s_city

def lower_city():
    """
    获取省市的省会、其他城市
    :return:
    省会: lower_result
    其他城市: qt_citys_result
    """
    ones_city = array_city()
    lower_result = []
    qt_citys_result = []
    for lower in ones_city:
        lower_citys_url = '{}key={}&keywords={}&subdistrict=1&extensions=base'.format(config.CI_URLS, config.KEYS,lower['name'])
        gethost_lower_city = requests.get(lower_citys_url, headers=header)
        JsonData = json.loads(gethost_lower_city.content)
        lower_cts = JsonData["districts"]
        pncc = 100
        for pncc_citys in lower_cts:
            pncc_code = str(pncc_citys['adcode'][0:3])
            adcode_citys = pncc_code + str(pncc)
            s_citys = pncc_citys['districts']
            for s_city in s_citys:
                codes_city = pncc_citys['adcode']
                if adcode_citys in s_city['adcode']:
                # print(pncc_citys['name'])
                    lower_result.append({
                            "name": s_city['name'],
                            "citycode": s_city['citycode'],
                            "adcode": s_city['adcode'],
                            "center": s_city['center'],
                            "level": s_city['level']
                        })
                else:
                    qt_citys_result.append({
                        "name": s_city['name'],
                        "citycode": s_city['citycode'],
                        "adcode": s_city['adcode'],
                        "center": s_city['center'],
                        "level": s_city['level']
                    })

    # print(qt_citys_result)
    return lower_result, qt_citys_result

if __name__ == '__main__':
    lower_city()