"""
The official documentation for the smtplib package:
https://docs.python.org/3/library/smtplib.html

The SMTP builder() is used to set the SMTP server settings.
The starttls() function is used to encrypt the connection.
The login() function enables you to log in as a specific user.
Emails can be sent through the sendmail() function.
"""

from smtplib import SMTP

sender_email = 'uvaysalmohammady@gmail.com'
rec_email = 'uvaysalmohammady@gmail.com'
password = 'eesahewtktbltdmd'
message = 'Subject: Message from Python. \nHello. This is message from Python!'

server = SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

print('Login Success')

server.sendmail(sender_email, rec_email, message)
print('Email has been send to: ', rec_email)

server.quit()
