import os,xlrd
#思路解答1：将Excel中的学生信息存放到列表中
#有三种方式获取表格中的数据信息）创建学生类  →  读取Excel中的数据做成学生对象存放到列表中

#思路解答2：将Excel中的学生信息存放到列表中
#读取Excel保存为列表嵌套列表

#1、获取Excel数据文件路径
current_path = os.path.dirname(__file__)  # 获取当前路径
print(current_path)
excel_path = os.path.join(current_path,'../data/测试数据.xlsx')  #目录拼接  ../值得是返回当前目录的上一级
# print(excel_path)

#2、读取Excel中的内容
workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_index(0)
value = sheet.cell_value(3,1)
print(value)

