#  二次封装：函数封装
import xlrd,os
from excel_read.StudentBaseinfo import StudentBaseinfo

#  1、读取数据保存为对象
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
    return student_info

#  2、读取数据保存为列表
def read_excel_get_student_list(excel_path):
    all_student_info = []  # 存放学生信息为列表
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_index(0)
    for i in range(1, sheet.nrows):  # 读取行数   控制读取次数
        row_student_info = []  # 存放单个学生信息
        for j in range(sheet.ncols):  # 读取列
            row_student_info.append(sheet.cell_value(i, j))  # 读取整行数据
        all_student_info.append(row_student_info)
    return all_student_info

current_path = os.path.dirname(__file__)  # 获取当前路径
excel_path = os.path.join(current_path,'../data/测试数据.xlsx')

#  测试方法
print(read_excel_get_student_list(excel_path))
print(read_excel_get_student_info(excel_path)[0].name)