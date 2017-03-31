#coding=utf-8

import lib.log


handlers = {}

def hander_method(fn):
    global handlers
    handlers[fn.__name__] = fn

def call(name,content):
    if name in handlers:
        handlers[name](content)
    else :
        lib.log.log( "No handler named : %s " % (name) )


def trace(content):
    print content

handlers['trace'] = trace

import demo
import mail
import redis
