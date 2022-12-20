# 计算0~100之间内所有偶数之和
# 定义一个结果变量
result = 0;
# 定义一个初始变量i
i = 0;
# 设置循环
while i <= 100:
    # 打印输出变量i
    # 判断变量i是否为偶数
    if i % 2 == 0:
        # print(i);
        result += i
    # else:
    # print("i为奇数")
    i += 1;
print(result);
