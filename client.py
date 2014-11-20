#!/usr/bin/python
import time
import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host, port))
s.send('PING\r')
pre_time = time.time()
recv_line = s.recv(1024)
print recv_line
matchObj = re.match(r'.* (\d+\.?\d*)', recv_line)
if matchObj:
  print matchObj.group(1)
  server_time = matchObj.group(1)
  delta_time = float(server_time) - pre_time
  print 'delta time ' + str(delta_time)
else:
  print 'not matched'
s.close
