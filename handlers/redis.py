#coding=utf-8

import wrapper
import redis
import lib.log

@wrapper.hander_method
def redis(items):
    lib.log.log("redis handler %s " % (items))
    passed = []
    for item in items:
        ip   = item[0]
        port = item[1]
        id_str = ip + "_" + port
        if id_str in passed:
            continue
        lib.log.log("Test %s " % (item))
        
        try:
            r = redis.StrictRedis(host=ip, port=port,socket_timeout=2)
            k = "_______A"
            r.set(k,"B")
            if "B" == r.get(k):
                lib.log.log("XX : %s" % (id_str))
        except Exception,e:
            lib.log.log(e)

