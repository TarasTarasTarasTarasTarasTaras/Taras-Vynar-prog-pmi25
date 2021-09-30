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
        return('"ID": "' + str(self.__ID) + '",' +
                '\n"Amount": "' + self.__amount + '",' +
                '\n"Currency": "' + str(self.__currency) + '",' +
                '\n"Email": "' + self.__payer_email + '",' + 
                '\n"Transaction ID": "' + self.__transaction_id + '",' + 
                '\n"Due to date": "' + str(self.__payment_due_to_date) + '",' + 
                '\n"Request date": "' + str(self.__payment_request_date) + '"\n')


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


    def getAll_getters(self):
        array_of_getters = []
        for local_attr in dir(self):
            if local_attr.startswith("get_") and callable(getattr(self, local_attr)):
                array_of_getters.append(local_attr)
        return array_of_getters

