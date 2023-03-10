"""
变量的格式化输出：
    在python中可以使用print函数将信息输出到控制台
    如果希望输出文字信息的同时输出数据，就需要使用到格式化操作符
    % 被称为格式化操作符，专门用于处理字符串中的格式
        包含%的字符串被称为格式化字符串
        %和不同的字符连用，不同类型的数据需要使用不同的格式化字符
            格式化字符    含义
            %s          字符串
            %d          有符号十进制整数，%06d表示输出的整数显示显示位数，不足的地方使用 0 补全
            %f          浮点数，%.02f表示小数点后只显示两位
            %%          输出%
    语法格式如下：
        print("格式化字符串" % 变量1)
        print("格式化字符串" % （变量1，变量2，变量3.....）)
"""