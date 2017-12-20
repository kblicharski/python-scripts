#
# Connect to alien server ('localhost', 10000),
# Then send USER followed by aliensignal,
# Then send PASS followed by unlockserver,
# Next SEND followed by moonbase.
# Then send END and if all followed key will provided.
#
# Note: You must recieve data back from the server after you send each message
#

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))

clientsocket.send('USER')
data = clientsocket.recv(1024)
print(data)

clientsocket.send('aliensignal')
data = clientsocket.recv(1024)
print(data)

clientsocket.send('PASS')
data = clientsocket.recv(1024)
print(data)

clientsocket.send('unlockserver')
data = clientsocket.recv(1024)
print(data)

clientsocket.send('SEND')
data = clientsocket.recv(1024)
print(data)

clientsocket.send('moonbase')
data = clientsocket.recv(1024)
print(data)

clientsocket.send('END')
data = clientsocket.recv(1024)
print(data)

