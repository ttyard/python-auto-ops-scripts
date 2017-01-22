#!/usr/bin/env python
import difflib
import sys

try:
    nginx_conf_1=sys.argv[1]   
    nginx_conf_2=sys.argv[2]

except Exception,e:
    print "Error:"+str(e)
    print "Usage: diff_two_nginx_conf_html.py filename1 filename2"
    sys.exit()
    
def readfile(filename):
    try:
        fileHandle = open (filename,'rb')
        text=fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print ('Read file Error:'+str(error))
        sys.exit()

if nginx_conf_1=="" or nginx_conf_2=="":
    print "Usage: diff_two_nginx_conf_html.py filename1 filename2"
    sys.exit()

nginx_conf_1_lines = readfile(nginx_conf_1)
nginx_conf_2_lines = readfile(nginx_conf_2)

d=difflib.HtmlDiff()
print d.make_file(nginx_conf_1_lines,nginx_conf_2_lines)