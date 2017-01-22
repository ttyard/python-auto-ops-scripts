#!/usr/bin/env python
import dns.resolver
import os
import httplib

#域名IP列表清单
iplist=[]
appdomain="www.baidu.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception,e:
        print "DNS resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True
    
def checkip(ip):
    checkurl=ip+"80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)
    
    try:
        conn.request("GET","/",headers = {"Host": appdomain})
        r=conn.getresponse()
        getcontent = r.read(15)
    finally:
        if getcontent=="<?doctype html>":
            print ip+"[OK]"
        else:
            print ip+"[Error]"


if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."
        