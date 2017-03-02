#coding=utf-8

import log
import datetime
import conf
import requests
import handlers
import fetcher

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
        print str
        print "parse item error !"
        exit(1)

    w["minute"] = arr[0]
    w["hour"] = arr[1]
    w["day"] = arr[2]
    w["url"] = arr[3]
    w["actions"] = arr[4]

    return w

def do_watch(item):
    if "url" in item and "actions" in item:
        if item["url"][0:4] == "http" :
            response = requests.get(item['url'])
            if response.status_code == 200 :
                content = response.text

        elif item["url"][0:5] == "fetch":
            f_items = item["url"][8:].split(".")
            if len(f_items) != 0 :
                fetcher_name = f_items.pop(0) 
                params = f_items
                content = fetcher.fetch(fetcher_name,params)
            else :
                content = False

        if False != content:
            names = item['actions'].split(",")
            for n in names:
                handlers.call(n,content)

    else :
        print "ITEM ERROR!"

def should_run(now,w):

    if int(w["minute"]) == -1 :
        return True

    flags = [True,True,True]

    flags[0] = (w["day"] == "*") or (int(w["day"]) == now.day)
    flags[1] = (w["hour"] == "*") or (int(w["hour"]) == now.hour)
    flags[2] = (w["minute"] == "*") or (int(w["minute"]) == now.minute)

    return flags[0] and flags[1] and flags[2]


def do_once():

    log.log("RUN BEGIN :")
    now = datetime.datetime.now()

    watches = conf.url.watches
    for item in watches:
        watch = parse_watch(item)
        if should_run(now,watch):
            do_watch(watch)


