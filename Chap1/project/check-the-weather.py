import os.path

# IDEA: https://stackoverflow.com/questions/40416072/reading-file-using-relative-path-in-python-project
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../resource/weather_info.txt")
locations_and_weather = {}
user_query_location_history = []

def process_data(arg):
    # IDEA: https://stackoverflow.com/questions/4803999/python-file-to-dictionary
    with open(arg) as f:
        for line in f:
            (key, value) = line.strip().split(',')
            locations_and_weather[key] = value

def app_usage(arg):
    if arg in ['help', 'h']:
        print("""
            输入城市名，查询该城市的天气;
            输入 help 或 h，获取帮助文档;
            输入 history，获取查询历史;
            输入 quit 或 q，退出天气查询系统。
           """)

def store_user_query_location(arg):
    if arg in locations_and_weather.keys():
        user_query_location_history.append(arg)

def query_history(arg):
    if arg == "history":
        for location in user_query_location_history:
            print(location, locations_and_weather[location])

def query_weather(arg):
    weather_result = locations_and_weather.get(arg, None)
    if weather_result:
        print("%s的天气情况为: %s" % (arg, weather_result))
    elif arg in ['quit', 'q']:
            exit(0)
    else:
        print("请输入地理位置，如您输入了地理位置，可能您输入的地理位置不在服务范围")

def process_user_input():
    return input("输入指令或您要查询的地名:").strip()

def main():
    process_data(path)
    print("输入 help 或 h 获取程序使用方法")
    while True:
        user_input = process_user_input()
        query_weather(user_input)
        store_user_query_location(user_input)
        query_history(user_input)
        app_usage(user_input)

if __name__ == '__main__':
    main()
