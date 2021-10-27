from Payment_Request import *
from Container_PaymentRequest import *
valid_payment1 = PAYMENT_REQUEST('1', '250', 'uah', 'taras.vynar@gmail.com', '91347253-12', '12.04.2017', '14.07.2017')
valid_payment2 = PAYMENT_REQUEST('10', '2500', 'eur', 'taras.vynar@lnu.edu.ua', '48573719-51', '05.01.2018', '21.05.2018')
valid_payment3 = PAYMENT_REQUEST('100', '25000', 'usd', 'taras.vynar@lnu.edu.ua', '13528523-11', '25.09.2019', '31.12.2019')


dictValidAttr1 = {'id' : '1', 'amount' : '250', 'currency' : 'uah', 'payer_email' : 'taras.vynar@lnu.edu.ua',
    'transaction_id' : '91347253-12', 'get_payment_due_to_date' : '12.04.2017', 'get_payment_request_date' : '14.07.2017'} 
dictValidAttr2 = {'id' : '10', 'amount' : '2500', 'currency' : 'eur', 'payer_email' : 'taras.vynar@lnu.edu.ua',
    'transaction_id' : '48573719-51', 'get_payment_due_to_date' : '05.01.2018', 'get_payment_request_date' : '21.05.2018'} 
dictValidAttr3 = {'id' : '100', 'amount' : '250000', 'currency' : 'usd', 'payer_email' : 'taras.vynar@lnu.edu.ua',
    'transaction_id' : '13528523-11', 'get_payment_due_to_date' : '25.09.2019', 'get_payment_request_date' : '31.12.2019'} 


basedata_payments = [valid_payment1, valid_payment2, valid_payment3]
basedata_valid_attr = [dictValidAttr1, dictValidAttr2, dictValidAttr3]


#invalid_payment = PAYMENT_REQUEST('2', 'rqw', 'wf', '=/?-!', '2354-5265', '20.22.2025', '38.-1.2029')