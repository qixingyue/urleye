#coding=utf-8

import wrapper
import lib.mail
import lib.log

@wrapper.hander_method
def demo(content):
    lib.log.log(content)
    pass
