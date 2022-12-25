# -*- coding: UTF-8 -*-
programmers = [
    "约翰·巴科斯(JohnWarnerBackus), 创建了Fortran语言",
    "阿兰·库珀(Alan Cooper), 开发了Visual Basic语言",
    "詹姆斯·高斯林(James Gosling), 开发了Java语言",
    "安德斯·海尔斯伯格(Anders Hejlsberg), 开发了Turbo Pascal、Delphi、C#以及TypeScript",
    "丹尼斯·里奇(Dennis MacAlistair Ritchie), 发明了C语言",
    "比雅尼·斯特劳斯特鲁普(Bjarne Stroustrup), 他以创造C++编程语言而闻名，被称为“C++之父”",
    "吉多·范罗苏姆(Guido van Rossum), 创造了 Python"
]
def parse_parts(creator):
    index = creator.find(',')
    name, achievement = creator[0:index], creator[index+1:]
    return name.strip(), achievement.strip()

def parse_name(name):
    index = name.find('(')
    name_cn, name_en = name[0:index], name[index:]
    name_en = name_en[1:len(name_en)-1]
    return name_cn, name_en

def parse_creators(creators):


if __name__ == '__main__':
    creators = ...
    profiles = parse_creators(creators)
    print(profiles)