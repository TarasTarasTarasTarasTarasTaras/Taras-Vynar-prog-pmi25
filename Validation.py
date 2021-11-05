import re
import time
from datetime import date
from FlightBooking import FlightBooking

class Validation(object):
    @staticmethod
    def validate_file(value):
        if value is not str:
            raise ValueError("Filename must be str")
        if value.endswith('.txt') is not True:
            raise ValueError(value + " must be txt format")
        return value


    @staticmethod
    def validate_aviaCompany(value):
        is_valid = 0
        for i in FlightBooking.array_of_names:
            if i == value: 
                is_valid = 1
                break
        if is_valid == 0:
            raise ValueError("'aviaCompany' is bad")
        return value


    @staticmethod
    def validate_noOfPeople(value):
        if not 0 < int(value) <= 300:
            raise ValueError("'noOfPeople must' be more than 0 and less than 301")
        return value


    @staticmethod
    def validate_flightNumber(value):
        if not re.fullmatch(r'\w{2}-\d{4}', value):
            raise ValueError("'flightNumber' must be XX YYYY, X - літера, Y - цифра format")

    @staticmethod
    def validate_date(value):
        [dd, mm, yyyy] = str(value).split('.')
        day, month, year = int(dd), int(mm), int(yyyy)
        try:
            value = date(year, month, day)
        except:
            raise ValueError("Date must be in the following format: dd-mm-yyyy")
        if(year < 1980 or year > 2022):
            raise ValueError("The year cannot be less than 1980 and more than 2022")
        return value

    @staticmethod
    def validate_time(value):
        [hh, mm] =str(value).split(':')
        hour, minute = int(hh), int(mm)
        try:
            value = time(hour, minute)
        except:
            raise ValueError("Time must be in the following format: HH:MM")
        return value

    @staticmethod
    def validate_two_times(value1, value2):
        if value1 > value2:
            raise ValueError("Endtime should be later Starttime")
        return True