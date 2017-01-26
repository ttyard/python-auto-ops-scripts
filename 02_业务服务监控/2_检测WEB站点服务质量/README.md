# 使用pycurl探测WEB服务质量

## 模块常用方法说明
pycurl.Curl()类实现创建一个libcurl包的Curl句柄对象，无参数。

更多使用说明详见 http://curl.haxx.se/libcurl/c/libcurl-tutorial.html

下面介绍Curl对象几个常用的方法。
close(): 对应libcurl包中的curl_easy_cleanup方法，无参数，实现关闭、回收Curl对象。

perform(): 对应libcurl包中的curl_easy_perform方法，无参数，实现Curl对象请求的提交。

setopt(option,value): 对应libcurl包中的curl_easy_setopt方法，参数option通过libcurl的常量来指定，参数value的值会依赖option，可以是一个字符串、整型、长整型、文件对象、列表或函数等。

下面列举常用的常量列表：

c = pycurl.Curl() #创建一个curl对象

c.setopt(pycurl.CONNECTTIMEOUT, 5) #连接的等待时间，设置为0则屏蔽

c.setopt(pycurl.TIMEOUT, 5) #请求超时时间

c.setopt(pycurl.NOPROGRESS, 0) #是否屏蔽下载进度条，非0屏蔽

c.setopt(pycurl.MAXREDIRS, 5) #指定HTTP重定向的最大数

c.setopt(pycurl.FORBID_REUSE, 1) #完成交付后强制断开连接，不重用

c.setopt(pycurl.FRESH_CONNECT, 1) #强制获取新的连接，即替代缓存中的连接

c.setopt(pycurl.DNS_CACHE_TIMEOUT, 60) #设置保存DNS信息的时间，默认为120s

c.setopt(pycurl.URL,"http://www.baidu.com") #指定请求的URL

c.setopt(pycurl.USERAGENT,"mOZILLA/5.2 (Compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)") #配置请求HTTP头的User-Agent

c.setopt(pycurl.HEADERFUNCTION, getheader) # 将返回的HTTP HEADER指向到回调函数getheader

c.setopt(pycurl.WRITEFUNCTION, getbody) #将返回的内容重定向到回调函数getbody

c.setopt(pycurl.WRITEHEADER, fileobj) #将返回的HTTP HEADER 定向到fileobj文件对象

c.setopt(pycurl.WRITEDATA, fileobj) #将返回的HTML内容定向到fileobj文件对象

getinfo(option)方法，对应libcurl包中的curl_easy_getinfo方法，参数option是通过libcurl的常量来指定的。下面列举的常量列表：

c = pycurl.Curl() #创建一个curl对象

c.getinfo(pycurl.HTTP_CODE) #返回的HTTP状态码

c.getinfo(pycurl.TOTAL_TIME) #传输结束所消耗的总时间

c.getinfo(pycurl.NAMELOOKUP_TIME) #DNS解析所消耗的总时间

c.getinfo(pycurl.CONNECT_TIME) #建立连接所消耗的总时间

c.getinfo(pycurl.PRETRANSFER_TIME) #从建立连接到准备传输所消耗的时间

c.getinfo(pycurl.STARTRANSFER_TIME)#从建立连接到开始传输所消耗的时间

c.getinfo(pycurl.REDIRECT_TIME)#重定向所消耗的时间

c.getinfo(pycurl.SIZE_UPLOAD)#上传数据包大小

c.getinfo(pycurl.SIZE_DOWNLOAD)#下载数据包大小

c.getinfo(pycurl.SPEED_DOWNLOAD)#平均下载速度

c.getinfo(pycurl.SPEED_UPLOAD) #平均上传速度

c.getinfo(pycurl.HEADER_SIZE) #HTTP头部大小


