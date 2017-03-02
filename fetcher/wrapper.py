#coding=utf-8

import lib.log

fetchers = {}

def fetch_method(fn):
    global fetchers 
    fetchers[fn.__name__] = fn

def fetch(name,params):
    global fetchers
    if name in fetchers:
        return fetchers[name](params)
    else :
        lib.log.log("No fetcher named %s " % (name))
        return False

import baidu
