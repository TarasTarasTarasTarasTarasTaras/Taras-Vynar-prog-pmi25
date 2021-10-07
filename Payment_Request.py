from Validation import *


class PAYMENT_REQUEST:
    array_of_names = ["ID", "Amount", "Currency", "Payer_email", "Transaction_ID", "Payment_due_to_date", "Payment_request_date"]

    def __init__(self, id, amount, currency, payer_email, transaction_id, payment_due_to_date, payment_request_date):
        self.__validation = Validation()
        try:
            if self.__validation.validate_ID("ID", id)                                    is True:  self.id = id
            if self.__validation.validate_amount("Amount", amount)                        is True:  self.amount = amount
            if self.__validation.validate_currency("Currency", currency)                  is True:  self.currency = currency
            if self.__validation.validate_email("Email", payer_email)                     is True:  self.payer_email = payer_email
            if self.__validation.validate_transactionID("Transaction ID", transaction_id) is True:  self.transaction_id = transaction_id
            if self.__validation.validate_date("Due to date", payment_due_to_date)        is True:  self.payment_due_to_date = payment_due_to_date 
            if self.__validation.validate_date("Request date", payment_request_date)      is True:  self.payment_request_date = payment_request_date
        except ExceptionPayment as message:
            raise ValueError(str(message) + "\nError creating object")


    def __str__(self):
        string = ""
        for i in range(len(self.array_of_names)):
            string += self.array_of_names[i] + ": " + str(self.__getattribute__(self.array_of_names[i].lower()))
            if i < len(self.array_of_names) - 1: string += "\n"
        return string
    

    def get_id(self):
        return self.id
    def get_payer_email(self):
        return self.payer_email
    def get_amount(self):
        return self.amount 
    def get_currency(self):
        return self.currency
    def get_payment_request_date(self):
        return self.payment_request_date
    def get_payment_due_to_date(self):
        return self.payment_due_to_date
    def get_transaction_id(self):
        return self.transaction_id


    def set_id(self, id):
        if self.__validation.validate_ID("ID", id) is True:
            self.id = id
    def set_payer_email(self, email):
        if self.__validation.validate_email("Email", email) is True:
            self.payer_email = email
    def set_amount(self, amount):
        if self.__validation.validate_amount("Amount", amount) is True:
            self.amount = amount
    def set_currency(self, currency):
        if self.__validation.validate_currency("Currency", currency) is True:
            self.currency = currency
    def set_payment_request_date(self, date):
        if self.__validation.validate_date("Request date", date) is True:
            self.payment_request_date = date
    def set_payment_due_to_date(self, date):
        if self.__validation.validate_date("Due to date", date) is True:
            self.payment_due_to_date = date
    def set_transaction_id(self, id):
        if self.__validation.validate_transactionID("Transaction ID", id) is True:
            self.transaction_id = id


    def getAll_getters(self):
        array_of_getters = []
        for local_attr in dir(self):
            if local_attr.startswith("get_") and callable(getattr(self, local_attr)):
                array_of_getters.append(local_attr)
        return array_of_getters

