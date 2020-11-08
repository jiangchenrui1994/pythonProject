'''
创建一个学生类：
属性：姓名  年龄   学号  方法：答到，展示学生信息
类属性：名称
创建一个班级类：
属性：学生，班级名  方法：添加学生，删除学生，点名
'''
class student:  #学生类
    designation = ''
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def showinfo(self):   #答道  展示学生信息
        print('我的名字叫{},我今年{}岁，我的学号是{}'.format(self.name,self.age,self.id))
class cla:
    students = []
    def __init__(self,student,ClassName):
        self.students.append(student)
        self.ClassName = ClassName
    #添加学生
    def AddStudent(self,name,age,id):
        self.students.append(student(name,age,id))
    #删除学生
    #students[['张三',18,1],['李四',19,2]]
    def RemoveStudent(self,name):
        names = []
        for n in range (len(self.students)):
            names.append(self.students[n].name)
        if name in names:
            for i in range(len(self.students)):
                if name == self.students[i].name:
                    self.students.remove(self.students[i])
                    break
        else:
            print('该学生不存在')

        #点名
    def dm(self,name):
        names = []
        for n in range(len(self.students)):
            names.append(self.students[n].name)
        if name in names:
            for i in range(len(self.students)):
                if name == self.students[i].name:
                    self.students[i].showinfo()
                    break
        else:
            print('该学生不存在')

zs = student('张三',18,1)
zs.showinfo()
test_class = cla(zs,'测试1班')
test_class.AddStudent('李四',19,1)
test_class.AddStudent('王二狗',18,2)
test_class.AddStudent('张吕丹',20,3)
# for n in range(len(test_class.students)):  #查看添加的学生名字
#     print(test_class.students[n].name)
test_class.dm('王二狗')
test_class.RemoveStudent('王二狗')
test_class.dm('王二狗')







