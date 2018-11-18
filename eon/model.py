from enum import Enum

from .mixin import *
from .util import *


class InvoiceType(Enum):
    ADVANCE = 'Avans'
    CONSUMPTION = 'Consum'

class InvoiceFilter(Enum):
    ALL = 'FF'
    SERVICES = 'SD'

class PaymentStatus(Enum):
    UNPAID = 0
    UNKNOWN = 1
    PAID = 2


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

class InvoicePage(StringMixin):
    def __init__(self, data):
        self.total_count = data.get('totalNumber')
        self.start_index = data.get('startIndex')
        self.page_size = data.get('pageSize')
        self.account_balance = data.get('accountBalance')
        self.unpaid_value = data.get('unpaidValue')
        self.invoices = list(map(Invoice, data.get('invoices')))

class Invoice(StringMixin):
    def __init__(self, data):
        self.emission_date = parse_date_time(data.get('emissionDate'))
        self.expiry_date = parse_date_time(data.get('expiryDate'))
        self.payment_status = PaymentStatus(data.get('paymentStatus'))
        self.value = data.get('value')
        self.balance = data.get('balance')
        self.type = InvoiceType(data.get('invoiceType'))
        self.number = data.get('invoiceNumber')
        self.fiscal_number = data.get('fiscalNumber')
        self.bar_code = data.get('barCode')
        self.electronic = data.get('electronic')

class InvoiceDetails(StringMixin):
    def __init__(self, data):
        self.measurement_unit = data.get('measurementUnit')
        self.period = parse_date_period(data.get('period'))
        self.price = data.get('price')
        self.product = utf8_encode(data.get('product'))
        self.quantity = data.get('quantity')
        self.vat_value = data.get('VATValue')
        self.value_without_vat = data.get('valueWithoutVAT')

class InvoiceMeterDetails(StringMixin):
    def __init__(self, data):
        self.consumption_cubic_meters = data.get('consumptionCubicMeters')
        self.consumption_kwh = data.get('consumptionKwh')
        self.type = utf8_encode(data.get('invoiceType'))
        self.measurement_unit = data.get('measurementUnit')
        self.new_index = data.get('newIndex')
        self.old_index = data.get('oldIndex')
        self.pcs = data.get('pcs')
        self.period = parse_date_period(data.get('period'))
        self.serial = data.get('series')
