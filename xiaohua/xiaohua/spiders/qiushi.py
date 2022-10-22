import scrapy
from ..items import XiaohuaItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.xhkong.com/tag/%E7%B3%97%E4%BA%8B']

    def parse(self, response):
        # # 解析: 段子标题+段子内容
        # list_article = response.xpath('//div[@class="content fix"]/section/article')
        # all_data = []  # 存储所有解析到的数据
        # for art in list_article:
        #     # xpath返回的是列表, 但是列表元素一定是Selector类型的对象
        #     # extrack可以将Selector对象中data参数存储的字符串提取出来
        #     title = art.xpath('./header/h2[1]/a/text()')[0].extract()
        #     content = art.xpath('./div/p/text()').extract_first()
        #     content = "".join(content)
        #     dic = {
        #         "title": title,
        #         "content": content
        #     }
        #     all_data.append(dic)
        # return all_data

        # 解析: 段子标题+段子内容
        list_article = response.xpath('//div[@class="content fix"]/section/article')
        all_data = []  # 存储所有解析到的数据
        for art in list_article:
            # xpath返回的是列表, 但是列表元素一定是Selector类型的对象
            # extrack可以将Selector对象中data参数存储的字符串提取出来
            title = art.xpath('./header/h2[1]/a/text()')[0].extract()
            content = art.xpath('./div/p/text()').extract_first()
            content = "".join(content)

            item = XiaohuaItem()
            item["title"] = title
            item["content"] = content

            yield item  # 将item提交给了管道
