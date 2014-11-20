import urllib

target_file = 'temp.jpg'
f = open(target_file, 'wb')
url = 'http://img4.cache.netease.com/photo/0026/2013-11-14/9DLOE4SE4CJ80026.jpg'
f.write(urllib.urlopen(url).read())
f.close()

target_file2 = 'temp2.jpg'
urllib.urlretrieve(url, target_file2)
