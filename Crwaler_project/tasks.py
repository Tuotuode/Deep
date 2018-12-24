from Celery import app
import requests
from requests import exceptions


@app.task
def download(url):
    try:
        html = requests.get(url,timeout= 3)
        return (url,html.text)
    except (exceptions.ConnectionError,exceptions.Timeout) as e:
        return (url,str(e))


def on_result_ready(result):
    print('Received result for id %r' % (result.id))


if __name__ == '__main__':
    download("http://www.baidu.com")

