import requests
import time
#超时设置
print(time.time())  #格林威治时间 当前时间（20201018）-19700101 秒数
response = requests.get(url = 'http://www.baidu.com',timeout = 0.001)    #float格式
print(time.time())
#特殊需求，公司  系统之间  有心跳包  A---B

#数值：float   接收数据的时间设定
#(0.1,0.2)   tuple  0.1 代表连接超时时间    0.2  代表接收数据超时时间