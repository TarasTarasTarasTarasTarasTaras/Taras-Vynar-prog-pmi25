import unittest
from Payment_Request import *
from basedata_test import basedata_valid_attr

map_attr = ['id', 'amount', 'currency', 'payer_email', 'transaction_id', 'get_payment_due_to_date', 'get_payment_request_date']

class TestPayment_Getter(unittest.TestCase):
    payment = PAYMENT_REQUEST(basedata_valid_attr[0][map_attr[0]],
                              basedata_valid_attr[0][map_attr[1]],
                              basedata_valid_attr[0][map_attr[2]],
                              basedata_valid_attr[0][map_attr[3]],
                              basedata_valid_attr[0][map_attr[4]],
                              basedata_valid_attr[0][map_attr[5]],
                              basedata_valid_attr[0][map_attr[6]],)

    def test_get_id(self):
        self.assertEqual(self.payment.get_id(), basedata_valid_attr[0][map_attr[0]])


    def test_get_amount(self):
        self.assertEqual(self.payment.get_amount(), basedata_valid_attr[0][map_attr[1]])


    def test_get_currency(self):
        self.assertEqual(self.payment.get_currency(), basedata_valid_attr[0][map_attr[2]])


    def test_get_payer_email(self):
        self.assertEqual(self.payment.get_payer_email(), basedata_valid_attr[0][map_attr[3]])


    def test_get_transaction_id(self):
        self.assertEqual(self.payment.get_transaction_id(), basedata_valid_attr[0][map_attr[4]])


    def test_get_due_to_date(self):
        self.assertEqual(self.payment.get_payment_due_to_date(), basedata_valid_attr[0][map_attr[5]])


    def test_get_request_date(self):
        self.assertEqual(self.payment.get_payment_request_date(), basedata_valid_attr[0][map_attr[6]])


    
class TestPayment_Setter(unittest.TestCase):
    payment = PAYMENT_REQUEST(basedata_valid_attr[0][map_attr[0]],
                              basedata_valid_attr[0][map_attr[1]],
                              basedata_valid_attr[0][map_attr[2]],
                              basedata_valid_attr[0][map_attr[3]],
                              basedata_valid_attr[0][map_attr[4]],
                              basedata_valid_attr[0][map_attr[5]],
                              basedata_valid_attr[0][map_attr[6]],)


    def test_set_id(self):
        self.assertEqual(self.payment.get_id(), basedata_valid_attr[0][map_attr[0]])
        self.payment.set_id(basedata_valid_attr[1][map_attr[0]])
        self.assertEqual(self.payment.get_id(), basedata_valid_attr[1][map_attr[0]])


    def test_set_amount(self):
        self.assertEqual(self.payment.get_amount(), basedata_valid_attr[0][map_attr[1]])
        self.payment.set_amount(basedata_valid_attr[1][map_attr[1]])
        self.assertEqual(self.payment.get_amount(), basedata_valid_attr[1][map_attr[1]])

    def test_set_currency(self):
        self.assertEqual(self.payment.get_currency(), basedata_valid_attr[0][map_attr[2]])
        self.payment.set_currency(basedata_valid_attr[1][map_attr[2]])
        self.assertEqual(self.payment.get_currency(), basedata_valid_attr[1][map_attr[2]])


    def test_set_payer_email(self):
        self.assertEqual(self.payment.get_payer_email(), basedata_valid_attr[0][map_attr[3]])
        self.payment.set_payer_email(basedata_valid_attr[1][map_attr[3]])
        self.assertEqual(self.payment.get_payer_email(), basedata_valid_attr[1][map_attr[3]])


    def test_set_transaction_id(self):
        self.assertEqual(self.payment.get_transaction_id(), basedata_valid_attr[0][map_attr[4]])
        self.payment.set_transaction_id(basedata_valid_attr[1][map_attr[4]])
        self.assertEqual(self.payment.get_transaction_id(), basedata_valid_attr[1][map_attr[4]])


    def test_set_due_to_date(self):
        self.assertEqual(self.payment.get_payment_due_to_date(), basedata_valid_attr[0][map_attr[5]])
        self.payment.set_payment_due_to_date(basedata_valid_attr[1][map_attr[5]])
        self.assertEqual(self.payment.get_payment_due_to_date(), basedata_valid_attr[1][map_attr[5]])


    def test_set_request_date(self):
        self.assertEqual(self.payment.get_payment_request_date(), basedata_valid_attr[0][map_attr[6]])
        self.payment.set_payment_request_date(basedata_valid_attr[1][map_attr[6]])
        self.assertEqual(self.payment.get_payment_request_date(), basedata_valid_attr[1][map_attr[6]])




if __name__ == '__main__':
    unittest.main()