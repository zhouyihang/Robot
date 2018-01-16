#coding:utf-8
from taobao import spider
import sys
import getopt

def Usage():
    print ('艾斯卡尔  taobao-spider 使用指南:')
    print ('    -h    --help:    显示帮助信息.')
    print ('    -v    --ver:    显示脚本版本')
    print ('    -k    --key:    搜索关键词，默认 iphone7')
    print ('    -n    --num:    搜索页数，每页包含44条商品数据，如输入2，那说明会抓取2*44条商品数据')
    print ('    -f    --file:    获取的文件保存位置，默认为D:\iphone.txt')
    print ('使用实例：')
    print ('python taobao.py -k 滑板鞋 -n 5 -f D:\huaban.txt')

def Version():
    print ('python-spider 1.0.0')
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'hvk:n:f:', ['help', 'version', 'key=', 'num=', 'file='])
    except getopt.GetoptError:
        Usage()
        sys.exit(2)
    key =""
    num =0
    fileName=""
    for o, a in opts:
        if o in ('-h', '--help'):
            Usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            Version()
            sys.exit(0)
        elif o in ('-k', '--key'):
            key=a
        elif o in ('-n', '--num'):
            num=int(a)
        elif o in ('-f', '--file'):
            fileName=a
        else:
            print ('unhandled option')
            sys.exit(3)
    spider(num,key,fileName)
if __name__ == '__main__':
    main(sys.argv)
