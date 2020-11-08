import requests
#https://www.baidu.com/s?wd=newdream
get_param_dict={
    'wd':'newdream'
}
#get 模拟请求头部信息   当返回的响应数据提示'网络不给力'、或者返回的数据不是真正的业务数据时，需要模拟头部信息
#将青花瓷抓到的头部信息放在字典
header_info_dict={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
response = requests.get(url='https://www.baidu.com/s',params=get_param_dict,headers=header_info_dict)
print(response.content.decode('utf-8'))