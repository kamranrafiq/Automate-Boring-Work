import socket
port_numbers = input("Enter the port number: ")

service = socket.getservbyport(int(port_numbers))
print ("Port number",port_numbers,"runs service:", service.upper())