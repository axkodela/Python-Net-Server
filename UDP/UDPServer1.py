import socket, sys, string

def processData(data):
	if data[0:2] == "U:":
		return data[2:].upper()
	elif data[0:2] == "L:":
		return data[2:].lower()
	elif data[0:2] == "X:":
		return data[2:]
	else:
		return "Invalid Command. Try another one..."

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.1.35', 10000)
sck.bind(server_address)

while True:
	data, address = sck.recvfrom(4096)
	if data:
		sent = sck.sendto(processData(data), address)
		
