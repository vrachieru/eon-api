from enum import Enum

from .mixin import *
from .util import *

class MessagePage(StringMixin):
    def __init__(self, data):
        self.total_count = data.get('totalNumber')
        self.unread_count = data.get('unreadMessages')
        self.start_index = data.get('startIndex')
        self.page_size = data.get('pageSize')
        self.messages = list(map(MessageSummary, data.get('notifications')))

class MessageSummary(StringMixin):
    def __init__(self, data):
        self.id = data.get('id')
        self.subject = utf8_encode(data.get('subject'))
        self.date = parse_date_time(data.get('date'))
        self.read = data.get('read')

class Message(MessageSummary):
    def __init__(self, data):
        super().__init__(data)
        self.body = utf8_encode(data.get('body'))
