import sys
sys.path.append('../')

from eon import EON

eon = EON('username', 'password')

message_page = eon.get_inbox()

print ('Page size: %s' % message_page.page_size)
print ('Start index: %s' % message_page.start_index)

print ('Total messages: %s' % message_page.total_count)
print ('Unread messages: %s' % message_page.unread_count)

is_unread = lambda message: not message.read
unread_messages = filter(is_unread, message_page.messages)

for message in unread_messages:
    message = eon.get_message(message.id)
    print('Id: %s' % message.id)
    print('Subject: %s' % message.subject)
    print('Date: %s' % message.date)
    print('Body: %s' % message.body)
