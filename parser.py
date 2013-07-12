import os
import re

APKTOOL_DIRECTORY = "./apktool"

def parseChannel():
    if os.system("java -jar %s/apktool.jar d -f a.apk" % APKTOOL_DIRECTORY) != 0:
        print "error";
        return "";

    for line in open("a/AndroidManifest.xml").readlines():
        m = re.match(r".*UMENG_CHANNEL\"\sandroid:value=\"(.*)\".*", line);
        if m != None:
            return m.group(1);


if __name__ == '__main__':
    print parseChannel()
