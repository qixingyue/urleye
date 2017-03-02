#coding=utf-8

import datetime 
import color

def log(message):
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print "%s%s%s %s " % (color.green,now,color.end ,message)

def info():
    print """
*** %sUrleys%s Start Ok.
*** This is One framework run progreames based on urls and actions.
*** You can define some urls in conf/url.py like "minute hour url acions"
*** actions can be implode by "," like demo,redis or more 
*** that means that time will run get content from that url , then handler these contents by handlers defined .
""" % (color.green,color.end)


