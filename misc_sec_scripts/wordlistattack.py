import subprocess
import itertools

passwordfile = './strings2'
dictionary = 'realhuman_phill.txt'

with open(dictionary) as f:
    words = [x.strip() for x in f.readlines()]

for word in words:
    phrase = ''.join(word)
    print(phrase)
    output = subprocess.check_output([filename, phrase])
    print(output)
