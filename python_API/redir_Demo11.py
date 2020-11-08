#  重定向  请求或响应的时候，状态码为3**
#  http://www.360buy.com
import requests
response = requests.get(url='http://www.360buy.com')
print(response.history)  #显示请求的重定向的信息
print(response.url)  #展示响应的连接
print(response.content.decode('utf-8'))
# requests 在发送请求的时候，会自动进行重定向处理   不需要干预

print('**********************************************')
response = requests.get(url='http://www.360buy.com',allow_redirects = False)  #allow_redirects  关闭重定向的开关
print(response.history)  #显示请求的重定向的信息
print(response.url)  #展示响应的连接
print(response.content.decode('utf-8'))