#coding=utf-8

import wrapper
import json

@wrapper.fetch_object
class baidu:

    name = "baidu"

    def __init__(self):
        pass

    def scheme_get(self,url):
        x = [
            {"subject":"Hi world","content":"My name is world","toemail":"xingyue@staff.sina.com.cn"}			
        ]
        return json.dumps(x)

    def scheme_set(self,url):
        pass

