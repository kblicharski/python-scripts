#
# Browse the contents of these alien directories found in /tmp/aliendir to find
# the flag
#
#

import os

for root, dirs, files in os.walk('/tmp/aliendir'):
        for name in files:
                    if name:
                                    print(name)

