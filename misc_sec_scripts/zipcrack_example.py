import zipfile
import itertools
import time

# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        pass

zipfilename = 'planz.zip'
first_half_password = 'password'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet.upper()
numbers = '0123456789'

zip_file = zipfile.ZipFile(zipfilename)

for c in itertools.product(alphabet+alphabet_upper+numbers, repeat=3):
    password = first_half_password + ''.join(c)
    print("Trying {}".format(password))

    if extractFile(zip_file, password):
        print('*' * 20)
        print('Password found: {}'.format(password))
        print('Files extracted...')
        exit(0)
print('Password not found.')
