# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SdweatherspiderPipeline(object):
    def process_item(self, item, spider):
        with open('weather.txt','a',encoding='utf8') as fp:
            for i in range(len(item['city'])):
                fp.write(item['city'][i]+' ')
                fp.write(item['weather'][i]+'\n')
        return item