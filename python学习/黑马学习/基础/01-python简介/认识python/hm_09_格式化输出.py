"""
定义字符串变量name ,输出我的名字叫小明，请多多关照
"""
name = "小明"
print("我的名字叫：%s 请多多关照" % name)
# 定义整数变量student_no ,输出我的学号是00001
student_no = 1
print("我的学号是：%04d" % student_no)
# 定义小数 price,weight,money,输出苹果单价 9.00 元一斤，购买了 5.45斤 一共付了49.05元
price = 9.00
weight = 5.45
money = float(price) * float(weight)
print("苹果单价 %.02f 元一斤，购买了 %.02f 斤 一共付了 %.02f 元" % (price, weight, money))
# 定义一个小数scale ,输出数据比例为 10.02%
scale = 10.02
print("数据比例为 %.2f%%" % scale)
print("数据比例为 %.2f%%" % (scale * 10))
