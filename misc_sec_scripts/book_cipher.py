#
# Connect to the  server at 'localhost', 10000 send any data,
# the server will respond with the required word codes
# You will find a passage of text in the file backdoor.txt write a script
# which will use that text to build a message using the recieved word codes.
# Each word code is sent on a new line and contains
# paragraph_number, line_number, word_number
# Send the expected words back to the server to retrieve the flag.
# The server expects all the words in a single transmission.
# The words should have punctuation stripped from them.
# And the words should be separated by newline characters (\n)
#

import socket
import re

# set up connection
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))
clientsocket.send('test')
data = clientsocket.recv(1024)

# clean the book data and codes
def clean(text):
        cleaned = []
            for w in text:
                        cleaned.append(re.sub('[",.?!]', '', w))
                            return cleaned

# get the codes
codes = clean(data.split('\n')[:-1])


# read in from the file
with open('backdoor.txt', 'r') as f:
        # strip commas and quotes
            text_file = f.read()
                paragraphs = clean(text_file.split('\n\n'))

                secret_phrase = ''
                for code in codes:
                        # cast into integers
                            code_ints = [int(num) for num in code.split()]
                                
                                    # get the paragraph
                                        paragraph = paragraphs[code_ints[0]-1]
                                            
                                                # get the line
                                                    lines = paragraph.split('\n')
                                                        line = lines[code_ints[1]-1]
                                                            
                                                                # get the word
                                                                    words = line.split(' ')
                                                                        word = words[code_ints[2]-1]
                                                                            
                                                                                # append to phrase
                                                                                    secret_phrase += word + '\n'
                                                                                        
                                                                                        print(secret_phrase)
                                                                                        clientsocket.send(secret_phrase)
                                                                                        response = clientsocket.recv(1024)
                                                                                        print(response)

