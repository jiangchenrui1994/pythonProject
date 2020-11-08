#异常
import requests
from requests.exceptions import MissingSchema,ConnectionError,RequestException

try:
    reponse = requests.get(url = 'www.baidu.com')
except MissingSchema as e:   #丢失HTTP
    print('http/https前缀没加')
except ConnectionError as e:  # 丢失HTTP
    print('连接超时')
except RequestException as e:  # 丢失HTTP
    print('请求异常')