from Validation import *


class PAYMENT_REQUEST:
    array_of_names = ["id", "amount", "currency", "payer_email", "transaction_id", "payment_due_to_date", "payment_request_date"]

    def __init__(self, id, amount, currency, payer_email, transaction_id, payment_due_to_date, payment_request_date):
        self.__validation = Validation()
        try:
            self.set_id(id)
            self.set_amount(amount)
            self.set_currency(currency)
            self.set_payer_email(payer_email)
            self.set_transaction_id(transaction_id)
            self.set_payment_due_to_date(payment_due_to_date)
            self.set_payment_request_date(payment_request_date)
            Validation.validate_two_dates(self.payment_due_to_date, self.payment_request_date)
        except ExceptionPayment as message:
            raise ValueError(str(message) + "\nError creating object")


    def __str__(self):
        string = ""
        for i in range(len(self.array_of_names)):
            string += self.array_of_names[i] + ": " + str(self.__getattribute__(self.array_of_names[i])).lower()
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


    @Validation.validate_ID
    def set_id(self, id):
        self.id = id
    @Validation.validate_amount
    def set_amount(self, amount):
        self.amount = amount
    @Validation.validate_currency
    def set_currency(self, currency):
        self.currency = currency
    @Validation.validate_email
    def set_payer_email(self, email):
        self.payer_email = email
    @Validation.validate_date
    def set_payment_request_date(self, date):
        self.payment_request_date = date
    @Validation.validate_date
    def set_payment_due_to_date(self, date):
        self.payment_due_to_date = date
    @Validation.validate_transactionID
    def set_transaction_id(self, id):
        self.transaction_id = id


    def getAll_getters(self):
        array_of_getters = []
        for local_attr in dir(self):
            if local_attr.startswith("get_") and callable(getattr(self, local_attr)):
                array_of_getters.append(local_attr)
        return array_of_getters