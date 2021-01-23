from urllib import request
url = 'https://piaofang.maoyan.com/dashboard'
# resp1 = request.urlopen(url)
# print(resp1.read().decode('utf-8'))


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
rq =request.Request(url, headers= headers)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))
