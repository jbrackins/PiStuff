#!/usr/bin/python
from __future__ import print_function
import poplib
from email import parser

blanks = ""

forever = 1
while forever:
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('jandvpi@gmail.com')
    pop_conn.pass_('greatwhitebuffalo')
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    #Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    for message in messages:
        subj = message['Subject']
        print (subj)
        for i in range(20):
            print (blanks)
    pop_conn.quit()
