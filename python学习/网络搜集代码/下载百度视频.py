import requests
import re
import os
from concurrent.futures import ThreadPoolExecutor

"""
1、输入关键字搜索需要的视频
2、找到子页面链接
3、根据子页面链接请求获取到：playurl
4、下载数据
"""


def search_verdio(keyword):
    '''
    :param keyword: 输入关键字搜索视频
    :return 返回子链接列表
    '''
    url = 'https://www.baidu.com/sf/vsearch'
    data = {'pd': 'video', 'tn': 'vsearch', 'ie': 'utf-8', 'wd': str(keyword), 'async': '1', 'pn': '10'}
    num = 10  # 记录翻页，每次+10
    for i in range(20):
        data['pn'] = num
        res = requests.get(url, params=data)
        res.encoding = 'utf-8'
        # 解析
        obj = re.compile(
            ' <div class="video_small_intro">.*?href="(?P<href>.*?)".*? >(?P<title>.*?)</a>.*?<span class="wetSource c-font-normal">来源：(?P<sorce>.*?)</span>',
            re.S)
        result = obj.finditer(res.text)
        href_list = []
        for i in result:
            # 其他视频来源不好下载，所以锁定了好看视频
            if i.group('sorce') == '好看视频':
                href = i.group('href')
                # sorce = i.group('sorce')
                href_list.append(href)
                print(href)
        num += 10
        return href_list


def download_mp4(url):
    vediodFile = 'vediodFile'
    if not os.path.exists(vediodFile):
        os.mkdir(vediodFile)

    headers = {
        "User-Agent": "Mozilla/7.0 (Windows NT 10.0; Win32; x32) AppleWebKit/538.39 (KHTML, like Gecko) Chrome/99.0.4692.71 Safari/547.36"}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    obj = re.compile('.*?<title>(?P<title>.*?)</title>.*?playurl":"(?P<playurl>.*?)",', re.S)  # playurl
    palyurls = obj.finditer(resp.text)

    # 找出url和标题
    for i in palyurls:
        title = i.group('title').split(',')[0]
        playurl = i.group('playurl').replace('\\', '')
        # 下载视频
        with open(f'{vediodFile}/{title}.mp4', mode='wb') as f:
            res = requests.get(playurl)
            f.write(res.content)
        print(f'{title}下载完成')


if __name__ == '__main__':
    url_list = search_verdio('吉他弹唱')
    with ThreadPoolExecutor(10) as pool:  # 启用10个子线程
        for lis in url_list:
            pool.submit(download_mp4, url=lis)  # 提交任务
