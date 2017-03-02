#!/data0/python27/bin/python
#coding=utf-8

import lib.core
import sys

if __name__ == "__main__":
    i = len(sys.argv)
    if i > 1:
        arr = sys.argv[1].split(" ")
        lib.core.simple_do(sys.argv[1])
        lib.core.do_watch({"url":arr[0],"actions":arr[1]})
        exit()
    lib.core.do_once()

