import re
from datetime import date

class ExceptionPayment(Exception) : 
    def __init__(self, message: str = ''):
        self.message = message

    def __str__(self) -> str:
        return self.message


def decoratorValidate(validate):
    def decorator(*args, **kwargs):
        try:
            validate(*args, **kwargs)
            return True
        except ValueError as message:
            raise ExceptionPayment(  "ERROR validating " + args[1] + ": " + str(message))
    return decorator


class Validation:
    def __init__(self):
        pass

    def validate_is_str(self, key, value):
        if type(value) is not str:
            raise ValueError(key + " must be string")


    def validate_file(self, key, value):
        self.validate_is_str(key, value)
        
        if value.endswith('.txt') is not True:
            raise ValueError(value + " must be txt format")
        return True


    @decoratorValidate
    def validate_PAYMENT(self, key, value):
        self.validate_ID("ID", value.get_id())
        self.validate_amount("Amount", value.get_amount())
        self.validate_currency("Currency", value.get_currency())
        self.validate_email("Email", value.get_payer_email())
        self.validate_transactionID("TransactionID", value.get_transaction_id())
        self.validate_date("Due to date", value.get_payment_due_to_date())
        self.validate_date("Request date", value.get_payment_request_date())


    @decoratorValidate
    def validate_ID(self, key, value):
        if type(value) is int:
            if value < 0 or value > 999999:
                raise ValueError(key + " must be no less than 0 and no more than 999999")
        self.validate_is_str(key, value)
            
        if not re.fullmatch(r'[0-9]{1,6}', str(value)):
            raise ValueError(key + " must contains only 1-6 numbers")


    @decoratorValidate
    def validate_amount(self, key, value):
        if type(value) is int:
            if value < 0 or value > 999999:
                raise ValueError(key + " must be no less than 0 and no more than 999999")
        self.validate_is_str(key, value)
        
        if not re.fullmatch(r'[0-9]{1,6}', str(value)):
            raise ValueError(key + " must contains only 1-6 numbers")


    @decoratorValidate
    def validate_currency(self, key, value):
        self.validate_is_str(key, value)

        if value != "USD" and value != "EUR" and value != "UAH":
            raise ValueError(key + " must be only USD/EUR/UAH")


    @decoratorValidate
    def validate_date(self, key, value):
        self.validate_is_str(key, value)
        
        [dd, mm, yyyy] = str(value).split('.')
        day, month, year = int(dd), int(mm), int(yyyy)
        try:
            value = date(year, month, day)
        except ValueError:
            raise ValueError(key + " must be in the following format: dd-mm-yyyy")
        if(year < 1980 or year > 2021):
            raise ValueError("  The year cannot be less than 1980 and more than 2021")


    @decoratorValidate
    def validate_email(self, key, value):
        self.validate_is_str(key, value)
        
        if not re.fullmatch(r'[A-Z a-z 0-9 _@.-]{,50}', value): 
            raise ValueError(key + " must be less than 50 symbols\n  and contains only the following characters: A-Z, a-z, 0-9, _, @, - and .")

        

    @decoratorValidate
    def validate_transactionID(self, key, value):
        self.validate_is_str(key, value)
        if not re.fullmatch(r'\d{8}-\d{2}', value):
            raise ValueError(key + " must be in the format: ********-** and contains only numbers")

