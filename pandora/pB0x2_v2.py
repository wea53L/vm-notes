#! /usr/bin/env python

import socket
import time
import string
import numpy


target = '192.168.56.101'
port = 54311


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target,port))

banner = s.recv(512)
prompt = s.recv(512)


for char in (string.ascii_letters + string.digits + string.punctuation):
	
	t0 = time.time()
	s.send(char + '\n')
	prompt = s.recv(512)
	t1 = time.time()

	t2 = time.time()
	s.send(char + '\n')
	prompt = s.recv(512)
	t3 = time.time()

	t4 = time.time()
	s.send(char + '\n')
	prompt = s.recv(512)
	t5 = time.time()

	t6 = time.time()
	s.send(char + '\n')
	prompt = s.recv(512)
	t7 = time.time()

	times = [(t7-t6), (t5-t4), (t3-t2), (t1-t0)]
	average = numpy.mean(times)
	
	print(char + ": " + str(average))

s.close()