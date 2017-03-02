#coding=utf-8

import wrapper
import json

@wrapper.fetch_method
def baidu(params):
	x = [
			{"subject":"Hi world","content":"My name is world","toemail":"xingyue@staff.sina.com.cn"}			
	]
	return json.dumps(x)

