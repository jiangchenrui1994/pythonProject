#单继承
#继承   一个类获取另外一个类的属性和方法的过程
#  子类获取父类的属性或者方法
#人类：属性name  ,age,sex 方法：say()  sleep()
# 学生：  属性 name,age,sex   方法：say()   sleep()  study()
class people:
    def __init__(self,name,age,sex,studentid):
        self.name = name
        self.age = age
        self.sex = sex
        self.studentid = studentid
    def say(self):
        print('我是一个正直的人')
    def sleep(self):
        print('我是人类，我需要睡觉')
    def __drivercar(self):   #私有的属性和方法不能被继承
        print('我是一个老司机，今晚岳麓山见')

class student(people):  #继承于people
    #父类有构造方法的话，那子类必须实现构造方法
    def __init__(self,name,age,sex,studentid):
        #方法1  调用父类的构造方法，必须要传self
        people.__init__(self,name,age,sex)
        self.studentid = studentid

test = student('张三',20,'男',1)
test.say()
