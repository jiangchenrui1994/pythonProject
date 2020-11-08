# 二次封装：类封装
import xlrd,os
from excel_read.StudentBaseinfo import StudentBaseinfo

class ReadExcel:
    def __init__(self,excel_path):  #构造方法直接给路径
        self.excel_path = excel_path

    #  1、读取数据保存为对象
    def read_excel_get_student_info(self):
        student_info = []  # 存放学生列表
        workbook = xlrd.open_workbook(self.excel_path)
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
    def read_excel_get_student_list(self):
        all_student_info = []  # 存放学生信息为列表
        workbook = xlrd.open_workbook(self.excel_path)
        sheet = workbook.sheet_by_index(0)
        for i in range(1, sheet.nrows):  # 读取行数   控制读取次数
            row_student_info = []  # 存放单个学生信息
            for j in range(sheet.ncols):  # 读取列
                row_student_info.append(sheet.cell_value(i, j))  # 读取整行数据
            all_student_info.append(row_student_info)
        return all_student_info

#  测试方法
if __name__ == '__main__':
    current_path = os.path.dirname(__file__)  # 获取当前路径
    excel_path = os.path.join(current_path, '../data/测试数据.xlsx')
    stu = ReadExcel(excel_path)  #创建对象
    print(stu.read_excel_get_student_list())
    print(stu.read_excel_get_student_info()[0].name)