import requests
import re

headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Accept-Encoding" : "gzip, deflate, br",
    "DNT" : "1",
    "Connection" : "cloes"
}


regex_text = re.compile(r'<div class="page-content">(.|\n)+</pre>')
regex_title = re.compile(r'<h1>(.|\n)*?</h1>')
regex_rubbish1 = re.compile(r'<script>(.|\n)*?</script>')
regex_rubbish2 = re.compile(r'<(.|\n)*?>')

for i in range(1, 425):
    address = 'https://www.xiaoshuodaquan.com/longmushijie/' + str(i)
    source = requests.get(address)
    source.encoding = 'gbk'
    html = str(source.text)
    text = re.search(regex_text, html).group(0)
    title = re.search(regex_title, html).group(0)
    text = re.sub(regex_rubbish1, '', text)
    text = re.sub(regex_rubbish2, '', text)
    title = re.sub(regex_rubbish2, '', title)

    with open('a.txt', 'a') as f:
        f.write(title + '\n\n')
        f.write(text + '\n\n')
    f.close()
    print('finished chapter ' + str(i))

print('OVER')