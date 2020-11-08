
#获取微信测试号步骤：微信公众号--进入微信公众号账号测试号申请系统--登录--微信扫一扫
#https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
# https :协议类型         api.weixin.qq.com  ：主机地址
#cgi-bin/token?   ：请求地址     grant_type=client_credential&appid=APPID&secret=APPSECRET   ：参数  参数之间用&分割
import requests
#get 请求携带参数
#方式一
# response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx31860a05377fa17c&secret=b89245c9cb0d39f934e6945d00ced79f')
# print(response.content.decode('utf-8'))
#注意，运行时关闭青花瓷，因为青花瓷没有ssl证书认证

#方式二：将参数做成字典 (比较常用，较为正规)
get_data_dict={
    "grant_type":"client_credential",
    "appid":"wx31860a05377fa17c",
    "secret":"b89245c9cb0d39f934e6945d00ced79f"
}
response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',params=get_data_dict)
print(response.content.decode('utf-8'))