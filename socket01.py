import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)
#mysockrecv = mysock.send(cmd)
#print(mysockrecv)

while True:
    data = mysock.recv(512)
    #print(data)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()