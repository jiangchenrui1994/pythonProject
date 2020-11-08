'''
JISON数据：
jison数据是开发常用的数据报文交换格式，常用来模块之间或者前后端之间进行数据传递
jison数据类型有两种：
字典---键值对   {"name":"xiaoming","age":18,"sex":"男"}
数组形式
[
{"name":"xiaoming","age":18,"sex":"男"},
{"name":"xiaowang","age":15,"sex":"男"},
{"name":"xiaohong","age":19,"sex":"女"}
]
两者之间可以任意组合
{"name":"xiaoming","age":18,"sex":"男","books":["拖延心理学","犯罪心理学","狂人日记"]}
jison校验以及查看结构网址：https://www.bejson.com/-----点击jison视图

{"name":"xiaoming","age":18,"sex":"男","books":[{"bname":"拖延心理学","price":"59.4","date":"2020-09-23"},{"bname":"犯罪心理学","price":"59.4","date":"2019-09-23"}]}
'''

import json  #自带默认模块，用来处理json数据
import requests
str_dict = {"name":"xiaoming","age":18,"sex":"男"}
print(type(str_dict))

str1 = json.dumps(str_dict)    #把字典、json对象转化为字符串
print(type(str1))
print(repr(str1))   #repr()  转换为字符串，方便程序阅读的显示         str()  方便用户阅读的显示

str2 = '{"name":"xiaoming","age":18,"sex":"男"}'
str_json = json.loads(str2)  #把字符串转换为json数据，与dumps相反
print(type(str_json))
print(str_json)
print(str_json['sex'])
print(str_json.get('sex'))