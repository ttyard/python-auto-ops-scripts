# Python与系统安全

## 1.构建集中式的病毒扫描机制

  Clam AntVirue(ClamAV)是一款免费开源的防病毒软件,软件与病毒库更新皆有社区免费发布.目前ClamAV提供Linux/Unix的发现版本，提供病毒查杀、病毒扫描等服务。pyClamd(http://xael.org/norman/ppython/pyclamd)是一个Python第三方模块，可以让Python直接使用ClamAV病毒扫描守护进程clamd来实现搞下的病毒检测功能。另外，pyClamd模块也非常容易整合到我们已有的平台当中。
  
  yum install -y clamav clamd clamav-update
  chkconfig --levels 234 clamd on
  /usr/bin/freshclam
  setenforce 0 
  
  更新守护进程监听IP配置文件，根据不同环境自行修改监听的IP。
  sed -i -e '/^TCPADDR/{ s/127.0.0.1/0.0.0.0/;}' /etc/clamd.conf
  /etc/init.d/clamd start 
  
### 常用模块常用方法
  
pyClamad提供了两个关键类，一个为ClamdNetworkSocket()类，实现使用网络套接字操作clamd；另一个为ClamdUnixSocket()类，实现使用Unix套接字类操作clamd.两个类定义的方法完全一样。

__init__(self,host='127.0.0.1',port=3310,timeout=None)方法，是ClamdNetworkSocket类的初始化方法，host为连接主机IP；port为连接端口号，默认端口号是3310

contscan_file(self,file) 方法，实现扫描指定的文件或目录，在扫描时发生错误或发现病毒将不终止，file为指定的文件或目录的绝对路径。

multiscan_file(self,file),实现多线程扫描指定的文件或目录，多核环境速度更快，在扫描时发生错误或发现病毒将不终止，file为指定的文件或目录的绝对路径

scan_file(self,file),实现扫描指定的文件或目录，在扫描发生错误或发现病毒时终止。

shutdown(self),强制关闭clamd进程并退出

stats(self),获取Clamscan当前状态。

reload(self),强制重载clamd病毒特征库，扫描前建议reload操作

EICAR(self),返回EICAR测试字符串，即生成具有病毒特征的字符串，便于测试。


