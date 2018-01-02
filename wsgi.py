from flask import Flask
from taobao import spider
from threading import Thread
application = Flask(__name__)

@application.route("/")
def hello():
    key ="nike"
    num =0
    fileName=""
    thread = Thread(target = spider, args = (num,key,fileName))
    thread.start()
    thread.join()
#    spider(num,key,fileName)
    return "Hello World!"

if __name__ == "__main__":
    application.run()
