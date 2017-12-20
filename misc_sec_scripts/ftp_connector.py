from ftplib import FTP

host = 'services.cyberprotection.agency'
port = 2121
user = 'secure_user'

word_file = 'words.txt'

with open(word_file) as f:
    passwords = [x.strip() for x in f.readlines()]

with FTP(host=host, user=user, passwd=password, source_address=(host, port)) as ftp:
    ftp.login()
    ftp.dir()

