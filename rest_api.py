#!/usr/bin/python
# http://isbullsh.it/2012/06/Rest-api-in-python/

# use urllib2
github_url = 'https://api.github.com/user/repos'

request = urllib2.Request(github_url, urllib.urlencode({'name':'Test repo', 'description': 'Some test repository'})) # Manual encoding required
handler = urllib2.urlopen(request)

handler = urllib2.urlopen(request)
print handler.read()
