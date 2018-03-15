import urllib.request
f=urllib.request.urlopen('http://www.baidu.com/')
f.read(500)
f.read(500).decode('utf-8')
