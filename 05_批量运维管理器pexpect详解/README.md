# 系统批量运维管理器pexpect详解

pexpect是Linux下expect的Python封装，通关pexpect我们可以实现对ssh,ftp,passwd,telnet等命令进行自动交互，而无需人工干涉来达到自动化的目的。

pexpect官方网站，参考 https://pexpect.readthedocs.io/en/stable/

## 1.安装pexpect

pexpect作为Python的一个普通模块，支持pip,easy_install方式安装。

pip install pexpect  或  easy_install pexpect

## 2.pexpect的核心组件

下面主要介绍几个核心组件：spawn、run、pxssh

### 2.1 spawn类

spawn是 pexpect的主要接口，用于启动或控制子应用程序，以下是他的构造函数定义：

class pexpect.spawn(command, args=[], timeout=30, maxread=200, searchwindowssiz=None, logfile=None, cwd=None, env=None, ignore_sighup=True)

command: 可以是任意已知的系统命令，如：

child = pexpect.spawn('/usr/bin/ftp') #启动FTP客户端

child = pexpect.spawn('/usr/bin/ssh user@wanglijie.cn') #启动ssh远程连接命令

当子程序需要参数时，还可以使用Python列表来替代参数项：

child = pexpect.spawn('/usr/bin/ftp', [])

child = pexpect.spawn('/usr/bin/ssh', ['user@wanglijie.cn'])

child = pexpect.spawn('ls', [-latr], ['/tmp'])

timeout: 等待结果的超时时间

maxread: pexpect从终端控制台一次读取的最大字节数

searchwindowssize: 匹配缓存区字符串的位置，默认是从开始位置匹配

需要注意： pexpect不会解析shell命令中的元字符，包括重定向 >, 管道 | 或 * 号，当然可以通过将存在这三种字符的命令作为/bin/bash参数进行调用：
```
child = pexpect.spawn('/bin/bash -c "ls -l | grep LOG > logs.txt"')

child.expect(pexpect.EOF)
```

我也也可以通过将命令的参数以Python列表的形式进行替换，从而使我们的语法变得更加清晰。

shell_cmd = 'ls -l |grep LOG > logs.txt'

child = pexpect.spawn('/bin/bash',['-c', shell_cmd])

child = expect(pexpect.EOF)

有时候调试代码需要pexpect获取输入输出信息，以便于了解匹配的情况。pexpect提供了两种途径，一种为写到日志文件，另一种为输出到标准输出。

写到日志文件的方式实现如下：

child = pexpect.spawn('some_command')

fout = file ('mylog.txt','w')

child.logfile = fout

输出到标准输出的方法实现如下：

child = pexpect.spawn('some_command')

child.logfile = sys.stdout

下面的例子，完整实现远程ssh登录，并显示/home目录文件清单,并通过日志文件记录所有的输入与输出.
```
import pexpect
import sys
child = pexpect.spawn('ssh pactera@10.12.49.153')
fout = file('mylog.txt','w')
#child.logfile = sys.stdout

child.expect("password:")
child.sendline("pactera")
child.expect('#')
child.sendline('ls /home')
child.expect('#')
```
以下为mylog.txt日志内容，可以看到pexpect产生的全部输入与输出信息

(1)expect方法

定义了一个子程序输出的匹配规则.

expect[pattern,timeout=-1,searchwindowssize=-1]

pattern表示字符串、pattern.EOF指向缓存区尾部(无匹配项)、expect.TIMEOUT匹配等待超时、正则表达式或者前面四种类型的列表List。当pattern为一个列表时，且不止一个表列元素被匹配，则返回的结果是子程序输出最先出现的那个元素，或者是列表最左边的元素(最小索引ID)

timeout指定匹配结果超时时间，单位为秒(s)。当超时被触发时，expect将匹配到pexpect.TIMEOUT

searchwindowssize 匹配缓存区字符串的位置，默认从开始位置开始匹配

当pexpect.EOF、pexpect.TIMEOUT、作为expect的列表参数时，匹配时间返回所处列表中的索引ID。

expect方法有两个非常棒的成员：before与after.befor成员保存了最近匹配成功之前的内容。after成员保存最近匹配成功之后的内容。

(2)read方法

下面这些输入方法的作用都是向子程序发送响应命令，可以理解成代替了我们的标准输入键盘。

send(self, s) #发送命令，不回车

sendline(self, s='') #发送命令，回车

sendcontrol(self, char) #发送控制字符，如child.sendcontrol('c') 等价于 ctrl+c

sendeof() #发送EOF

## 2.2 run函数

run是使用pexpect进行封装的调用外部命令的函数，类似于os.system或os.popen。不同的是使用run()可以获得命令的输出结果及命令的退出状态。

函数定义: pexpect.run(command, timeout=-1, withexitstatus=False, events=None, extra_args=None, logfile=None, cwd=None, env=None)

command:系统已知的任意命令，如没有写绝对路径时将会尝试搜索命令的路径。

event: 是一个字典，定义expect及sendline方法的对应关系

下面是spawn方式的示例：

from pexpect import *
child = spawn('scp foo user@example.com:.')
child.expect('(?i)password')
child.sendline(mypassword)

使用fun函数实现上面的内容：

from pexpect import *
run('scp foo user@example.com:.', events={'(?i)password': mypassword})

## 2.3 pxssh 类

pxssh是pexpect的派生类，针对在ssh会话操作上再做一层封装，提供与基类更加直接的操作方法。

pxssh类定义： class pexpect.pxssh.pxssh(timeout=30, maxread=200, searchwindowssize=None, logfile=None, cwd=None, env=None)

pxssh常用的三个方法如下：

login() #建立ssh连接

logout() #断开连接

prompt() #等待系统提示符，用于等待命令执行结束


