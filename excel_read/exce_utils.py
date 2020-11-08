import os,xlrd
from excel_read.StudentBaseinfo import StudentBaseinfo  #操作Excel工具包
#1、获取Excel数据文件路径
# student_info = [对象1，对象2，对象3，....]
current_path = os.path.dirname(__file__)  # 获取当前路径
print(current_path)
excel_path = os.path.join(current_path,'../data/测试数据.xlsx')  #目录拼接  ../值得是返回当前目录的上一级

#  -------第一种方式：一个一个获取表格信息（比较蠢的方法）----------
'''
student_info = []  #存放学生列表
workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_index(0)
id = sheet.cell_value(1,0)
name = sheet.cell_value(1,1)
sex = sheet.cell_value(1,2)
age = sheet.cell_value(1,3)
score = sheet.cell_value(1,4)
student01 = StudentBaseinfo(id,name,sex,age,score)  #创建学生对象 并调用StudentBaseinfo的构造方法
student_info.append(student01)                      # 追加学生信息到student_info[]列表中
print(student_info[0].name)
'''
#  -------第二种方式：循环获取----------
''''
student_info = []  #存放学生列表
workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_index(0)
row_count = sheet.nrows  #获取总行数
for i in range(1,row_count):  #从第1行开始获取
    student01 = StudentBaseinfo(sheet.cell_value(i,0),  #id
                                sheet.cell_value(i,1),   #name
                                sheet.cell_value(i,2),   #age
                                sheet.cell_value(i,3),   #sex
                                sheet.cell_value(i,4))   #score
    student_info.append(student01)  # 追加学生信息到student_info[]列表中
# print(student_info[1].name)
n = len(student_info)
for i in range(n):  #循环打印某一列的信息，在student_info[i]列表中获取的信息   
    print(student_info[i].name)
'''
# -------第三种方式：做成方法--------------
'''
def read_excel_get_student_info(path):
    student_info = []  # 存放学生列表
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(0)
    row_count = sheet.nrows  # 获取总行数
    for i in range(1, row_count):  # 从第1行开始获取
        student01 = StudentBaseinfo(sheet.cell_value(i, 0),  # id
                                    sheet.cell_value(i, 1),  # name
                                    sheet.cell_value(i, 2),  # age
                                    sheet.cell_value(i, 3),  # sex
                                    sheet.cell_value(i, 4))  # score
        student_info.append(student01)  # 追加学生信息到student_info[]列表
    return  student_info

   #  测试方法
studentinfo = read_excel_get_student_info(excel_path)
print(studentinfo[1].name)
'''


#2、读取Excel保存为列表嵌套列表
#[[newdream001,张三，男，15，89],[newdream002,李四，男，16，87],.......]
all_student_info = []  #存放学生信息为列表
workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_index(0)
print(sheet.nrows,sheet.ncols)   #获取总行数  总列数
for i in range(1,sheet.nrows):   #读取行数   控制读取次数
    row_student_info = [] #存放单个学生信息
    for j in range(sheet.ncols):  #读取列
        row_student_info.append(sheet.cell_value(i,j))  #读取整行数据
    all_student_info.append(row_student_info)
print(all_student_info)


