#异常处理  异常也是对象，，可进行操作
# 下标越界

try:  #try下面写运行可能出错的diamante
    num = int(input('请输入1~5之间的数字：'))
    lista = [1,2,3,4,5]
    print(lista[num])
except IndexError as e:  #出错之后的处理
    print('下标越界')
# except ValueError as e:
#     print('输入的数据类型出错')
except Exception as e:   #异常的所有基类，一般在异常监控最后都加上,代表所有的错误
    print('报错了，但是不知道什么原因')
# else:    #try中没有发生异常则执行else中的代码，发生异常则不执行下面的代码
#     print('hello word!')   #上面虽然报错，但程序会继续往后执行
finally:
    print('不管是否报错，我都会一直执行')