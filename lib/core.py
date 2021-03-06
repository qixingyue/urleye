#coding=utf-8

import log
import datetime
import conf
import requests
import handlers
import fetcher
import urlparse


# 你可以创建数据库，把这些存到数据库里
sql = """
CREATE TABLE `url_alarm` (
id int primary key auto_increment,
check_url varchar(128) not null default "",
actions varchar(127) not null default "",
minutes int not null default 1,
hours int not null default 0,
date int not null default 0,
ctime datetime default CURRENT_TIMESTAMP,
mtime datetime default CURRENT_TIMESTAMP
)
"""

def parse_watch(str):

    w = {}
    arr = str.split(" ")
    if len(arr) != 5 :
        log.log(str)
        log.log("parse item error !")
        exit(1)

    w["minute"] = arr[0]
    w["hour"] = arr[1]
    w["day"] = arr[2]
    w["url"] = arr[3]
    w["actions"] = arr[4]

    return w

def do_watch(item):
    if "url" in item and "actions" in item:

        parse_item = urlparse.urlparse(item['url'])

        scheme = parse_item.scheme

        if scheme == 'http':
            response = requests.get(item['url'])
            if response.status_code == 200:
                content = response.text
        elif scheme != "":
            content = fetcher.scheme_get(scheme,item['url'])
        else :
            content = False

        if False != content:
            names = item['actions'].split(",")
            for n in names:
                handlers.call(n,content)
        else:
            log.error("No Content find from : %s " % ( item['url']))

    else :
        log.error("ITEM ERROR!")

def should_run(now,w):

    if int(w["minute"]) == -1 :
        return True

    flags = [True,True,True]

    flags[0] = (w["day"] == "*") or (int(w["day"]) == now.day)
    flags[1] = (w["hour"] == "*") or (int(w["hour"]) == now.hour)
    flags[2] = (w["minute"] == "*") or (int(w["minute"]) == now.minute)

    return flags[0] and flags[1] and flags[2]


def simple_do(item):
    """
    Only contains item and actions like this :
    http://baidu.com demo
    """
    arr = item.split(" ")
    if len(arr) != 2 :
        log.error("item invalid %s" % (item)) 
        exit(1)
    i = {"url":arr[0],"actions":arr[1]}
    do_watch(i)

def do_once():

    log.log("RUN BEGIN :")
    now = datetime.datetime.now()

    watches = conf.url.watches
    for item in watches:
        watch = parse_watch(item)
        if should_run(now,watch):
            do_watch(watch)


def info():
    log.info()

