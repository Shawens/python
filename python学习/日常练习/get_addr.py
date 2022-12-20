


import random

province_name = [
'黑龙江省',
'青海省',
'陕西省',
'重庆',
'辽宁省',
'贵州省',
'西藏自治区',
'福建省',
'甘肃省',
'湖南省',
'湖北省',
'海南省',
'浙江省',
'河南省',
'河北省',
'江西省',
'江苏省',
'新疆维吾尔自治区',
'广西壮族自治区',
'广东省',
'山西省',
'山东省',
'安徽省',
'宁夏回族自治区',
'天津',
'四川省',
'吉林省',
'北京',
'内蒙古自治区',
'云南省',
'上海']


def get_addr(encoding=None):

    if encoding is None:
        encoding = "utf-8"

    try:
        random.shuffle(province_name)
        province_key = random.choice(province_name)
        with open("address1.txt", mode="r", encoding=encoding) as f:
            while True:

                line = f.readline().strip()
                if not len(line):
                    break
                line_l = line.split("\t")
                if province_key == line_l[0]:
                    ll = line_l[1].split(",")
                    city = random.choice(ll)
                    res = province_key+city
                    return res
    except Exception as e:
        # print(e)
        if encoding == "gbk":
            return get_addr("utf-8")

        return get_addr("gbk")



if __name__ == '__main__':
    print(get_addr("gbk"))


    for i in range(30):
        # print(get_address())
        print(get_addr("gbk"))
