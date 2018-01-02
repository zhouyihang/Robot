from flask import Flask
from taobao import spider
application = Flask(__name__)

@application.route("/")
def hello():
    key ="nike"
    num =0
    fileName=""
    spider(num,key,fileName)
    return "Hello World!"

if __name__ == "__main__":
    application.run()
