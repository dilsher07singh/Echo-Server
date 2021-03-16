import socket

chooseinput = input("Pick one between the two: TCP or UDP: ") #choose from two

#start with udp code. Input:UDP
if(chooseinput == "UDP"): 
	#for client open socket conncetion
	cs = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	#gather user input
	messageinput = input("enter the string you want to modify based on rules: ")
	#if bye close connection as mentioned
	if(messageinput == "bye"):
		print("Closing connection")
		#close connection if bye entered
		cs.close()
	#else perform following
	else:
		#encoded message sent to the side of server based on port,adress
		cs.sendto(messageinput.encode("utf-8"),('127.0.0.1',8888))
		#assign from get values.
		abcde,adress = cs.recvfrom(2048)
		#print format
		print(abcde.decode("ascii"))
#conditions for user input TCP
elif(chooseinput == "TCP"):

    #CLIENT opening socket connection TCP
	z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Gather input from user or client
	es = input("enter the string you want to modify based on rules: ")
	#bye means close connection
	if(es=="bye"):
		print("Closing connection")
	#specific local adress and host connection
	z.connect(('127.0.0.1',7777))
	#send string
	z.send(bytes(es,"utf-8"))
	#recieval from server with defined bits
	message = z.recv(2048)
	#Connection closure
	z.close()
	#print format
	print(message.decode("ascii"))




