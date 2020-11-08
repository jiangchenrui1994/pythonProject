#代理设置
# 1、爬虫类项目  有检测机制
# 2、系统有防灌水等功能
# 3、需要翻墙做接口测试
import requests
proxy_server = {'http':'http://127.0.0.1:8888',
                'https':'http://127.0.0.1:8888'
}
# VPN代理设置  包含用户名和密码
# proxy_server_password = {'https':'http://username:password@127.0.0.1:8888'}

response = requests.get(url='http://www.hnxmxit.com/',proxies=proxy_server)  #proxies设置代理的关键字
print(response.status_code)