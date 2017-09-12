#!/usr/bin/env python

import sys
import requests
import json
from utils.const_value import API, KEY, UNIT, LANGUAGE, LOCATION

user_query_weather_history = []

def get_input():
    return input("输入指令或您要查询的地名:").strip()

def fetch_weather(location):
    result = requests.get(API, params = {
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout = 1)
    if result.status_code == requests.codes.ok:
        parsed_json = json.loads(result.text)
        weather_data = parsed_json['results'][0]
        weather_info = weather_data['location']['name'] + ' ' + weather_data['now']['text'] + ' ' + weather_data['now']['temperature'] + '度' + ' ' + '风向' + weather_data['now']['wind_direction']
        time = weather_data['last_update']
        print(weather_info)
        print('更新时间：%s %s' % (time.split('T')[0], time.split('T')[1].split('+')[0]))
        user_query_weather_history.append(weather_info)
    else:
        print("暂时不支持您输入的地理位置和指令")

def main():
    print("输入 help 或 h 获取程序使用方法")
    while True:
        user_input = get_input()
        if user_input in ['help', 'h']:
            print("""
                输入城市名，查询该城市的天气;
                输入 help 或 h，获取帮助文档;
                输入 history，获取查询历史;
                输入 quit 或 q，退出天气查询系统。
               """)
        elif user_input in ['quit', 'q']:
            exit(0)
        elif user_input in ['history']:
            for value in user_query_weather_history:
                print(value)
        else:
            fetch_weather(user_input)

if __name__ == '__main__':
    main()
