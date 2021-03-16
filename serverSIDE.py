import socket
#use variable decision to get input from user
decision = input("Pick one between the two: TCP or UDP: ")

#if input:UDP server side
if(decision == "UDP"):
	#socket connection to port and adress specified
	d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	d.bind(('127.0.0.1',8888))
	#true corresponds to 1
	while 1:
		#get data and adress client side
		abcde,adress = d.recvfrom(2048)
		#decode from client
		message = abcde.decode("utf-8")

		print(f"{adress} UDP client has been connected!")


		#declare string variable for conditions
		stringf=""
		#run for loop to check. mod2=0 means even therefore upper case else vice versa.
		for y in range(len(message)):
			if y%2==0:
				stringf += message[y].upper()
			else:
				stringf += message[y].lower()
		#encode msg using variable message1
		message1 = stringf.encode("utf-8")
		#send to clientside
		d.sendto(message1,adress)
#input:TCP server side
elif(decision == "TCP" ):
	#establish opening a sock connection
	x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#connection
	x.bind(('127.0.0.1', 7777))
	#listen
	x.listen(10)

	while 1:
		#data clientso and adress ad while elstablishing connection:
		clientso, ad = x.accept()
		print(f"{ad} TCP client has been connected!")
		#similiar to client side recieves the values. Store
		abcd = clientso.recv(2048)
		#decode
		wordofclient = abcd.decode("utf-8")
		#if bye input close connection 
		if (wordofclient == "bye"):
			x.shutdown(socket.SHUT_RDWR)
			x.close()
			clientso.shutdown(socket.SHUT_RDWR)
			clientso.close()


		else:
			#declare string variable for conversion
			stringf=""
			#range of input client mod2=0 means even therefore upper else vice versa
			for y in range(len(wordofclient)):
				if y%2==0:
					stringf += wordofclient[y].upper()
				else:
					stringf += wordofclient[y].lower()
			#variable encoding
			check = stringf.encode("utf-8")
			#send to client
			clientso.send(check)

			


