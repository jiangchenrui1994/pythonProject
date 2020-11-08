from abc import ABCMeta,abstractmethod
#抽象类
#1、抽象类要有抽象方法
#2、要有抽象定义语句
#3、抽象类是用来被继承的，如果没有被继承，是毫无意义的
class animal(metaclass= ABCMeta):  #这种写法子类必须实现父类的抽象方法
    # __metaclass__ = ABCMeta  #抽象声明   这种写法子类不是强制性必须要实现抽象方法
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #抽象方法
    @abstractmethod
    def say(self):  #只定义不实现具体的内容，子类必须实现父类的抽象方法
        pass
class dog(animal):#父类是抽象类  1、实现父类的抽象方法  2、本身也是抽象类
    def __init__(self,name,age):
         super().__init__(name,age)
    def say(self):
         print('我是子类，我实现了父类的抽象方法：汪汪汪！！！')
    def test_say(self):
        print('我是子类，我实现了父类的抽象方法：汪汪汪！！！')

xiaohei = dog('小黑',2)
xiaohei.say()    #继承父类抽象方法
xiaohei.test_say()