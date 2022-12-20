import datetime



'''
createDateString：创建指定长度随机中文的字符串,默认获取当前时间，可针对天进行调整
days：根据当前天数进行调整的天数
'''



def getTimeone ():

    return int(datetime.datetime.now().strftime('%Y%m%d'))

print(getTimenow())