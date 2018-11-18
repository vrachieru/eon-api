import sys
sys.path.append('../')

from eon import EON

eon = EON('username', 'password')

invoice_page = eon.get_invoices('000000000000') # account_contract (you can find this in account settings via app; different for gas and electricity)

download_path = '/home/user/documents/invoices/eon'

for invoice in invoice_page.invoices:
    print ('Downloading invoice #{}'.format(invoice.number))
    eon.download_invoice(invoice.number, download_path) # NOTE: This only works if you have electronic invoice activated.