import requests
import jsonpath

hosts ='https://api.weixin.qq.com'
get_param_dict ={
    'grant_type':'client_credential',
    'appid':'wx31860a05377fa17c',
    'secret':'b89245c9cb0d39f934e6945d00ced79f'
}
respon = requests.get(url='%s/cgi-bin/token'%hosts,
                      params=get_param_dict)
print(respon)
json_obj = respon.json()
print(json_obj)
#获取token
token_id = jsonpath.jsonpath(json_obj,'$.access_token')[0]  #接口验证，接口关联
print(token_id)
#创建标签
get_param_dict1 = {
    'access_token':token_id
}
post_data = {'tag':{'name':'jiangchenrui3p4'}}
response01 = requests.post(url='%s/cgi-bin/token'%hosts,
                           params=get_param_dict1,
                           json=post_data)
json_obj_1 = response01.json()
creat_tag_id =jsonpath.jsonpath(json_obj_1,'$.tag.id')[0]
# print(type(creat_tag_id),creat_tag_id)
# post_data01 = {"tag":{ "id":creat_tag_id,"name":"广州人"   }}
# resonse02 = requests.get(url='%s/cgi-bin/token'%hosts,
#                          params=get_param_dict1,
#                          json=post_data01)
# print(resonse02.json())
