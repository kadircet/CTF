from socket import *;
from os import *;
import time;

ip = "127.0.0.";
port = 0xdead;
pssw = "HELICOTRMA";

timeout(10)
for i in range(10):
	if(fork()==0):
		ip += str(i+10);
		s = socket(AF_INET, SOCK_STREAM);
		s.bind((ip, 0));
		s.connect(("localhost", 24027));
	
		val = s.recv(1024);
		print ip + "<" + val;
		tosend = [0]*20
		for i in range(len(pssw)):
			tosend[i] = ord(val[i])^ord(pssw[i]);
		s.send(bytearray(tosend));
		#print ip + ">" + tosend;
		time.sleep(5);
		
		print "YEEEY:" + s.recv(1024);
		s.close();
		break;

