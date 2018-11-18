<p align="center">
    <img src="https://user-images.githubusercontent.com/5860071/48424356-2569ae80-e76b-11e8-9ccf-782510e54366.jpg" width="200px" />
    <br/>
    <a href="https://github.com/vrachieru/eon-api/releases/latest">
        <img src="https://img.shields.io/badge/version-1.0.0-brightgreen.svg?style=flat-square" alt="Version">
    </a>
    <a href="https://travis-ci.org/vrachieru/eon-api">
        <img src="https://img.shields.io/travis/vrachieru/eon-api.svg?style=flat-square" alt="Version">
    </a>
    <br/>
    E.ON Myline API wrapper
</p>

## Features

* Read messages
* Get invoices
* Download invoices

## Install

```bash
$ pip3 install git+https://github.com/vrachieru/eon-api.git
```
or
```bash
$ git clone https://github.com/vrachieru/eon-api.git
$ pip3 install ./eon-api
```

## Usage

### Reading messages

```python
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

```

```bash
$ python3 messages.py

Page size: 1
Start index: 0

Total messages: 128
Unread messages: 1

Id: 000000000
Subject: Bun venit!
Date: 2018-11-13 15:06:15
Body: 'Stimate client,\nBine ai venit pe portalul E.ON Myline!\nLinia ta direct\xc4\x83 cu noi \xc3\xae\xc5\xa3i ofer\xc4\x83:\nVizualizare \xc5\x9fi desc\xc4\x83rcare a facturii \xc3\xaen format electronic (prin activarea serviciului de factur\xc4\x83 electronic\xc4\x83)Notificare pe e-mail la emiterea facturii electronicePlata facturilor E.ON cu cardul pe platforma E.ON Myline f\xc4\x83r\xc4\x83 niciun comisionTrimiterea indexului contorului de gaze naturale \xc5\x9fi energie electric\xc4\x83 (dac\xc4\x83 a\xc5\xa3i optat pentru autocitirea contorului)Informa\xc5\xa3ii cu privire la verificarea periodic\xc4\x83 \xc5\x9fi revizia tehnic\xc4\x83 a instala\xc5\xa3iei tale de gaze naturaleGestionarea programului/conven\xc5\xa3iei de consumAbonarea la newsletter\xc3\x8entre\xc5\xa3inerea \xc5\x9fi actualizarea datelor tale de autentificarePosibilitatea modific\xc4\x83rii datelor de coresponden\xc5\xa3\xc4\x83\n\nPo\xc5\xa3i consulta ghidul utilizatorului E.ON Myline aici.\nEchipa E.ON Myline'

...
```

### Reading invoices

```python
from eon import EON

eon = EON('username', 'password')

invoice_page = eon.get_invoices('000000000000') # account_contract (you can find this in account settings via app; different for gas and electricity)

print('Total invoices: {}\n'.format(invoice_page.total_count))

print('Account balance: {}'.format(invoice_page.account_balance))
print('Unpaid value: {}\n'.format(invoice_page.unpaid_value))

for invoice in invoice_page.invoices:
    print('Number: {}'.format(invoice.number))
    print('Fiscal number: {}'.format(invoice.fiscal_number))
    print('Emission date: {}'.format(invoice.emission_date))
    print('Expiry date: {}'.format(invoice.expiry_date))
    print('Type: {}'.format(invoice.type.name))
    print('Value: {}'.format(invoice.value))
    print('Balance: {}'.format(invoice.balance))
    print('Payment status: {}'.format(invoice.payment_status.name))
    print('Bar code: {}'.format(invoice.bar_code))
    print('Electronic: {}'.format(invoice.electronic))

    for meter_detail in eon.get_invoice_meter_details(invoice.number):
        print('Consumption: {} m3 ({} KWH)'.format(meter_detail.consumption_cubic_meters, meter_detail.consumption_kwh))
        print('Old index: {}'.format(meter_detail.old_index))
        print('New index: {}'.format(meter_detail.new_index))
        print('Period: {} - {}'.format(meter_detail.period[0], meter_detail.period[1]))
```

```bash
$ python read_invoices.py
Total invoices: 18

Account balance: 203.99
Unpaid value: 203.99

Number: 000000000000
Fiscal number: 0000000000000000
Emission date: 2018-11-15 00:00:00
Expiry date: 2018-12-17 00:00:00
Type: CONSUMPTION
Value: 203.99
Balance: 203.99
Payment status: UNPAID
Barcode: 000000000000000000000000000000000000000
Electronic: False
Consumption: 113 m3 (1209.326 KWH)
Old index: 2595
New index: 2708
Period: 2018-10-03 00:00:00 - 2018-11-05 00:00:00

...
```

### Downloading invoices

```python
from eon import EON

eon = EON('username', 'password')

invoice_page = eon.get_invoices('000000000000') # account_contract (you can find this in account settings via app; different for gas and electricity)

download_path = '/home/user/documents/invoices/eon'

for invoice in invoice_page.invoices:
    print ('Downloading invoice #{}'.format(invoice.number))
    eon.download_invoice(invoice.number, download_path) # NOTE: This only works if you have electronic invoice activated.
```

## License

MIT