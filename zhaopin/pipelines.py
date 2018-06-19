# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


# class ZhaopinPipeline (object):
#     def __init__(self):
#         self.fh = open ("G:/zhaopin.txt", "w")
#
#     def process_item(self, item, spider):
#         print (item["name"])
#         print (item["link"])
#         print (item["company"])
#         print (item["money"])
#         print (item["location"])
#
#         print ("--------")
#         # self.fh.write (item["name"][0] + "\n" + item["link"][0] + "\n" + item["company"][0] + "\n" + item["money"][0] + "\n"+ item["location"][0] + "\n"+ "--------" + "\n")
#         self.fh.write (
#             item["name"] + "\n" + item["link"] + "\n" + item["company"] + "\n" + item["money"] + "\n" +
#             item["location"]+ "\n" + "--------" + "\n")
#
#         return item
#
#     def close_spider(self):
#         self.fh.close ()





class ZhaopinPipeline (object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host='127.0.0.1',user='root',passwd='12345678',db='zhaopin',charset='utf8')
        sql = "insert into zp(name,link,company,money,location) values('" + item["name"] + "','" + item["link"] + "','" + item["company"] + "','" + item["money"] + "','" + item["location"] + "')"
        conn.query (sql)
        print ('正在写入数据库')
        conn.commit ()
        conn.close ()
        print ('写入数据库成功')
        return item