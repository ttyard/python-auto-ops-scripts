#!/usr/bin/env python
import pexpect
import sys

#在Linux系统集群运营中,经常需要批量远程执行Linux命令,并双向同步文件的操作
#脚本使用spawn()方法来实现ssh,scp命令的

ip="192.168.1.21" #定义目标主机
user="root" #用户名
passwd="H6DSY#*$df32" #密码
target_file="/data/logs/nginx_access.log" #目标主机的文件目录

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip]) #运行ssh命令
fout = file('mylog.txt','w') #输入/输出日志写入mylog.txt文件
child.logfile = fout

try:
    child.expect('(?i)password') #匹配password字符串,(?i) 表示不区分大小写
    child.sendline(passwd) 
    child.expect('#')
    child.sendline('tar -czf /data/nginx_access.tar.gz '+target_file) #打包日志文件
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF: #定义EOF处理异常
    print "expect EOF"
except TIMEOUT: #定义Timeout处理异常
    print "expect TIMEOUT"

#使用scp远程Copy打包好的文件到/home目录
child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/data/nginx_access.tar.gz','/home']) 
fout = file('mylog.txt','a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF) #匹配缓存区EOF(结尾),保证文件复制正常完成
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"
