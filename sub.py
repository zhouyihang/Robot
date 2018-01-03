from taobao import spider

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
