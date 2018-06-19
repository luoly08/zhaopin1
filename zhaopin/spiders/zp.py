# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from zhaopin.items import ZhaopinItem
import urllib.request
import re
class ZpSpider(scrapy.Spider):
    name = 'zp'
    allowed_domains = ['jobs.zhaopin.com']
    # start_urls = ['http://jobs.zhaopin.com/']
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

    }
    def start_requests(self):
        # for i in range(2,10):
        #     url='http://jobs.zhaopin.com/guangzhou/p'+str(i)
        #     yield Request(url=url,callback=self.parse,headers=self.headers)
        yield Request (url='http://jobs.zhaopin.com/guangzhou/', callback=self.parse, headers=self.headers)

    def parse(self, response):
        item=ZhaopinItem()
        name=response.xpath("//span[@class='post']/a/text()").extract()
        link = response.xpath ("//span[@class='post']/a/@href").extract ()
        company = response.xpath ("//span[@class='company_name']/a/text()").extract ()
        for j in range(0,len(link)):
            data=urllib.request.urlopen(link[j]).read().decode('utf-8','ignore')
            pat1='<li><span>职位月薪：</span><strong>(.*?)&nbsp;<a'
            money=re.compile(pat1,re.S).findall(data)
            pat2 = '<li><span>工作地点：</span><strong><a target="_blank" href=".*?">(.*?)</a>'
            location = re.compile (pat2, re.S).findall (data)
            item['money'] = money[0]
            item['location'] = location[0]
            item['name'] = name[j]
            item['link'] = link[j]
            item['company'] = company[j]
            yield item
        for i in range (2, 101):
            url = 'http://jobs.zhaopin.com/guangzhou/p' + str (i)
            print('正在爬取第'+ str(i)+'页')
            yield Request (url=url, callback=self.parse, headers=self.headers)