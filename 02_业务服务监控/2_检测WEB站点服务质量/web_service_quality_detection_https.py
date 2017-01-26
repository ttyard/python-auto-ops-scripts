# -*- coding: utf-8 -*-
import os,sys
import time
import sys
import pycurl
import certifi

#探测的目标URL
URL="https://www.baidu.com"
#探测一个curl对象
c = pycurl.Curl()
#定义请求的URL常量
c.setopt(pycurl.URL, URL)          
#连接超时时间,5秒
c.setopt(pycurl.CONNECTTIMEOUT, 5)
#使用certifi HTTPS SSL证书了验证
c.setopt(pycurl.CAINFO, certifi.where())


#下载超时时间,5秒
c.setopt(pycurl.TIMEOUT, 5)
#完成交付后强制断开连接，不重用
c.setopt(pycurl.FORBID_REUSE, 1)
#指定HTTP重定向的最大数为1
c.setopt(pycurl.MAXREDIRS, 1)
#屏蔽下载进度条
c.setopt(pycurl.NOPROGRESS, 1)
#设置保存DNS信息的时间为30s
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
#创建一个文件对象，已"WB"方式打开,用来存储方法的http头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content_SSL.txt", "wb")
#将返回的HTML内容重定向到indexfile文件对象
c.setopt(pycurl.WRITEHEADER, indexfile)
#将返回的HTML内容定向到indexfile文件对象
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()  #提交请求
except Exception,e:
    print "connecion error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME) #获取DNS解析时间
CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)  #获取建立连接时间
PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME) #获取从建立连接到准备传输所消耗的时间
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME) #获取从建立连接到开始传输消耗的时间
TOTAL_TIME = c.getinfo(c.TOTAL_TIME) #获取传输总时间
HTTP_CODE =  c.getinfo(c.HTTP_CODE) #获取HTTP状态码
SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD) #获取下载数据包大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE) #获取HTTP头部大小
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD) #获取平均下载速度

print "HTTP状态码：%s" %(HTTP_CODE)
print "DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000)
print "建立连接时间：%.2f ms" %(CONNECT_TIME*1000)
print "准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000)
print "传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000)
print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000)

print "下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD)
print "HTTP头部大小：%d byte" %(HEADER_SIZE)
print "平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD)

indexfile.close() #关闭文件
c.close() #Curl对象
