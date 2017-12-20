#
# Send a spoofed email.  Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@gmail.com
# Recipient needs to be zultron@thebigeye.com
#


import smtplib
from email.MIMEMultipart import import MIMEMultipart
from email.MIMEText import import MIMEText

me = 'bob-roswell-1947@gmail.com'
you = 'zultron@thebigeye.com'

msg = MIMEMultipart()
msg['From'] = me
msg['To'] = you
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

address = '127.0.0.1'
port = 1025
mailserver = smtplib.SMTP(address, port)

mailserver.sendmail(me,you, msg.as_string())

mailserver.quit()
