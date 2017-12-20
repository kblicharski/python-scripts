#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send GET_KEY to download a string.
# The string is compressed with a common algorithm found in many
# websites. Uncompress the string and print it to get the flag.
#

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))
clientsocket.send('GET_KEY')
data = clientsocket.recv(1024)

print(data)

import zlib
decompressed_data = zlib.decompress(data, 16+zlib.MAX_WBITS)
print(decompressed_data)
