# #多继承    一个子类有多个父类
# # 人类  --老师--司机
# class people:
#     def __init__(self,name):
#         self.name = name
#     def say(self):
#         print('我是人类，我会说话')
#     def sleep(self):
#         print('我需要睡觉')
#
# class teacher:
#     def __init__(self,courseName):
#         self.courseName = courseName
#     def say(self):
#         print('我是一名老师，我会教书')
#     def play(self):
#         print('我是老师，我会打球')
#
# class driver(teacher，people):   #假如父类中有多种同名方法，那么就按照父类先后顺序惊醒调用
#     def __init__(self,name,courseName,drivingYears):
#         people.__init__(self,name)
#         teacher.__init__(self,courseName)
#         self.drivingYears = drivingYears
#     def say(self):
#         print('我是兼职的滴滴司机，白天我是一名老师')
# laowang = driver('老王','体育',8)
# print('我的名字叫{},我有{}年驾另'.format(laowang.name,laowang.courseName))
#
