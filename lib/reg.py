#coding=utf-8

import re

#o = re.findall(r"(www)\.([a-z]+)\.([a-z]+)","www.baidu.com")
#return [('www', 'baidu', 'com')]
#[1,2,3]["a","b","c"]
#
def findContent(reg,content,indexNames):
    o = re.findall(reg,content)
    if len(o) == 0 :
        return []
    else:
        result = []
        for x in o:
            item = {}
            for i in range(0,len(indexNames[0])):
                index = indexNames[0][i]
                name = indexNames[1][i]
                item[name] = x[index]
            result.append(item)
        return result

if __name__ == "__main__":
    print findContent(r"([abc]+)one([bcd]+)two","aaabbcconebbbccddtwo",[[0,1],["title","content"]])
