#coding=utf-8

import wrapper
import json

@wrapper.fetch_method
def csv(params):
    f_name = params[0] + ".csv"


