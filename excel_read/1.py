#完成 打开京东-》登录-》搜索商品-》加入购物车-》付款结算 的脚本
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
#初始化浏览器
driver.get("https://www.jd.com")
#登录
driver.find_element_by_xpath('//a[text()="你好，请登录"]').click()
driver.find_element_by_xpath('//a[text()="账户登录"]').click()
driver.find_element_by_id('loginname').send_keys('17873672286')
driver.find_element_by_id('nloginpwd').send_keys('jJ08187742')
driver.find_element_by_id('loginsubmit').click()
sleep(10)
#搜索商品
driver.find_element_by_id('key').send_keys('华为P40')
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
sleep(5)
#进入商品详情页
js = "window.scrollTo(0,3000);"
driver.execute_script(js)
driver.find_element_by_id("J_AD_67117853959").click()
#切换窗口
new_win=driver.window_handles[-1]
driver.switch_to.window(new_win)
#加入购物车
sleep(5)
driver.find_element_by_id('InitCartUrl').click()
#点购物车结算
driver.find_element_by_id("GotoShoppingCart").click()
#点击结算
driver.find_elements_by_class_name('submit-btn')
#新增收货人地址
driver.find_elements_by_xpath('//*[@id="jd_area"]/div[1]/div')
# 下拉框元素定位，卡住了
driver.find_element_by_id('consignee_name').send_keys('姜琛瑞')
driver.find_element_by_id('consignee_address').send_keys('泰山三村50号楼707')
driver.find_element_by_name('consigneeParam.mobile').send_keys('17873672286')
driver.find_element_by_id('saveConsigneeTitleDiv').click()
#提交订单
driver.find_element_by_id('enterPriseUserPaymentSubmit').click()
sleep(10)
driver.quit()