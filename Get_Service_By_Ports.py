import socket
for x in range(0, 65):
    try:
        ports = socket.getservbyport(x)
        print("Port Number ",x, " runs service ", ports.upper())
    except:
        continue