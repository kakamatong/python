import os
import sys
import re
fileName = "log.txt"
#filePath = os.path.join(os.getcwd(), fileName)
with open(fileName) as f:
    lines = f.readlines()
    for line in lines:
        read = re.findall(r"libcocos2dcpp.so \+ (.+)", line, re.I)
        if read:
            print(read)
            command = "aarch64-linux-android-addr2line -e libcocos2dcpp.so %s" % read[0]
            os.system(command)
            #print(command)
            pass
        else:
            print("not libcocos2dcpp")
            pass
input("Prease <enter>")