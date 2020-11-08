#异常分类
# 1、系统异常：下标越界，路径找不到、值输入错误
# 2、业务异常：年龄只能输入1~120、账号密码错误、充值只能是正数
# 3、触异常：触发异常有raise触发的，只要有raise就会报错
'''
try:
    raise IndexError('报错了')   #创建了一个报错对象，并且赋值
except IndexError as e:       #e就是报错的对象
    print(e)     #打印值得内容
print('hello world!!!')
'''

#要求输入的值在0~4范围之内
#自定义业务异常类
class onlyInput04Error(Exception):   #继承于exception（基类）
    def __str__(self):
        return '输入的数据不再0~4范围之内'
try:
    num = int(input('请输入0~4之间的数据：'))
    if num<0 or num>4:
        raise onlyInput04Error()   #手动触发报错
except onlyInput04Error as e:
    print(e)
except Exception as e:
    print('报错了，不知是什么错')