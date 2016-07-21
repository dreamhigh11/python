
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re


def open(a):  #打开每个新闻详情网页
    for i in a:


        url= 'http://www.acgdoge.net'+i
        req = urllib2.Request(url)
        data = urllib2.urlopen(req)
        data1=data.read()
        title=re.compile(r'<title>(.*) \| ACGdoge</title>')#标题匹配

        describe=re.compile(r'<meta name="description" content="(.*)" />')#描述匹配
        content=re.compile(r'<p>(.*|.*\n)<span id="more-\d*"></span></p>')
        passage=re.compile(r'<p>(.*?)[^>]</p>')
        result = re.findall(title,data1)
        t=result[0]
        result1=re.findall(describe,data1)
        d=result1[0]
        result2=re.findall(content,data1)
        c=result2[0]
        result3=re.findall(passage,data1)
        for p in result3:
            print p




page = 1
url = 'http://www.acgdoge.net/page/'+str(page)#网页地址


req = urllib2.Request(url)
data = urllib2.urlopen(req)



data1=data.read()
#content= data1.decode('utf-8')
pattern = re.compile(r'<a href="http://www\.acgdoge\.net(.*)" class="more-link">Read More →</a></p>')
    #匹配规则，含有上式形式，并其中一段以http://www/acgdoge.net开头

#relink = '<a href="(.*?)" class="more-link">Read More →</a></p>'
result1 = re.findall(pattern,data1)
#source='<a href="http://www.acgdoge.net/archives/10547#more-10547" class="more-link">Read More →</a></p>'
#urllll=re.findall(relink,data1,re.I)
#for result in urllll:
#    print result
jieguo=[]
for result in result1:#循环将匹配结果传给列表

    jieguo.append(result)
    #print 'http://www.acgdoge.net'+result
#for i in jieguo:
#        print 'http://www.acgdoge.net'+i

open(jieguo)