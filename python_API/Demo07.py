import requests
response = requests.get(url = 'http://www.hnxmxit.com')

# 截取响应信息
# 响应行   响应状态码   响应信息     协议版本
print(response.status_code)   #状态码  200
print(response.reason)  #响应信息   ok

# 响应头
print(response.headers)  #所有响应头  {...}
print(response.headers['Server'])  #Server的头部信息
print(response.headers['Content-Encoding'])

# 响应正文
# 方式1   响应文本  只能获取文本内容，图片不能获取
# response.encoding = response.apparent_encoding
# print(response.text)

# 方式2：二进制响应内容
# print(response.content.decode('utf-8'))

#方式3：json响应正文
'''
get_data_dict={
    "grant_type":"client_credential",
    "appid":"wx31860a05377fa17c",
    "secret":"b89245c9cb0d39f934e6945d00ced79f"
}
response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',params=get_data_dict)
print(response.json())
'''
# 方式4：  原始响应内容 (一般不用这种方法)
response = requests.get(url='http://www.baidu.com',stream = True)
print(response.raw.read(1))


