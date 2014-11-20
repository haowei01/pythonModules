#!/usr/bin/python
import time
import socket
import re

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
s.send('PING\r')
recv_line = s.recv(1024)
print recv_line
matchObj = re.match(r'.* (\d+\.?\d*)', recv_line)
if matchObj:
  print matchObj.group(1)
else:
  print 'not matched'
s.close
