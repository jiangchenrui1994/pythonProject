#继承：一个类获取另外一个类的属性和方法的过程
#      子类获取父类的属性或者方法
#人类：属性 name,age,sex   方法：say（）  sleep（）
#学生：属性 name  age sex  studengtid  方法：say（）  sleep（） study（）
class people: #父类
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say(self):
        print('我是一个正直的人，我会说话')
    def sleep(self):
        print('我是人类，我需要睡觉')
class student(people):#继承与people   子类
    #父类有构造方法，子类必须实现构造方法
    def __init__(self,name,age,sex,studentid):
    #方法一：调用父类的构造方法  必须传self
        people.__init__(self,name,age,sex)
        self.studentid = studentid
    #方法二：使用super，这种方式不需要传self
        super().__init__(name,age,sex)
        self.studentid = studentid
    #方法三：使用super，此时super中的第一个参数是子类名称
        super(student,self).__init__(name,age,sex)
        self.studentid = studentid
    def study(self):  #子类重写父类的方法，子类对象调用的时候会优先调用自己的
        print('我是一个学生，我爱学习')
    def say(self):
        print('我是一个学生，我也是人类的一员')

test = student('张三',20,'男',1)
test.say()
test.study()
