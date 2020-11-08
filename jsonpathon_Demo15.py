import jsonpath
import requests
import json
#json数据解析  从一个json体中取出你需要的字段数据过程
str = '{"name":"xiaoming","age":18,"sex":"男"}'
json_data = json.loads(str)
name = jsonpath.jsonpath(json_data,'$.name')
print(name[0])

str2='{"name":"xiaoming","age":18,"sex":"男","books":[{"bname":"拖延心理学","price":"89.4","date":"2020-09-23"},{"bname":"犯罪心理学","price":"59.4","date":"2019-09-23"}]}'
json_data2 =json.loads(str2)
price = jsonpath.jsonpath(json_data2,'$.books[1].price')
print(price)
