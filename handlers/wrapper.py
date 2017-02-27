#coding=utf-8


handlers = {}

def hander_method(fn):
	global handlers
	handlers[fn.__name__] = fn

def call(name,content):
	print name
	if name in handlers:
		handlers[name](content)


import demo
import mail
