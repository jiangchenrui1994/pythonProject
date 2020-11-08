import requests
# 在请求中添加cookie
#方式1：
# cookie_dict = {'company_name':'newdream'}
# requests.get(url= 'http://www.hnxmxit.com',cookies=cookie_dict)
# 方式2：
header_info_dic ={
    'cookie':'company_name=newdream'
}
requests.get(url= 'http://www.hnxmxit.com',headers=header_info_dic)
