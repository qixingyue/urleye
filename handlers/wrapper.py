#coding=utf-8


handlers = {}

def hander_method(fn):
	global handlers
	handlers[fn.__name__] = fn

def call(name,content):
	if name in handlers:
		handlers[name](content)
    else :
        print "No handler named : %s " % (name)


import demo
import mail
import redis
