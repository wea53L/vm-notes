#! /usr/bin/env python

import socket
import time


target = '192.168.56.101'
port = 54311


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target,port))

banner = s.recv(512)
prompt = s.recv(512)

s.send('A\n')

t0 = time.time()
response = s.recv(512)
prompt = s.recv(512)
t1 = time.time()

s.send('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n')

t2 = time.time()
response = s.recv(512)
prompt = s.recv(512)
t3 = time.time()

print("short: " + str(t1 - t0))
print('Long: ' + str(t3 - t2))


s.close()