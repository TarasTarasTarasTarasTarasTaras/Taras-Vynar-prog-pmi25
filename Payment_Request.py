from Validation import Validation
from Validation import ExceptionPayment

class PAYMENT_REQUEST:
    def __init__(self, ID, amount, currency, payer_email, transaction_id, payment_due_to_date, payment_request_date):
        self.__validation = Validation()
        try:
            if self.__validation.validate_ID("ID", ID)                                    is True:  self.__ID = ID
            if self.__validation.validate_amount("Amount", amount)                        is True:  self.__amount = amount
            if self.__validation.validate_currency("Currency", currency)                  is True:  self.__currency = currency
            if self.__validation.validate_email("Email", payer_email)                     is True:  self.__payer_email = payer_email
            if self.__validation.validate_transactionID("Transaction ID", transaction_id) is True:  self.__transaction_id = transaction_id
            if self.__validation.validate_date("Due to date", payment_due_to_date)        is True:  self.__payment_due_to_date = payment_due_to_date 
            if self.__validation.validate_date("Request date", payment_request_date)      is True:  self.__payment_request_date = payment_request_date
        except ExceptionPayment as message:
            raise ValueError(str(message) + "\nError creating object")


    def __str__(self):
        return('"ID": ' + str(self.__ID) +
               '\n"Amount": ' + str(self.__amount) +
               '\n"Currency": ' + str(self.__currency) +
               '\n"Email": ' + str(self.__payer_email) + 
               '\n"TransactionID": ' + str(self.__transaction_id) + 
               '\n"Due_to_date": ' + str(self.__payment_due_to_date) +  
               '\n"Request_date": ' + str(self.__payment_request_date) + '\n')


    def get_id(self):
        return self.__ID
    def get_payer_email(self):
        return self.__payer_email
    def get_amount(self):
        return self.__amount 
    def get_currency(self):
        return self.__currency
    def get_payment_request_date(self):
        return self.__payment_request_date
    def get_payment_due_to_date(self):
        return self.__payment_due_to_date
    def get_transaction_id(self):
        return self.__transaction_id


    def set_id(self, id):
        if self.__validation.validate_ID("ID", id) is True:
            self.__ID = id
    def set_payer_email(self, email):
        if self.__validation.validate_email("Email", email) is True:
            self.__payer_email = email
    def set_amount(self, amount):
        if self.__validation.validate_amount("Amount", amount) is True:
            self.__amount = amount
    def set_currency(self, currency):
        if self.__validation.validate_currency("Currency", currency) is True:
            self.__currency = currency
    def set_payment_request_date(self, date):
        if self.__validation.validate_date("Request date", date) is True:
            self.__payment_request_date = date
    def set_payment_due_to_date(self, date):
        if self.__validation.validate_date("Due to date", date) is True:
            self.__payment_due_to_date = date
    def set_transaction_id(self, id):
        if self.__validation.validate_transactionID("Transaction ID", id) is True:
            self.__transaction_id = id


    def getAll_getters(self):
        array_of_getters = []
        for local_attr in dir(self):
            if local_attr.startswith("get_") and callable(getattr(self, local_attr)):
                array_of_getters.append(local_attr)
        return array_of_getters

