from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
# 使用用户名密码模拟登陆知乎网站

cookiejar = CookieJar()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

post_url=''
post_data = parse.urlencode({
    'username':''
    'password':''
})

req = request.Request(post_url, data = post_data.encode('utf-8'))
opener.open(req)

# 访问个人主页

url = '个人主页网址'
rq = request.Request(url,headers= headers) #headers中有user-agent
resp = opener.open(rq)
print(resp.read().decode('utf-8'))
