#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pyclamd
from threading import Thread

class Scan(Thread):

    def __init__ (self,IP,scan_type,file):
        """构造方法"""
        Thread.__init__(self)
        self.IP = IP
        self.scan_type=scan_type
        self.file = file
        self.connstr=""
        self.scanresult=""


    def run(self):
        """多进程run方法"""

        try:
            cd = pyclamd.ClamdNetworkSocket(self.IP,3310) #创建socket连接对象
            if cd.ping(): #探测连通性
                self.connstr=self.IP+" connection [OK]"
                cd.reload() #重载clamd病毒库，建议更新病毒后做relaod()操作
                if self.scan_type=="contscan_file":#选择不同的扫描模式
                    self.scanresult="{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type=="multiscan_file":
                    self.scanresult="{0}\n".format(cd.multiscan_file(self.file))
                elif self.scan_type=="scan_file":
                    self.scanresult="{0}\n".format(cd.scan_file(self.file))
                time.sleep(1) #线程挂起1s
            else:
                self.connstr=self.IP+" ping error,exit"
                return
        except Exception,e:
            self.connstr=self.IP+" "+str(e)


IPs=['192.168.1.21','192.168.1.22'] #扫描的足迹列表
scantype="multiscan_file" #指定扫描模式
scanfile="/data/www" #指定扫描路径
i=1
threadnum=2 #指定启动的线程数
scanlist = [] #存储扫描scan类线程对象列表

for ip in IPs:

    currp = Scan(ip,scantype,scanfile) # 创建扫描Scan类对象，参数(IP,扫描模式,扫描路径)
    scanlist.append(currp) #追加最先到列表

    if i%threadnum==0 or i==len(IPs): #当达到指定的线程数或IP列表数后启动、退出线程
        for task in scanlist:
            task.start() #启动线程

        for task in scanlist:
            task.join() #等待所有子线程退出，并输出扫描结果
            print task.connstr #大约服务器连接信息
            print task.scanresult #打印扫描结果
        scanlist = []   
    i+=1