import requests
#  模拟get请求
# response  响应对象  （响应行   响应头   响应正文）
response = requests.get(url='http://www.hnxmxit.com/')  #get()模拟发送get请求


#获取响应正文有两种方式
#第一种
#print(response.content.decode('utf-8'))  #decode 解码  防止响应正文乱码
#第二种
response.encoding ='utf-8'
print(response.text)

