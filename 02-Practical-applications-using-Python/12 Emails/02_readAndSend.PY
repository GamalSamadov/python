"""
The send() function is used to send email from the logged in account.
To get a list of all unread emails, call the unread() function.
The summary() function returns a summary of GmailThread or GmailMessage.
The recent() function returns the most recent incoming messages to your email.
The search() function is used to search for specific messages.
"""

import ezgmail

## Print Email adress 
# print(ezgmail.EMAIL_ADDRESS)

## send message send('mail_to_send@mail.co', 'Head of message', 'Message body', 'file_to_send.file')
# ezgmail.send('uvaysalmohammady@gmail.com', 'Test line', 'Test body bla bla bla bla', ['Test.jpg', 'test1.jpg'])

## get unread messages from sing inned mail
# unreadmessages = ezgmail.unread() # returns gmailthrid object
# print(ezgmail.summary(unreadmessages))
# print()
# print(len(unreadmessages))
# print()
# print(unreadmessages[0])
# print()
# print(unreadmessages[0].messages[0])
# print()
# print(unreadmessages[0].messages[0].subject)
# print(unreadmessages[0].messages[0].body)
# print(unreadmessages[0].messages[0].timestamp)
# print(unreadmessages[0].messages[0].sender)
# print(unreadmessages[0].messages[0].recipient)

## Get resent messages
# resentThreads = ezgmail.recent()
# print(len(resentThreads))

# resentThreads = ezgmail.recent(maxResults = 50)
# print(len(resentThreads))

## search
resentThreads = ezgmail.search('amazon')
print(len(resentThreads))
print(ezgmail.summary(resentThreads))



