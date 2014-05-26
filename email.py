#!/usr/bin/env python3

import smtplib

server = 'mail.server.com'
user = ''
password = ''

recipients = ['jubear.720@gmail.com']
sender = 'vicweiss94@gmail.com'
message = 'Hello World'

session = smtplib.SMTP(server)
# if your SMTP server doesn't need authentications,
# you don't need the following line:
session.login(user, password)
session.sendmail(sender, recipients, message)