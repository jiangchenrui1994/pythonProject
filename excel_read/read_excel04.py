#异常处理
import xlrd,os
# 1、让try范围更广
'''
def read_excel_get_student_list(excel_path):
    try:
        all_student_info = []  # 存放学生信息为列表

        workbook = xlrd.open_workbook(excel_path)
        sheet = workbook.sheet_by_index(0)
        for i in range(1, sheet.nrows):  # 读取行数   控制读取次数
            row_student_info = []  # 存放单个学生信息
            for j in range(sheet.ncols):  # 读取列
                row_student_info.append(sheet.cell_value(i, j))  # 读取整行数据
            all_student_info.append(row_student_info)
    except Exception as e:
        print('路径错误')
        return all_student_info

current_path = os.path.dirname(__file__)  # 获取当前路径
excel_path = os.path.join(current_path, '../data123/测试数据.xlsx')
print(read_excel_get_student_list(excel_path))
'''

# 2、看业务需求怎么定  （常用方法）
def read_excel_get_student_list(excel_path):
    all_student_info = []  # 存放学生信息为列表
    try:  #文件路径错误就给一个默认的路径
        workbook = xlrd.open_workbook(excel_path)
    except FileExistsError as e:
        print('文件路径错误，系统使用默认路径')
        current_path = os.path.dirname(__file__)  # 获取当前路径
        e_path = os.path.join(current_path, '../data/测试数据.xlsx')
        workbook = xlrd.open_workbook(e_path)
    sheet = workbook.sheet_by_index(0)
    for i in range(1, sheet.nrows):  # 读取行数   控制读取次数
        row_student_info = []  # 存放单个学生信息
        for j in range(sheet.ncols):  # 读取列
            row_student_info.append(sheet.cell_value(i, j))  # 读取整行数据
        all_student_info.append(row_student_info)
    return all_student_info

current_path = os.path.dirname(__file__)  # 获取当前路径
excel_path = os.path.join(current_path, '../data1/测试数据.xlsx')
print(read_excel_get_student_list(excel_path))