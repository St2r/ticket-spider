# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json


class CorePipeline:
    def __init__(self):
        # python3保存文件 必须需要'wb' 保存为json格式
        self.f = open("result.json", 'wb')
        self.item_list = []

    def process_item(self, item, spider):
        # 读取item中的数据 并换行处理
        self.item_list.append(dict(item))
        return item

    def close_spider(self, spider):
        # 关闭文件
        content = json.dumps(self.item_list, ensure_ascii=False, indent=1)
        self.f.write(content.encode('utf-8'))
        self.f.close()
