from tools import Baidu_crawler
from tasks import download,on_result_ready
import time
from celery.result import AsyncResult as asy
from Celery import app
import requests


# collections = MongoClient_connection()

def test():
    c = Baidu_crawler()
    for i in c.baidu_crawler():
        if i:
            for url in i:
                result = download.delay(url)
                if result.ready():
                    url,html = result.get()
                    print(url)
                    collections.insert(result.id,url,html)

                time.sleep(5)
def test2():
    n = 0
    tasks = []
    c = Baidu_crawler()
    urls = c.baidu_crawler()

    for url_list in urls:
        if url_list:
            for url in url_list:
                result = download.delay(url)
                print(result.task_id)
                tasks.append(result.id)

    print(len(tasks))
    time.sleep(60)

    for i in tasks:
        if test3(i):
            n +=1
    print(n)




def test3(id):
    c = asy(id=id,backend=app.backend,app=app)
    if c.ready():
        url, html = c.get()
        collections.insert({"work_id": result.id, "url": url, "html": html})
        print(url)
        return True
    else:
        print("===>abandont")
        return False


if __name__ == '__main__':
    test2()
