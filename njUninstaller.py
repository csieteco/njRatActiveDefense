import time
import socket
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname() # host is needed for Internet Connections
port = 2020
 
s.bind((host, port))
s.listen(500)           	# 500 clients
 
while True:
    clientSocket, addr = s.accept()
    print("got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
	mssg = '''un|'|'|~'''
    clientSocket.send(str(len(mssg))+'\x00'+mssg)
    time.sleep(1)
    print(" - Infected client on %s uninstalled" % str(addr))
	clientSocket.close()
