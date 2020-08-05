import requests
import re
import os

# code by lbdbcx/huyufeifei
# don't add headers in requests, or the response can't be encode!!!!!!!!!!!!!!!
# I don't know why the param "size2000:true" doesn't work. If you know, please tell me, thank you!!!

param = {
    'apikey' : '', # please go to 'https://api.lolicon.app/#/setu' to get apikey
    'size1200' : 'true'
}

if not os.path.exists('setu\\'):
    os.mkdir('setu\\')

for i in range(1, 301):
    web = requests.get('https://api.lolicon.app/setu/', params = param)
    url = re.search(r'"url":".+?"', web.text).group(0)
    url = re.sub(r'"url":"', '', url)
    url = re.sub(r'"', '', url)
    url = re.sub(r'\\', '', url)
    #print(url)
    img = requests.get(url)
    suffix = url.split('.')[-1]
    filename = 'setu\\' + str(i) + '.' + suffix
    #print('failname = ' + filename)
    with open(filename, 'wb') as f:
        f.write(img.content)
    f.close()
    print("finished image " + str(i))
print('OVER')