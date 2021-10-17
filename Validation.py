import re
from datetime import *

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
            raise ExceptionPayment(  "ERROR validating " + str(args[1]) + ": " + str(message))
    return decorator


class Validation:
    def __init__(self):
        pass

    @staticmethod
    def validate_is_str(key, value):
        if type(value) is not str:
            raise ValueError(key + " must be string")


    def validate_file(self, key, value):
        self.validate_is_str(key, value)
        
        if value.endswith('.txt') is not True:
            raise ValueError(value + " must be txt format")
        return True


    @staticmethod
    def validate_PAYMENT(key, item):
        Validation.validate_ID(lambda value : value)
        Validation.validate_amount(lambda value : value)
        Validation.validate_currency(lambda value : value)
        Validation.validate_email(lambda value : value)
        Validation.validate_transactionID(lambda value : value)
        Validation.validate_date(lambda value : value)
        Validation.validate_date(lambda value : value)


    @staticmethod
    def validate_ID(function):
        def decorator(*args, **kwargs):
            if type(args[1]) is int:
                if args[1] < 0 or args[1] > 999999:
                    raise ValueError("ID must be no less than 0 and no more than 999999")
            Validation.validate_is_str("ID", str(args[1]))        
            
            if not re.fullmatch(r'[0-9]{1,6}', str(args[1])):
                raise ValueError("ID must contains only 1-6 numbers")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_amount(function):
        def decorator(*args, **kwargs):
            if type(args[1]) is int:
                if args[1] < 0 or args[1] > 999999:
                    raise ValueError("Amount must be no less than 0 and no more than 999999")
            Validation.validate_is_str("Amount", str(args[1]))        
        
            if not re.fullmatch(r'[0-9]{1,6}', str(args[1])):
                raise ValueError("Amount must contains only 1-6 numbers")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_currency(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Date", str(args[1]))        
            if args[1] != "usd" and args[1] != "eur" and args[1] != "uah":
                raise ValueError("Currency must be only usd/eur/uah")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_date(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Date", str(args[1]))        
            [dd, mm, yyyy] = str(args[1]).split('.')
            day, month, year = int(dd), int(mm), int(yyyy)
            try:
                value = date(year, month, day)
            except ValueError:
                raise ValueError("Date must be in the following format: dd-mm-yyyy")
            if(year < 1980 or year > 2021):
                raise ValueError("  The year cannot be less than 1980 and more than 2021")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_two_dates(date1, date2):
        [d1, m1, y1] = str(date1).split('.')
        [d2, m2, y2] = str(date2).split('.')
        day, month, year = int(d1), int(m1), int(y1)
        _date1 = date(year, month, day)
        day, month, year = int(d2), int(m2), int(y2)
        _date2 = date(year, month, day)
        if _date1 > _date2:
            raise ExceptionPayment("'Due to date' can not be later than 'request to date'")


    @staticmethod
    def validate_email(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Payer email", str(args[1]))        
            if not re.fullmatch(r'[A-Z a-z 0-9 _@.-]{,50}', str(args[1])): 
                raise ValueError("Payer email must be less than 50 symbols\n  and contains only the following characters: A-Z, a-z, 0-9, _, @, - and .")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_transactionID(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Transaction ID", str(args[1]))
            if not re.fullmatch(r'\d{8}-\d{2}', str(args[1])):
                raise ValueError("Transaction ID must be in the format: ********-** and contains only numbers")
            function(*args, **kwargs)
        return decorator