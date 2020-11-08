#多态：一类事物，具有多种形态   多态前提必须要有继承  多态实现的过程中，会使用抽象类
#多态性：多态性是指具有不同功能的函数可以使用相同的函数
# TXT文件--双击打开查看内容
# EXE程序---双击安装软件
from abc import ABCMeta,abstractmethod
class File(metaclass=ABCMeta):
    @abstractmethod
    def double_click(self):
        pass
#不同类的多态表现
class txtFile(File):
    def double_click(self):
        print('打开TXT文件，查看内容')
class exeFile(File):
    def double_click(self):
        print('打开exe，安装软件')
class mp4File(File):
    def double_click(self):
        print('打开MP4，播放视屏')

#多态性：是指具有不同功能的函数可以使用相同的函数名
def double_click(file_obj):
    file_obj.double_click()
txt = txtFile()  #对象
exe = exeFile()
mp4 = mp4File()

#调用实现多态性
double_click(txt)
double_click(exe)
double_click(mp4)
