import time

import requests
from lxml import etree
from lxml.etree import HTMLParser

from configure import settings




"""

百度新闻咨询爬虫

默认搜索"地产主题"

"""



class Baidu_crawler():

    Keywords = "地产"
    URLS = []
    Next_page = settings["BD_NEWS_URL"].format(Keywords = Keywords)

    def baidu_crawler(self):

        while(Baidu_crawler.Next_page):
            response = requests.get(Baidu_crawler.Next_page,headers = settings["HEADER"])
            print(response.status_code)

            yield self.parse(response.text)


    def parse(self,text):
        html = etree.HTML(text,HTMLParser())
        urls = html.xpath("//div[@class='result']/h3/a/@href")
        Baidu_crawler.URLS = Baidu_crawler.URLS+urls
        next_url = html.xpath("/html/body/div[1]/p[@id='page']/a[last()]")[0]
        next_url ,text2 = next_url.xpath("@href")[0],next_url.xpath("text()")[0]
        if next_url and text2 == "下一页>":
            next_url = "http://www.baidu.com"+ next_url
            Baidu_crawler.Next_page = next_url
            return urls
        else:
            Baidu_crawler.Next_page = None


    def get_url_num(self):
        print(len(Baidu_crawler.URLS))
        return len(Baidu_crawler.URLS)

    def get_urls(self):
        print(Baidu_crawler.URLS)
        return Baidu_crawler.URLS

    def download_html(self,url):
        html = requests.get(url)
        return html.status_code,html.text






if __name__ == '__main__':
    crawler = Baidu_crawler()
    for i in crawler.baidu_crawler():
        print(i)
        time.sleep(10)
        print('ok!')
    crawler.get_url_num()









