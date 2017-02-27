#coding=utf-8

import datetime 

def log(message):
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print "%s %s " % (now, message)
