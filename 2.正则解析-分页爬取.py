#! /usr/bin/python3
# *-* coding:utf-8 *-*

import requests
import re
import os

if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"}
    # 创建一个文件夹(先判断该文件夹是否存在)
    if not os.path.exists("./nituLibs"):
        os.mkdir("./nituLibs")
    url = "https://www.nipic.com/topic/%d.html"
    for pageNum in range(1, 10):
        new_url = format(url % pageNum)
        # 使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text
        # 使用聚焦爬虫将页面中的所有图片进行解析/提取
        ex = '<li class="new-search-works-item-all">.*?<img src="(.*?)" alt.*?</li>'
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            # 拼接出一个完整的图片url
            whole_src = "https:"+src
            try:
                # 请求图片的二进制数据
                img_data = requests.get(url=whole_src, headers=headers).content
                # 生成图片名称
                img_name = whole_src.split("/")[-1]
                # 图片存储的路径
                imgPath = "./nituLibs/"+img_name
                with open(imgPath, "wb") as fp:
                    fp.write(img_data)
                    print("下载成功!")
            except Exception as result:
                print("未知错误 %s" % result)

