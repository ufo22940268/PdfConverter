#coding:utf-8
import re
import codecs
import json
from json import JSONEncoder

def parseToBlocks(fileName):
    blocks = set();
    with codecs.open(fileName, "r",  "utf-8") as f: 
        b = u"";
        for l in f.readlines():
            if not isEmpty(l):
                b += l.replace(u"\n", "");
            else:
                blocks.add(removeDup(b));
                b = u"";

    blocks = list(blocks);
    blocks = filterBlocks(blocks);
    return blocks;

def filterBlocks(blocks):
    newBlocks = [];

    #Remove phone number.
    for b in blocks:
        if not re.match(r"[\d-]+", b.strip()):
            newBlocks.append(b);
    return newBlocks;


def isEmpty(s):
    if not s:
        return True;
    else:
        if re.match(ur"^[\s]*$", s):
            return True;
        else:
            return False;

def removeDup(s):
    if s:
        if len(s)%2 != 0:
            return s;

        dic = dict();
        for ch in s:
            if not dic.get(ch):
                dic[ch] = 1;
            else:
                dic[ch] = dic[ch] + 1;

        items = list(dic.iteritems());
        for ch, cnt in items[1:]:
            if cnt != items[0][1]:
                return s;

        return s[:len(dic)];
    else:
        return s;


if __name__ == '__main__':
    blocks = parseToBlocks("a.txt")
    print json.dumps(map(lambda b : b.encode("utf-8"), blocks), ensure_ascii=False);
