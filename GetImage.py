import requests
import re
import io
import sys
import os
import time

def getBYImage():
    nowTime = time.strftime("%Y.%m.%d")
    filePath = 'image/' + '%s.jpg' % nowTime
    if os.path.exists(filePath):
        print("isExists %s" % filePath)
        pass
    else:
        url = 'http://cn.bing.com/'
        con = requests.get(url)
        content = con.text
        reg = r"(az/hprichbg/rb/.*?.jpg)"
        a = re.findall(reg, content, re.S)[0]
        imgUrl = url + a
        print(imgUrl)
        read = requests.get(imgUrl)
        f = open(filePath, 'wb')
        f.write(read.content)
        f.close()
        pass