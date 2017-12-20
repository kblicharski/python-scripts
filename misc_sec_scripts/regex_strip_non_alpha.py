#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#

import re

with open('/tmp/destroymoonbase.gif', 'r') as f:
      content = f.read()
        
        cleaned = re.sub(r'\W+','', content)
        print(cleaned)
