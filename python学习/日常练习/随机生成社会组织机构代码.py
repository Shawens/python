#!/usr/bin/python
# 全国组织机构代码由⼋位数字（或⼤写拉丁字母）本体代码和⼀位数字（或⼤写拉丁字母）校验码组成
#
import random


def OrgCode():
    factorList = [3, 7, 9, 10, 5, 8, 4, 2]  # 加权因子列表
    OrgCode = []  # 用于存放生成的社会住址机构代码
    sum = 0
    for i in range(8):  # 随机取前8位数字
        OrgCode.append(random.randint(1, 9))  # 随机取1位数字
        sum = sum + OrgCode[i] * factorList[i]  # 使用OrgCode加权因子
        # print(dd)
    for i in range(len(OrgCode)):
        OrgCode[i] = str(OrgCode[i])  # 将OrgCode(int)变成str
    C9 = 11 - sum % 11  # C9代表校验码。用已经生成的前8位加权后与11取余，然后用11减
    # print（C9）
    if C9 == 10:  # 当C9的值位10时，校验码应用大写的拉丁字母X表示; 当C9的值为11时校验码用0表示，除此之外就是C9本身
        C9 = "X"
    else:
        if C9 == 11:
            C9 = '0'
        else:
            C9 = str(C9)
    OrgCode.append('-' + C9)
    return "".join(OrgCode)  # 拼接成最终生成的组织

