import re
import codecs
import json
from json import JSONEncoder

def parseToBlocks(fileName):
    blocks = [];
    with codecs.open(fileName, "r",  "utf-8") as f: 
        b = u"";
        for l in f.readlines():
            if not isEmpty(l):
                b += l.replace(u"\n", "");
            else:
                blocks.append(b);
                b = u"";
    return blocks;


def isEmpty(s):
    if not s:
        return True;
    else:
        if re.match(ur"^[\s]*$", s):
            return True;
        else:
            return False;


if __name__ == '__main__':
    blocks = parseToBlocks("a.txt")
    print json.dumps(map(lambda b : b.encode("utf-8"), blocks), ensure_ascii=False);
