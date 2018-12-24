from celery import Celery

from configure import settings

broker="amqp://{}:{}@{}:5672/{}".format(settings["username"],settings["password"],settings["host"],settings["vhost"])
backend_ = "redis://localhost:6379/2"

app = Celery('tasks',broker=broker,backend=broker)

if __name__ == '__main__':

    print("vgjvjghvjgvjv")
    print(app.backend)
    app.start()
