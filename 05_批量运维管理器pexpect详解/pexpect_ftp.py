#!/usr/bin/env python
#
#使用pexpect的spawnu()方法执行FTP命令
#通过expect()方法定义匹配的输出规则
#sendline()方法执行相关FTP交付命令
#
from __future__ import unicode_literals

import pexpect
import sys

child = pexpect.spawnu('ftp ftp.openbsd.org') #运行FTP命令
child.expect('(?i)name .*: ') #(?i)表示后面的字符串正则匹配忽略大小写
child.sendline('anonymous') # 输入FTP账号
child.expect('(?i)password') # 匹配密码的提示
child.sendline('pexpect@sourceforge.net') #输入ftp密码
child.expect('ftp> ') 
child.sendline('bin') #启用二进制方式传输
child.expect('ftp> ')
child.sendline('get robots.txt') #下载robots.txt
child.expect('ftp> ')
sys.stdout.write (child.before) #输出匹配 "ftp> "之前的输入/输出
print("Escape character is '^]'.\n")
sys.stdout.write (child.after)
sys.stdout.flush()
child.interact() # 调用interact让出控制权,用户可以继续当前会话手工控制子程序,默认输入 ^] 提示符 跳出
child.sendline('bye')
child.close()
