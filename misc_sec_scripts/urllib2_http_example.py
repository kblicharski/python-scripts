#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#

import urllib2
import urllib

url = 'http://127.0.0.1:8082'
r = urllib2.Request(url)
r.add_header('x-api-key', 'tweetbotkeyv1')
data = urllib.urlencode({'user': 'tweetbotuser',
                             'status-update': 'alientest'})
r.add_data(data)
response = urllib2.urlopen(r)
print(response.read())

