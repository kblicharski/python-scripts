#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

import urllib2
from HTMLParser import import HTMLParser

class MyHTMLParser(HTMLParser):
        def __init__(self):
                    self.reset()
                            self.HTMLDATA = []

                                def handle_data(self, data):
                                            data = data.strip()
                                                    
                                                            if data:
                                                                                self.HTMLDATA.append(data)

                                                                                def make_request():
                                                                                        url = 'http://127.0.0.1:8082/selfdestruct'
                                                                                            request = urllib2.Request(url)
                                                                                                response = urllib2.urlopen(request)
                                                                                                    return response.read()

                                                                                                first_num = 1
                                                                                                second_num = 2

                                                                                                while first_num != second_num:
                                                                                                        data = make_request()
                                                                                                            parser = MyHTMLParser()
                                                                                                                parser.feed(data)
                                                                                                                    html_data = parser.HTMLDATA     
                                                                                                                        try:
                                                                                                                                    first_num = int(html_data[-3])
                                                                                                                                            second_num = int(html_data[-2])
                                                                                                                                                except ValueError:
                                                                                                                                                            break

                                                                                                                                                        print(parser.HTMLDATA)

