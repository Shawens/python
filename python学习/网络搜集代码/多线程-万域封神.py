# -*- coding: utf-8 -*-
# @time: 2022/4/10 14:13
# @Author: JCS
# @Email:576767604@qq.com
# @File ：多线程-万域封神.py
# @Softwre: PyCharm
# -*- coding: utf-8 -*-
# @time: 2022/3/30 10:36
# @Author: JCS
# @Email:576767604@qq.com
# @File ：多线程获取返回值-类.py
# @Softwre: PyCharm
import os
import queue
import re
import sys
import time
from datetime import datetime
from io import TextIOWrapper
from threading import Thread
import requests
# sys.stdout = TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
now_time = datetime.now().strftime('%Y-%m-%d-%S')
book_dict = {}
zj_name = []
zj_url = []
book_name = []
book_text = []
class Get_Book(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            url = self.queue.get()
            try:
                download_txt(url)
            except:
                print('下载失败')
            finally:
                self.queue.task_done()
def get_url():
    global book_dict
    global zj_url
    global zj_name
    global book_name
    url2 = 'https://www.aixdzs.com/novel/万域封神'  # 章节
    yum_url = 'https://www.aixdzs.com'
    res = requests.get(url2)
    res.encoding = 'utf-8'
    selenium_book = re.findall(r'(<li class="chapter"><a href=".*?.html" title=".*?">.*?</a></li>)', res.text)
    book_name = re.findall(r'<h1>(.*?)</h1>', res.text)
    for i in selenium_book:
        txt = re.findall(r'.html" title="字数:\d+">(.*?)</a></li>', i)
        txt2 = re.findall(r'href="(.*?)" title="字数:', i)
        zj_name.append(txt[0])
        zj_url.append(f'{yum_url}{txt2[0]}')
        book_dict = dict(zip(zj_name, zj_url))
def download_txt(url):
    global book_text
    req = requests.get(url)
    req.encoding="utf-8"
    zj_txt = re.findall(r'<h1>(.*?)</h1>',req.text)[0]
    book_text.append(req.text)
    print(f'{zj_txt}缓存成功')
def wtie_txt():
    for t in book_text:
        # print(t.encode('gbk','ignore').decode('gbk'))
        book_text_v = re.findall(r'<div class="content">\n<p>?(.*?)</p>\n</div>', t)[0].replace('</p><p>', '\n')
        zj_txt = re.findall(r'<li><span>(.*?)</span></li>', t)[0]
        book_dict[zj_txt] = book_text_v
        # print(book_text_v.encode('gbk','ignore').decode('gbk'))

    zm_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    txt_path = f'{zm_path}\\多线程-{book_name[0]}{now_time}.txt'

    for k,v in book_dict.items():

        with open(txt_path,'a+',encoding="utf-8") as f:
            f.write(f'{k}\n\n{v}\n\n')
        print(f"{k}写入完成")
if __name__ == '__main__':
    start_time = time.time()
    get_url()
    queue = queue.Queue()
    for x in range(300):
        worker = Get_Book(queue)
        worker.daemon = True
        worker.start()
    for i in zj_url:
            queue.put(i)
    queue.join()
    wtie_txt()
    print('多线程耗时',time.time() - start_time) #多线程耗时 13.298081159591675
