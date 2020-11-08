#模拟post请求（微信公众号）
import requests
import json
#https://api.weixin.qq.com/cgi-bin/tags/create?access_token=ACCESS_TOKEN
# 首先获取token，获取方法见Demo02
url_param_dict = {
    "access_token":"38_242HxMdfkAu5xmu1-8-2AV7KEro5SEat0SyOapy9nmlVSNcSJZn6PqsaFJ88kjINnFA9l_ldLOG-tTYL6lYKd8d1yLOc4MhTxYKOv6WS7sTR4JUVGemNWaqnehvMdIb67MnVWalGPPWXmxg1PWQjAFAVCW"
}
post_param_data = {"tag" : {"name" : "hunanP3&P4"} }
respons = requests.post(url = 'https://api.weixin.qq.com/cgi-bin/tags/create',
                        params = url_param_dict,
                        # json = post_param_data,  #第一种方法   获取json字符串
                        data = json.dumps(post_param_data)  #第二种方式
                        )
print(respons.content.decode('utf-8'))
