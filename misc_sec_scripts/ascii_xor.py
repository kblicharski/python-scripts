#
# Setup server listening on ('localhost', 10000)
# recieve data then send back XORed with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

def debugMsg(msg):
      # Use this function if you need any debug messages
        with open("/tmp/userdebug.log", "a") as myfile:
                myfile.write(msg + "\n")

                def sxor(s1,s2):    
                      # convert strings to a list of character pair tuples
                        # go through each tuple, converting them to ASCII code (ord)
                          # perform exclusive or on the ASCII code
                            # then convert the result back to ASCII (chr)
                              # merge the resulting array of characters as a string
                                return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
                                
                            import socket

                            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            serversocket.bind(('localhost', 10000))
                            serversocket.listen(10)

                            while True:
                                  clientsocket, address = serversocket.accept()
                                    data = clientsocket.recv(1024)
                                      
                                        if len(data) > 0:
                                                debugMsg('\nReceived: {}'.format(data))

                                                    key = 'attackthehumans'
                                                        debugMsg('\nKey: {}'.format(key))

                                                            xored_data = sxor(data, key)
                                                                debugMsg('\nDecoded message: {}'.format(xored_data))

                                                                    clientsocket.send(xored_data)
                                                                        response = clientsocket.recv(1024)
                                                                            print(response)
                                                                                debugMsg('\nResponse: {}'.format(response))
                                                                                    
                                                                                        break
                                                                                        

