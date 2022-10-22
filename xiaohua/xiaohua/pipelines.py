# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XiaohuaPipeline(object):
    fp = None

    # 重写父类的一个方法: 该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print("开始爬虫...")
        self.fp = open("./qiushi.txt", "w", encoding='utf-8')
    # 专门用来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接受到一个item就会被调用一次

    def process_item(self, item, spider):
        title = item["title"]
        content = item["content"]
        self.fp.write(title+'\n'+content+'\n')
        return item

    # 重写父类的一个方法: 该方法只在爬虫结束的时候被调用一次
    def close_spider(self, spider):
        print("结束爬虫!")
        self.fp.close()


# 管道文件中一个管道类对应将一组数据存储到一个平台或载体中
class MysqlPipeline(object):
    pass