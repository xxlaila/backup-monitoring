#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 13:41
# @Author  : xxlaila
# @Site    : 
# @File    : weather.py
# @Software: PyCharm

import requests, json
from lib import config
from city_info import lower_city
header = {"Content-Type":"application/json"}

def city_weathers(lower_city_names):
    """
    获取各个省会的天气状况
    :return: weather_result
    """

    weather_result = []
    for weather_city_adcode in lower_city_names:
        wea_url = '{}key={}&keywords=&city={}'.format(config.WE_URLS, config.KEYS,weather_city_adcode['adcode'])
        gethost_weather = requests.get(wea_url, headers=header)
        JsonData = json.loads(gethost_weather.content)
        # print(JsonData[JsonData][0]['weather'] )       # zabbix的item选项Preprocessing里面的JsonPath值可以使用这个方式来进行验证
        weather_cis = JsonData["lives"]
        for weather_ci in weather_cis:

            weather_result.append({
                "省份": weather_ci["province"],
                "省会": weather_ci["city"],
                "区域编码": weather_ci["adcode"],
                "天气": weather_ci["weather"],
                "气温": weather_ci["temperature"],
                "风向": weather_ci["winddirection"],
                "风力": weather_ci["windpower"],
                "空气湿度": weather_ci["humidity"]
            })

    print(weather_result)
    return weather_result

if __name__ == '__main__':
    lower_city_names, qt_citys_result= lower_city()
    city_weathers(lower_city_names)