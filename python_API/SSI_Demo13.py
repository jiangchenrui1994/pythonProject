import requests
import warnings
import urllib3
# https必须带证书操作， 处理方式一：不验证证书，报警告，返回200
# 关闭警告
#方案1：老版本  （废弃）
# from requests.packages import urllib3   #requests版本  2.6.0
# urllib3.disable_warnings()
#方案2：新版本
# requests.packages.urllib3.disable_warings()  #方案二  （最常用）
# warnings.filterwarnings('ignore')             #方案三
urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)   #方案四
response = requests.get(url = 'https://www.12306.cn',verify=False)  #关闭证书认证
print(response.content.decode('utf-8'))


# 安装：pyopenssl  模块，就不会报正式认证错误

#加上证书认证  公司内部  开发同事  ****。crt  (最稳妥的方式)
response = requests.get('https://www.12306.cn',cert =('/path/server.crt','/path/key'))