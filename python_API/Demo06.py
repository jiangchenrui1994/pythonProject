#post请求模拟上传文件
import requests
import os


current_path = os.path.dirname(__file__)
print(current_path)
# excel_path = os.path.json(current_path,'..','data','testdata.xlsx')   #拼接文件路径

excel_path = current_path + '/../data/testdata.xls'  #也可用这种拼接方法，更正式
print(excel_path)
excel_file = {'file':open(excel_path,'rb')}  #将文件做成字典对象
print(excel_file)
# respons = requests.post(
#                         url = 'http://httpbin.org/post',
#                         files = excel_file
# )
# print(respons.content.decode('utf-8'))