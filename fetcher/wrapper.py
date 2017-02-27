#coding=utf-8


fetchers = {}

def fetch_method(fn):
	global fetchers 
	fetchers[fn.__name__] = fn

def fetch(name,params):
	global fetchers
	if name in fetchers:
		return fetchers[name](params)
	else :
		return False


import baidu
