#!/usr/bin/python3
# *-* coding:utf-8 *-*

import requests
from lxml import etree

if __name__ == "__main__":
    # 爬取笔趣阁小说内容
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
    }
    fp = open("shengxu.txt", "w", encoding="utf-8")
    i = 0
    for pageNum in range(1, 26):
        if i == 0:
            url = "https://www.bbiquge.net/book/24881/"
            page_text = requests.get(url=url, headers=headers).text
            i += 1
    # 获取小说章节目录源码数据
        else:
            url = "https://www.bbiquge.net/book/24881/index_%d.html"
            new_url = format(url % pageNum)
            page_text = requests.get(url=new_url, headers=headers).text
        # 对获取的页面源码数据进行数据解析, 这里用xpath解析, 解析方式还有bs4, 正则表达式
        tree = etree.HTML(page_text, parser=etree.HTMLParser(encoding="gbk"))
        chapter_url = tree.xpath("/html/body/div[4]/dl/dd/a/@href")
        for chapter in chapter_url:
            # 拿到完整的当前的章节的url(也就是链接)
            whole_url = "https://www.bbiquge.net/book/24881/"+chapter
            # 对拿到的url发起请求
            detail_text = requests.get(url=whole_url, headers=headers).text
            # 对拿到的页面源码数据在进行解析
            tree_1 = etree.HTML(detail_text, parser=etree.HTMLParser(encoding="gbk"))
            # 拿到标题
            title = tree_1.xpath("//*[@id='main']/h1/text()")[0]
            # 拿到当前章节内容
            content = tree_1.xpath("/html/body/div[3]/div[2]/div[1]//text()")
            text = ""
            for con in content:
                text = text+con+'\n'
            text = text.replace("\xa0\xa0\xa0\xa0", " "*4)+'\n'*3
            # 将爬取的数据存入文件
            fp.write(title+'\n'+text)
            print(title, "爬取成功!")
    fp.close()
