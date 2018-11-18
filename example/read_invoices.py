import sys
sys.path.append('../')

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
    print('Barcode: {}'.format(invoice.bar_code))
    print('Electronic: {}'.format(invoice.electronic))

    for meter_detail in eon.get_invoice_meter_details(invoice.number):
        print('Consumption: {} m3 ({} KWH)'.format(meter_detail.consumption_cubic_meters, meter_detail.consumption_kwh))
        print('Old index: {}'.format(meter_detail.old_index))
        print('New index: {}'.format(meter_detail.new_index))
        print('Period: {} - {}'.format(meter_detail.period[0], meter_detail.period[1]))
