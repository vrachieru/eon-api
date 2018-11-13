import sys
sys.path.append('../')

import re

from eon import EON

eon = EON('username', 'password')

inbox = eon.get_inbox()

print ('Page size: %s' % inbox['pageSize'])
print ('Start index: %s' % inbox['startIndex'])

print ('Total messages: %s' % inbox['totalNumber'])
print ('Unread messages: %s' % inbox['unreadMessages'])

is_unread = lambda msg: not msg['read']
strip_html = lambda msg: re.sub('<[^<]+?>', '', msg)

unread = filter(is_unread, inbox['notifications'])

for notification in unread:
    message = eon.get_inbox_message(notification['id'])
    print('Id: %s' % message['id'])
    print('Subject: %s' % message['subject'].encode('utf-8'))
    print('Date: %s' % message['date'].encode('utf-8'))
    print('Body: %s' % strip_html(message['body']).encode('utf-8'))
