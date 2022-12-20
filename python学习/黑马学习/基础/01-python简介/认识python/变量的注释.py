"""
不同类型变量之间的计算
    数字型变量之间可以直接计算
        在python中两个数字型变量是可以直接进行算数运算的
        如果变量是bool型，在计算时
            True对应的数字是1
            flase对应的数字是0
        演练步骤
            1.定义整数 i= 10
            2.定义浮点数 f = 10.5
            3.定义布尔型 b = True
            print(i * f)  # 整数乘以浮点型得出浮点型
            print(i * b)  # 整数乘以布尔型得出本身
            print(f * b)  # 浮点型乘以布尔型得出本身浮点型’
    字符串变量之间使用+拼接生成新的字符串
        在python中字符串之间可以使用+拼接生成新的字符串
        frist_name = ”三“
        last_name = "张"
        print(frist_name + last_name)
    数字型变量和字符串之间不能进行其他计算
input函数实现键盘输入
    在python中可以使用input函数从键盘等待用户的输入
    用户输入的任何内容 python都会认为是一个字符串
    语法如下
    字符串变量 = input("提示信息：")
类型转换函数
    int(x) : 将x转换一个整数
    float(x) ：将x转换一个浮点数
"""
input("请输入内容：")
i = 10
f = 10.5
b = True
print(i * f)  # 整数乘以浮点型得出浮点型
print(i * b)  # 整数乘以布尔型得出本身
print(f * b)  # 浮点型乘以布尔型得出本身浮点型’
frist_name = "三"
last_name = "张"
print(frist_name + last_name)


# 请输入苹果的价格
unitPrice = float(input("请输入苹果的单价："))
weight = float(input("请输入苹果的重量："))
money = unitPrice * weight
print(money)





