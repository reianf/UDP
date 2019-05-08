import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_address = ('127.0.0.1', 5432)
sock_address2 = ('127.0.0.1', 5433)
message = input("Message to send to server: ")
sock.bind(sock_address2)
try:
	#Send data
	print('Sending "%s"' % message)
	sock.sendto(message.encode(), sock_address)

	#Recieve response
	print("Waiting to recieve message..")
	data, server = sock.recvfrom(4096)
	print('Received: "%s"' % data.decode())
finally:
	print('Closing socket')
	sock.close()
