# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import datetime

date = f'{datetime.datetime.now().month}{datetime.datetime.now().year}'

class UaeRealesatePipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client[f'UAE_Prices_0{date}_2']

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.insert_one(item)
        return item
