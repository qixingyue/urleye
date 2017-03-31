#coding=utf-8

import lib.log

fetchers = {}

def fetch_object(cla):
    global fetchers
    fetchers[cla.name] = cla

def scheme_get(name,url):
    global fetchers
    if name in fetchers:
        return fetchers[name]().scheme_get(url)
    else :
        lib.log.error("No scheme named %s " % (name))
        return False

import baidu
