#coding=utf-8

import datetime 
import color

def log(message):
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print "%s%s%s %s " % (color.green,now,color.end ,message)

def error(message):
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print "%s%s %s %s " % (color.red,now,message,color.end)

def info():
    print """
*** %sUrleys%s Start Ok.
*** This is One framework run progreames based on urls and actions.
*** You can define some urls in conf/url.py like "minute hour url acions"
*** Actions can be implode by "," like demo,redis or more 
*** That means that time will run get content from that url 
*** Then handler these contents by handlers defined .
*** Simple Run : %s python eye.py "fetch://baidu.com demo" %s
""" % (color.green,color.end,color.green,color.end)


