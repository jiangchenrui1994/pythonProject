from abc import ABCMeta,abstractmethod
# 学生----去教室读书
# 老师----去教室上课
# people:name  age    方法：goto_class
class people(metaclass=ABCMeta):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @abstractmethod
    def goto_class(self):
        pass
class student(people):
    def __init__(self,name,age,courseName):
        super().__init__(name,age)
        self.courseName = courseName
        # 假如开发忘记写goto_class方法，，运行报错
    def goto_class(self):
        print('我是学生，我去教室读书')

class teacher(people):
    def __init__(self,name,age,teh_courseName):
        super().__init__(name,age)
        self.courseName = teh_courseName
    def goto_class(self):
        print('我是老师，我去教室教书')

zs = student('张三',20,'语文')
ls = teacher('李四',29,'数学')

