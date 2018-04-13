import requests
import re
import io
import sys
import time
local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text

reg = r"(az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
imgUrl = url + a
print(imgUrl)
read = requests.get(imgUrl)
f = open('image/%s.jpg' % local, 'wb')
f.write(read.content)
f.close()