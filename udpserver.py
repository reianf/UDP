import socket

#Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 5432)
server_address2 = ('127.0.0.1', 5433)
print("Starting up on %s port %s" % server_address)

#Bind the socket to the port
sock.bind(server_address)

while True:
	print("Waiting to receive message..")
	
	data, server = sock.recvfrom(4096)
	result = data.decode()
	
	print('Received: "%s"' % result)
	
	message = input("Message to send back to client: ")
	data = message.encode()

	if data:
		print("Sending back data to client from %s port %s" % server_address2)
		sock.sendto(data, server_address2)
