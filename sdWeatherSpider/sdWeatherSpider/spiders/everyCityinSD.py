# -*- coding: utf-8 -*-
import scrapy
from urllib.request import urlopen
from sdWeatherSpider.items import SdweatherspiderItem
import re


class EverycityinsdSpider(scrapy.Spider):
    name = 'everyCityinSD'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/fujian/index.shtml']

    def parse(self, response):
        # 处理每个城市的天气预报页面数据
        item = SdweatherspiderItem()

        citys=[]
        weather=[]
        selector = response.xpath('//div[@class="forecastBox"]')
        for dl in selector.xpath('./dl'):
            city = dl.xpath('./dt//a//text()').extract()[0]
            tem=dl.xpath('./dd//a//text()').extract()[0]
            citys.append(city)
            weather.append(tem)
        # 存放天气数据

        item['city'] = citys
        item['weather'] = weather



        return [item]
        pass

