#coding=utf-8
#http://www.37zw.com/6/6340/
import urllib2
import re
from bs4 import BeautifulSoup
import time
import html5lib
from django.shortcuts import render
from django.http import HttpResponse

send_headers = {
	 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	 'Connection':'keep-alive'
	}
headUrl = ""
reopenTimes = 0
num = 1

def index(request):
	return render(request, 'books.html')

def geturl(request):
	return render(request, 'geturl.html')

def getbook(request):
    _url = request.GET['url']
    global headUrl
    html = getHtml(_url)
    soup = BeautifulSoup(html,'html5lib')
    nextChapter = _url
    
    if("html" in nextChapter):
        temp = soup.find("div",attrs={"class":"bottem1"}).find_all("a")
        nextChapter = temp[2].get('href')
        print nextChapter
        getBook(nextChapter)
    else:
        headUrl = _url
        temp = soup.find(id="list").find_all("a")
        nextChapter = headUrl+temp[0].get('href')
        name = soup.find(id="info").find("h1")
        fp = open('downloads/'+name.text+'.txt','w')
        fp.close
        f = open('downloads/'+name.text+'.txt','a')
        f.write("《"+name.text.encode('utf-8')+"》\n\n")

    getChapter(nextChapter,f)
    f.close
    print 'download success,timeout '+str(reopenTimes)+' times'

def getChapter(_url,fl):    
    while("html" in _url and "index.html" not in _url):
        global num
        html = getHtml(_url)
        soup = BeautifulSoup(html,'html5lib')
        title = soup.find_all("h1")
        texts = soup.find(id="content")
        if not texts:
            continue
        content = texts.text.encode('utf-8')
        content = content.replace('[三七中文 www.37zw.com]百度搜索“37zw.com”', '')
        content = content.replace('    [三七中文手机版 m.37zw.com]', '')
        content = content.replace('    （未完待续）', '')
        content = content.replace('(未完待续。)', '')
        content = content.replace('    ','\n    ')
        fl.write(title[0].text.encode('utf-8')+'\n')
        fl.write(content)
        fl.write('\n\n\n')
        print str(num)+"  "+_url
        num+=1
        temp = soup.find("div",attrs={"class":"bottem1"}).find_all("a")
        _url = headUrl+temp[3].get('href')

def getHtml(url):
    req = urllib2.Request(url,headers=send_headers)
    try:
        page = urllib2.urlopen(req,timeout=4)
        time.sleep(0.2)
        html = page.read()
    except Exception,e:
        global reopenTimes
        print "timeout"
        html = getHtml(url)
        reopenTimes += 1
        
    return html
# Create your views here.
