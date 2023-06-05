"""
Installing the IMAPClient package:
pip install IMAPClient

The select_folder() function is used to select a specific folder from the server.
The search() function searches for messages matching the specified query.
The fetch() function returns the specified data associated with one or more messages in the currently selected folder.


Install pyzmail package:
pip install pyzmail

The factory() function uses the appropriate parser and returns a PyzMessage object.
To get the message title, use the get_subject() function.
To get sender or recipient information, use the get_addresses() function.
The get_payload() function returns the message body as an object of class Byte.
"""

import imapclient
from pprint import pprint
import pyzmail

# connect to the server 
imapObject = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# login to email
rec_email = 'uvaysalmohammady@gmail.com'
password = 'eesahewtktbltdmd'
imapObject.login(rec_email, password)

# print all folders
pprint(imapObject.list_folders())

# select folder
imapObject.select_folder('INBOX', readonly=True)

# search in folder
UIDs = imapObject.search('ALL')
print(UIDs)

rawMessages = imapObject.fetch(1, ['BODY[]'])
pprint(rawMessages)

message = pyzmail.PyzMessage.factory(rawMessages[1][b'BODY[]'])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))

# Get message Body
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))