#coding=utf-8

import wrapper
import redis

@wrapper.hander_method
def redis(items):
    print "redis handler " + item
    passed = []
    for item in items:
        ip   = item[0]
        port = item[1]
        id_str = ip + "_" + port
        if id_str in passed:
            continue
        print "Test " + item
        
        try:
            r = redis.StrictRedis(host=ip, port=port,socket_timeout=2)
            k = "_______A"
            r.set(k,"B")
            if "B" == r.get(k):
                print "XX : %s " % (id_str)
        except Exception,e:
            print e





