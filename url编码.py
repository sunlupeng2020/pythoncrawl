from urllib import parse
data ={'wd':'石原里美'}
wd = parse.urlencode(data)
print(wd)

data1 = '石原里美'
wd2 = parse.quote(data1)
print(wd2)
