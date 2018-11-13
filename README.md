<p align="center">
    <img src="https://user-images.githubusercontent.com/5860071/48424356-2569ae80-e76b-11e8-9ccf-782510e54366.jpg" width="200px" />
    <br/>
    <a href="https://github.com/vrachieru/eon-api/releases/latest">
        <img src="https://img.shields.io/badge/version-0.1.0-brightgreen.svg?style=flat-square" alt="Version">
    </a>
    <a href="https://travis-ci.org/vrachieru/eon-api">
        <img src="https://img.shields.io/travis/vrachieru/eon-api.svg?style=flat-square" alt="Version">
    </a>
    <br/>
    E.ON Myline API wrapper
</p>

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

### Reading inbox

```python
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
```

```bash
$ python3 inbox.py

Page size: 1
Start index: 0

Total messages: 2
Unread messages: 1

Id: 123456789
Subject: Bun venit!
Date: 20181113 15:06:15
Body: 'Stimate client,\nBine ai venit pe portalul E.ON Myline!\nLinia ta direct\xc4\x83 cu noi \xc3\xae\xc5\xa3i ofer\xc4\x83:\nVizualizare \xc5\x9fi desc\xc4\x83rcare a facturii \xc3\xaen format electronic (prin activarea serviciului de factur\xc4\x83 electronic\xc4\x83)Notificare pe e-mail la emiterea facturii electronicePlata facturilor E.ON cu cardul pe platforma E.ON Myline f\xc4\x83r\xc4\x83 niciun comisionTrimiterea indexului contorului de gaze naturale \xc5\x9fi energie electric\xc4\x83 (dac\xc4\x83 a\xc5\xa3i optat pentru autocitirea contorului)Informa\xc5\xa3ii cu privire la verificarea periodic\xc4\x83 \xc5\x9fi revizia tehnic\xc4\x83 a instala\xc5\xa3iei tale de gaze naturaleGestionarea programului/conven\xc5\xa3iei de consumAbonarea la newsletter\xc3\x8entre\xc5\xa3inerea \xc5\x9fi actualizarea datelor tale de autentificarePosibilitatea modific\xc4\x83rii datelor de coresponden\xc5\xa3\xc4\x83\n\nPo\xc5\xa3i consulta ghidul utilizatorului E.ON Myline aici.\nEchipa E.ON Myline'
```

## License

MIT