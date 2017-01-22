#!/usr/bin/env python
import psutil

##1.获取CPU使用信息
psutil.cpu_times()
#scputimes(user=457.23, nice=176.16, system=277.84, idle=58334.32, iowait=1844.72, irq=0.0, softirq=6.72, steal=0.0, guest=0.0, guest_nice=0.0)

#User Time: 执行用户进程的时间百分比; 
psutil.cpu_times().user
#System Time: 执行内核进程和中断的时间百分比; 
psutil.cpu_times().system
#Wait IOError: 由于IO等待而使CPU处于idle(空闲)状态的时间百分比; 
psutil.cpu_times().iowait
#Idle: CPU处于Idel状态的时间百分比; 
psutil.cpu_times().idle
#cpu_times() 方法获取CPU完整信息，若要显示所有逻辑CPU信息指定percpu=True,即 
psutil.cpu_times(percpu=True)

##2.获取内存信息
psutil.virtual_memory()
#svmem(total=2089529344, available=1466224640, percent=29.8, used=430063616, free=226299904, active=725094400, inactive=792035328, buffers=603623424, cached=829542400, shared=20250624)
#Total: 内存总数 
psutil.virtual_memory().total
#userd: 已使用的内存数
psutil.virtual_memory().used
#free: 空闲内参数
psutil.virtual_memory().free
#buffers: 缓冲使用数
psutil.virtual_memory().buffers
#cache: 缓存使用数
psutil.virtual_memory().cached

##swap: 交换分区使用数
psutil.swap_memory()
#sswap(total=4294963200, used=368226304, free=3926736896, percent=8.6, sin=10403840, sout=374460416)

##3.磁盘信息
#在系统磁盘信息重点关注磁盘的利用率及IO信息
#获取完整的磁盘分区与挂载点
psutil.disk_partitions()
# [sdiskpart(device='/dev/mapper/lvm-root', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro')]
#获取磁盘分区的使用情况
psutil.disk_usage('/')
#sdiskusage(total=279710154752, used=230977331200, free=34500714496, percent=87.0)
#获取硬盘总的IO个数、读写信息,获取单个分区使用 perdisk=True 参数
psutil.disk_io_counters()
#sdiskio(read_count=394445, write_count=533637, read_bytes=4349835264, write_bytes=6614347776, read_time=4118176, write_time=66844380, read_merged_count=2774, write_merged_count=282135, busy_time=2908032)

##4.获取网络信息
psutil.net_io_counters()
#snetio(bytes_sent=51353071, bytes_recv=288323514, packets_sent=336323, packets_recv=317673, errin=0, errout=0, dropin=0, dropout=0)

##5.其他系统信息
#获取当前登录系统的用户信息
psutil.users()
#获取开机时间，默认返回Linux时间戳
psutil.boot_time()
datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")