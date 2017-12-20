#
# Find the valid png file in the /tmp directory. Using magic bytes.
# The code is hidden in this file.
#

import imghdr
import os

for root, dirs, files in os.walk('/tmp'):
        for name in files:
                    if imghdr.what('/tmp/'+name) == 'png':
                                    with open('/tmp/'+name, 'r') as f:
                                                                print(f.read())


